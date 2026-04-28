"""
preprocess_book2.py — Markdown → TTS-ready plain text for Book 2: The Creator's Blueprint

Reads Ch01–Ch15 + AppA–AppD from Book_2_The_Creators_Blueprint/Manuscript/,
strips all markdown formatting, converts tables to spoken prose, and produces:
  - 00_Audio/chapters/ChXX_clean.txt  (per-chapter)
  - 00_Audio/book2_tts_ready.txt      (single concatenated file)
  - 00_Audio/chapter_titles.json      (metadata index)
"""

import re
import json
import os
from pathlib import Path

BASE = Path(__file__).parent
MANUSCRIPT = BASE.parent / "01_Genesis_Physics" / "Book_2_The_Creators_Blueprint" / "Manuscript"
OUTPUT_DIR = BASE
CHAPTERS_DIR = OUTPUT_DIR / "chapters"
CHAPTERS_DIR.mkdir(parents=True, exist_ok=True)

CHAPTER_FILES = [f"Ch{i:02d}.md" for i in range(1, 16)]
APPENDIX_FILES = [
    "AppA_Family_Discussion_Guide.md",
    "AppB_Simplified_Glossary.md",
    "AppC_Recommended_Reading.md",
    "AppD_Experiments_At_Home.md",
]
ALL_FILES = CHAPTER_FILES + APPENDIX_FILES


def table_to_prose(table_lines):
    """Convert a markdown pipe table to spoken prose sentences."""
    rows = []
    for line in table_lines:
        line = line.strip()
        if not line.startswith("|"):
            continue
        # Skip separator rows (---|---|---)
        if re.match(r"^[|\s\-:]+$", line):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        rows.append(cells)

    if not rows:
        return ""

    headers = rows[0]
    data_rows = rows[1:]

    if not data_rows:
        # Just headers, no data
        return "Table: " + ", ".join(headers) + "."

    # Detect if this is the experiments table by looking for known columns
    col_lower = [h.lower() for h in headers]
    is_experiment_table = "experiment" in col_lower

    sentences = []
    for row in data_rows:
        if len(row) < len(headers):
            row = row + [""] * (len(headers) - len(row))

        row_dict = {headers[i]: row[i] for i in range(len(headers))}

        if is_experiment_table:
            exp = row_dict.get("Experiment", "")
            ch = row_dict.get("Chapter", "")
            time = row_dict.get("Time", "")
            materials = row_dict.get("Materials", "")
            ages = row_dict.get("Age Range", "")
            concept = row_dict.get("Concept", "")
            if exp:
                parts = [f"Experiment: {exp}."]
                if ch:
                    parts.append(f"Chapter {ch}.")
                if time:
                    parts.append(f"Time needed: {time}.")
                if materials:
                    parts.append(f"Materials: {materials}.")
                if ages:
                    parts.append(f"Suitable for ages {ages}.")
                if concept:
                    parts.append(f"Concept: {concept}.")
                sentences.append(" ".join(parts))
        else:
            # Generic: "Header: value. Header: value."
            parts = [f"{k}: {v}." for k, v in row_dict.items() if v]
            if parts:
                sentences.append(" ".join(parts))

    return "\n".join(sentences)


def clean_markdown(raw_text: str) -> tuple[str, str]:
    """
    Returns (chapter_title, cleaned_body).
    """
    lines = raw_text.split("\n")
    title = ""
    out_lines = []
    i = 0

    while i < len(lines):
        line = lines[i]

        # --- Detect start of a markdown table ---
        if line.strip().startswith("|"):
            table_block = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                table_block.append(lines[i])
                i += 1
            prose = table_to_prose(table_block)
            if prose:
                out_lines.append("")
                out_lines.append(prose)
                out_lines.append("")
            continue

        # --- H1: chapter title ---
        m = re.match(r"^#\s+(.+)", line)
        if m:
            raw_title = m.group(1).strip()
            # Strip markdown bold/italic from title
            raw_title = re.sub(r"\*\*\*(.+?)\*\*\*", r"\1", raw_title)
            raw_title = re.sub(r"\*\*(.+?)\*\*", r"\1", raw_title)
            raw_title = re.sub(r"\*(.+?)\*", r"\1", raw_title)
            if not title:
                title = raw_title
            i += 1
            continue

        # --- H2+: section headings — strip ## and §N. prefix ---
        m = re.match(r"^#{2,}\s*(.+)", line)
        if m:
            heading = m.group(1).strip()
            # Strip §N. prefix (e.g. "§1. " or "§12. ")
            heading = re.sub(r"^§\d+\.\s*", "", heading)
            # Strip remaining markdown
            heading = re.sub(r"\*\*\*(.+?)\*\*\*", r"\1", heading)
            heading = re.sub(r"\*\*(.+?)\*\*", r"\1", heading)
            heading = re.sub(r"\*(.+?)\*", r"\1", heading)
            if heading:
                out_lines.append("")
                out_lines.append(heading + ".")
                out_lines.append("")
            i += 1
            continue

        # --- Horizontal rules ---
        if re.match(r"^\s*---+\s*$", line):
            out_lines.append("")
            i += 1
            continue

        # --- [FIGURE: ...] references ---
        if re.match(r"^\s*\[FIGURE:", line):
            out_lines.append("See figure in print edition.")
            i += 1
            continue

        # --- Blockquotes (Bible epigraphs): > *text* or > text ---
        if line.startswith(">"):
            # Strip the leading > and optional whitespace
            bq = re.sub(r"^>\s*", "", line)
            # Strip surrounding italic markers
            bq = re.sub(r"^\*(.+)\*$", r"\1", bq.strip())
            # Strip inline bold/italic
            bq = re.sub(r"\*\*\*(.+?)\*\*\*", r"\1", bq)
            bq = re.sub(r"\*\*(.+?)\*\*", r"\1", bq)
            bq = re.sub(r"\*(.+?)\*", r"\1", bq)
            bq = bq.strip()
            if bq:
                out_lines.append(bq)
            i += 1
            continue

        # --- Inline formatting ---
        # LaTeX (shouldn't exist but handle defensively)
        line = re.sub(r"\$[^$\n]+\$", "[Equation]", line)
        # Bold+italic
        line = re.sub(r"\*\*\*(.+?)\*\*\*", r"\1", line)
        # Bold
        line = re.sub(r"\*\*(.+?)\*\*", r"\1", line)
        # Italic
        line = re.sub(r"\*(.+?)\*", r"\1", line)
        # Inline code
        line = re.sub(r"`(.+?)`", r"\1", line)
        # Markdown links [text](url)
        line = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", line)
        # Inline [FIGURE:] on same line as other text
        line = re.sub(r"\[FIGURE:[^\]]*\]", "See figure in print edition.", line)

        out_lines.append(line)
        i += 1

    body = "\n".join(out_lines)
    body = re.sub(r"\n{3,}", "\n\n", body).strip()

    return title, body


def process_file(filename: str) -> dict:
    """Read a manuscript file and return cleaned chapter data."""
    fpath = MANUSCRIPT / filename
    if not fpath.exists():
        raise FileNotFoundError(f"Missing: {fpath}")

    raw = fpath.read_text(encoding="utf-8")
    title, body = clean_markdown(raw)

    if not title:
        # Fallback: use filename without extension
        title = fpath.stem

    # Derive a short key for output file naming
    stem = fpath.stem  # e.g. "Ch01" or "AppA_Family_Discussion_Guide"
    # Normalize appendix names to short form
    if stem.startswith("App"):
        short_stem = stem.split("_")[0]  # AppA, AppB, etc.
    else:
        short_stem = stem[:4]  # Ch01, Ch02, etc.

    clean_file = CHAPTERS_DIR / f"{short_stem}_clean.txt"
    clean_file.write_text(body, encoding="utf-8")

    word_count = len(body.split())
    char_count = len(body)

    return {
        "key": short_stem,
        "title": title,
        "source_file": str(fpath),
        "clean_file": str(clean_file),
        "word_count": word_count,
        "char_count": char_count,
    }


def main():
    print("=== Book 2: The Creator's Blueprint — Preprocessing ===\n")

    chapters = []
    missing = []
    for fname in ALL_FILES:
        fpath = MANUSCRIPT / fname
        if not fpath.exists():
            missing.append(fname)
        else:
            print(f"  Found: {fname}")

    if missing:
        print(f"\nMISSING FILES: {missing}")
        raise SystemExit(1)

    print()

    all_text_parts = []
    metadata = []

    for fname in ALL_FILES:
        info = process_file(fname)
        metadata.append(info)
        all_text_parts.append(f"{info['title']}\n\n{open(info['clean_file'], encoding='utf-8').read()}")
        print(f"  {info['key']}: {info['title']!r}  ({info['word_count']:,} words)")

    # Write combined TTS-ready file
    combined = "\n\n\n".join(all_text_parts)
    tts_file = OUTPUT_DIR / "book2_tts_ready.txt"
    tts_file.write_text(combined, encoding="utf-8")

    # Write metadata index
    meta_file = OUTPUT_DIR / "chapter_titles_book2.json"
    meta_file.write_text(json.dumps(metadata, indent=2, ensure_ascii=False), encoding="utf-8")

    total_words = sum(m["word_count"] for m in metadata)
    print(f"\nTotal: {len(metadata)} sections, {total_words:,} words")
    print(f"Output: {tts_file}")
    print(f"Metadata: {meta_file}")
    print(f"Per-chapter files: {CHAPTERS_DIR}/")
    print("\nPreprocessing complete.")


if __name__ == "__main__":
    main()
