#!/usr/bin/env python3
"""
preprocess_book1.py
Preprocessing pipeline for Genesis Physics Book 1 — The Hidden Architecture.
Reads Ch01.md–Ch15.md, strips markdown, and writes TTS-ready text files.

Output:
  00_Audio/chapters/ChXX_clean.txt  — per-chapter TTS-ready text
  00_Audio/book1_tts_ready.txt      — single concatenated file
  00_Audio/chapter_titles.json      — chapter metadata for generation script
"""

import re
import json
from pathlib import Path

BOOK_DIR = Path(r"c:\Users\JeffRaymond\OneDrive - OKSI\Documents\Claude Desktop\Exodus Protocol\01_Genesis_Physics\Book_1_Hidden_Architecture\Manuscript")
OUTPUT_DIR = Path(r"c:\Users\JeffRaymond\OneDrive - OKSI\Documents\Claude Desktop\Exodus Protocol\01_Genesis_Physics\Book_1_Hidden_Architecture\audio book")
CHAPTERS_DIR = OUTPUT_DIR / "chapters"


def clean_markdown(text: str) -> tuple[str, str]:
    """
    Strip markdown formatting from chapter text.
    Returns (title, clean_body_text).
    Title combines H1 + first H2 subtitle when H1 is bare ("Chapter N").
    """
    lines = text.split('\n')
    title = ""
    first_h2 = ""
    out_lines = []

    for line in lines:
        # Chapter title (# heading) — capture and skip (spoken as announcement)
        m = re.match(r'^#\s+(.+)', line)
        if m:
            if not title:
                title = m.group(1).strip()
            continue

        # Section headings (## and ###) — keep as spoken sentences
        m = re.match(r'^#{2,}\s*(.+)', line)
        if m:
            heading = m.group(1).strip()
            heading = re.sub(r'^§\d+\.\s*', '', heading)  # strip §N. prefix
            # Capture first H2 as subtitle for bare chapter titles ("Chapter N")
            if not first_h2 and re.match(r'^#{2}\s', line):
                first_h2 = heading
            if heading:
                out_lines.append('')
                out_lines.append(heading + '.')
                out_lines.append('')
            continue

        # Horizontal rules → paragraph pause (blank line)
        if re.match(r'^\s*---+\s*$', line):
            out_lines.append('')
            continue

        # Figure captions → skip (meaningless in audio)
        if re.match(r'^\s*\[FIGURE:', line):
            continue

        # Strip bold, italic, bold-italic
        line = re.sub(r'\*\*\*(.+?)\*\*\*', r'\1', line)
        line = re.sub(r'\*\*(.+?)\*\*', r'\1', line)
        line = re.sub(r'\*(.+?)\*', r'\1', line)
        line = re.sub(r'_(.+?)_', r'\1', line)

        # Inline code → bare text
        line = re.sub(r'`(.+?)`', r'\1', line)

        # LaTeX inline math → spoken placeholder
        line = re.sub(r'\$[^$\n]+\$', 'the equation', line)

        # Markdown links → just the link text
        line = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', line)

        out_lines.append(line)

    body = '\n'.join(out_lines)
    body = re.sub(r'\n{3,}', '\n\n', body)  # collapse excess blank lines
    body = body.strip()
    # If title is bare "Chapter N" with no subtitle, combine with first H2
    if re.fullmatch(r'Chapter \d+', title) and first_h2:
        title = f"{title} — {first_h2}"

    return title, body


def main():
    CHAPTERS_DIR.mkdir(parents=True, exist_ok=True)

    # Glob chapter files, exclude SPEC and REVIEW files
    chapter_files = sorted(
        f for f in BOOK_DIR.glob('Ch[0-9]*.md')
        if not re.search(r'(SPEC|REVIEW)', f.name, re.IGNORECASE)
    )

    if not chapter_files:
        print(f"ERROR: No chapter files found in {BOOK_DIR}")
        return

    print(f"Found {len(chapter_files)} chapters\n")

    chapter_meta = []
    combined_parts = []

    for i, ch_file in enumerate(chapter_files, 1):
        text = ch_file.read_text(encoding='utf-8')
        title, body = clean_markdown(text)
        if not title:
            title = f"Chapter {i}"

        # Full TTS text: chapter announcement + body
        tts_text = f"Chapter {i}. {title}.\n\n{body}"

        clean_path = CHAPTERS_DIR / f"Ch{i:02d}_clean.txt"
        clean_path.write_text(tts_text, encoding='utf-8')

        word_count = len(body.split())
        char_count = len(tts_text)
        print(f"  Ch{i:02d}: '{title}' — {word_count:,} words, {char_count:,} chars")

        chapter_meta.append({
            'num': i,
            'title': title,
            'source_file': ch_file.name,
            'clean_file': clean_path.name,
            'word_count': word_count,
            'char_count': char_count,
        })
        combined_parts.append(tts_text)

    # Combined TTS-ready file (one section per chapter)
    combined_path = OUTPUT_DIR / "book1_tts_ready.txt"
    combined_path.write_text('\n\n\n'.join(combined_parts), encoding='utf-8')

    # Chapter metadata for downstream scripts
    meta_path = OUTPUT_DIR / "chapter_titles.json"
    meta_path.write_text(json.dumps(chapter_meta, indent=2), encoding='utf-8')

    total_words = sum(c['word_count'] for c in chapter_meta)
    est_minutes = total_words / 130  # ~130 wpm spoken
    print(f"\nTotal: {total_words:,} words across {len(chapter_meta)} chapters")
    print(f"Estimated runtime: ~{est_minutes:.0f} min ({est_minutes/60:.1f} hours)")
    print(f"\nOutputs:")
    print(f"  Combined:  {combined_path}")
    print(f"  Metadata:  {meta_path}")
    print(f"  Per-chap:  {CHAPTERS_DIR}/ChXX_clean.txt")


if __name__ == '__main__':
    main()
