"""
preprocess_book0.py — Markdown → TTS-ready plain text for Book 0 (all 6 volumes)

Discovers chapter and back-matter files for each volume, strips markdown and
LaTeX, and writes per-volume clean text + metadata JSON.

Run once before generate_audiobook_book0.py.
"""

import re
import json
import os
from pathlib import Path

BASE = Path(__file__).parent  # Book_0_The_Foundations/

# ---------------------------------------------------------------------------
# LaTeX → spoken-text conversion
# ---------------------------------------------------------------------------

GREEK_MAP = {
    r'\alpha': 'alpha', r'\beta': 'beta', r'\gamma': 'gamma',
    r'\delta': 'delta', r'\epsilon': 'epsilon', r'\varepsilon': 'epsilon',
    r'\zeta': 'zeta', r'\eta': 'eta', r'\theta': 'theta', r'\vartheta': 'theta',
    r'\iota': 'iota', r'\kappa': 'kappa', r'\lambda': 'lambda', r'\mu': 'mu',
    r'\nu': 'nu', r'\xi': 'xi', r'\pi': 'pi', r'\varpi': 'pi',
    r'\rho': 'rho', r'\varrho': 'rho', r'\sigma': 'sigma', r'\varsigma': 'sigma',
    r'\tau': 'tau', r'\upsilon': 'upsilon', r'\phi': 'phi', r'\varphi': 'phi',
    r'\chi': 'chi', r'\psi': 'psi', r'\omega': 'omega',
    r'\Gamma': 'Gamma', r'\Delta': 'Delta', r'\Theta': 'Theta',
    r'\Lambda': 'Lambda', r'\Xi': 'Xi', r'\Pi': 'Pi', r'\Sigma': 'Sigma',
    r'\Upsilon': 'Upsilon', r'\Phi': 'Phi', r'\Psi': 'Psi', r'\Omega': 'Omega',
    r'\partial': 'partial', r'\nabla': 'nabla', r'\infty': 'infinity',
    r'\hbar': 'h-bar', r'\ell': 'ell', r'\aleph': 'aleph',
    r'\cdot': 'times', r'\times': 'times', r'\div': 'divided by',
    r'\pm': 'plus or minus', r'\mp': 'minus or plus',
    r'\leq': 'less than or equal to', r'\geq': 'greater than or equal to',
    r'\neq': 'not equal to', r'\approx': 'approximately equal to',
    r'\propto': 'proportional to', r'\sim': 'approximately',
    r'\ll': 'much less than', r'\gg': 'much greater than',
    r'\rightarrow': 'approaches', r'\to': 'to', r'\leftarrow': 'from',
    r'\Rightarrow': 'implies', r'\Leftrightarrow': 'if and only if',
    r'\sqrt': 'square root of', r'\int': 'integral',
    r'\sum': 'sum', r'\prod': 'product',
    r'\langle': '', r'\rangle': '',
    r'\{': '', r'\}': '',
    r'\,': ' ', r'\;': ' ', r'\:': ' ', r'\ ': ' ',
    r'\!': '',
}


def latex_to_speech(expr: str) -> str:
    """Convert a LaTeX expression to a spoken approximation."""
    expr = expr.strip()

    # Empty
    if not expr:
        return ''

    # Replace Greek and named symbols
    for latex, english in GREEK_MAP.items():
        expr = expr.replace(latex, f' {english} ')

    # Superscripts: ^{...} → to the power of ...
    expr = re.sub(r'\^\{([^}]+)\}', r' to the \1', expr)
    expr = re.sub(r'\^(\w)', r' to the \1', expr)

    # Subscripts: _{...} → subscript ...
    expr = re.sub(r'_\{([^}]+)\}', r' sub \1', expr)
    expr = re.sub(r'_(\w)', r' sub \1', expr)

    # Fractions: \frac{a}{b} → a over b
    expr = re.sub(r'\\frac\{([^}]+)\}\{([^}]+)\}', r'\1 over \2', expr)

    # Remove remaining LaTeX commands
    expr = re.sub(r'\\[a-zA-Z]+\s*', ' ', expr)

    # Remove braces
    expr = expr.replace('{', '').replace('}', '')

    # Clean up whitespace
    expr = re.sub(r'\s+', ' ', expr).strip()

    # If the result is very short (single letter or number), return it directly
    if re.fullmatch(r'[A-Za-z0-9\s\+\-\*/=<>.,_]+', expr) and len(expr) < 60:
        return expr

    # Fallback for complex expressions
    if len(expr) > 60 or re.search(r'[\\{}^_]', expr):
        return 'the expression'

    return expr


def convert_inline_math(match) -> str:
    """Handle $...$ inline math."""
    inner = match.group(1).strip()
    return latex_to_speech(inner)


def convert_display_math(match) -> str:
    """Handle $$...$$ or \[...\] display math — drop it from TTS."""
    return '\n\n[Equation — see print edition.]\n\n'


# ---------------------------------------------------------------------------
# Markdown cleaning
# ---------------------------------------------------------------------------

def table_to_prose(table_lines: list) -> str:
    """Convert a markdown pipe table to spoken prose."""
    rows = []
    for line in table_lines:
        line = line.strip()
        if not line.startswith('|'):
            continue
        if re.match(r'^[|\s\-:]+$', line):
            continue
        cells = [c.strip() for c in line.strip('|').split('|')]
        rows.append(cells)

    if not rows:
        return ''

    headers = rows[0]
    data_rows = rows[1:]

    if not data_rows:
        return 'Table: ' + ', '.join(headers) + '.'

    sentences = []
    for row in data_rows:
        if len(row) < len(headers):
            row = row + [''] * (len(headers) - len(row))
        row_dict = {headers[i]: row[i] for i in range(len(headers))}
        parts = [f'{k}: {v}.' for k, v in row_dict.items() if v.strip()]
        if parts:
            sentences.append(' '.join(parts))

    return '\n'.join(sentences)


def strip_inline_formatting(line: str) -> str:
    """Strip bold, italic, code, links from a line."""
    line = re.sub(r'\*\*\*(.+?)\*\*\*', r'\1', line)
    line = re.sub(r'\*\*(.+?)\*\*', r'\1', line)
    line = re.sub(r'\*(.+?)\*', r'\1', line)
    line = re.sub(r'_(.+?)_', r'\1', line)
    line = re.sub(r'`(.+?)`', r'\1', line)
    line = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', line)
    return line


def clean_markdown(raw_text: str) -> tuple[str, str]:
    """Returns (chapter_title, cleaned_body_for_tts)."""

    # Pre-process: handle display math blocks ($$...$$, \[...\])
    # Multi-line $$...$$ blocks
    raw_text = re.sub(r'\$\$[\s\S]*?\$\$', '\n\n[Equation — see print edition.]\n\n', raw_text)
    # \[...\] display math
    raw_text = re.sub(r'\\\[[\s\S]*?\\\]', '\n\n[Equation — see print edition.]\n\n', raw_text)
    # \begin{...}...\end{...} environments
    raw_text = re.sub(r'\\begin\{[^}]+\}[\s\S]*?\\end\{[^}]+\}',
                      '\n\n[Equation — see print edition.]\n\n', raw_text)

    # Inline math $...$
    raw_text = re.sub(r'\$([^$\n]+)\$', convert_inline_math, raw_text)

    lines = raw_text.split('\n')
    title = ''
    out_lines = []
    i = 0

    while i < len(lines):
        line = lines[i]

        # Table detection
        if line.strip().startswith('|'):
            table_block = []
            while i < len(lines) and lines[i].strip().startswith('|'):
                table_block.append(lines[i])
                i += 1
            prose = table_to_prose(table_block)
            if prose:
                out_lines.append('')
                out_lines.append(prose)
                out_lines.append('')
            continue

        # H1 — chapter title
        m = re.match(r'^#\s+(.+)', line)
        if m:
            raw_title = strip_inline_formatting(m.group(1).strip())
            if not title:
                title = raw_title
            i += 1
            continue

        # H2–H6 — section headings
        m = re.match(r'^#{2,}\s*(.+)', line)
        if m:
            heading = strip_inline_formatting(m.group(1).strip())
            # Strip §N. and N.N prefixes
            heading = re.sub(r'^§[\d.]+\s*', '', heading)
            heading = re.sub(r'^\d+\.\d+[\d.]*\s+', '', heading)
            if heading:
                out_lines.append('')
                out_lines.append(heading + '.')
                out_lines.append('')
            i += 1
            continue

        # Horizontal rules
        if re.match(r'^\s*---+\s*$', line):
            out_lines.append('')
            i += 1
            continue

        # [FIGURE: ...] references
        if re.match(r'^\s*\[FIGURE:', line):
            out_lines.append('[Figure — see print edition.]')
            i += 1
            continue

        # Blockquotes
        if line.startswith('>'):
            bq = re.sub(r'^>\s*', '', line)
            bq = re.sub(r'^\*(.+)\*$', r'\1', bq.strip())
            bq = strip_inline_formatting(bq).strip()
            if bq:
                out_lines.append(bq)
            i += 1
            continue

        # Inline [FIGURE:...] on same line
        line = re.sub(r'\[FIGURE:[^\]]*\]', '[Figure — see print edition.]', line)

        # Strip remaining inline formatting
        line = strip_inline_formatting(line)

        out_lines.append(line)
        i += 1

    body = '\n'.join(out_lines)
    body = re.sub(r'\n{3,}', '\n\n', body).strip()

    return title, body


# ---------------------------------------------------------------------------
# File discovery
# ---------------------------------------------------------------------------

EXCLUDE_SUFFIXES = [
    '_OUTLINE', 'OUTLINE.md',
    '_BRIEF', '_REPORT', '_FINALIZATION', '_ATTACK_PLAN', '_SOLUTIONS',
    '_Part1', '_Part2', '_Part3',
    'SOURCE_MAP', 'Master_Index', 'MASTER_INDEX', 'PROBLEM_SETS_SUMMARY',
    'CHAPTER_PROMPTS', 'WRITING_PROMPT', 'QUALITY_GATE', 'CLAUDE.md',
    'README', 'STATUS', 'BIBLIOGRAPHY.md', 'Problem_Sets.md',
    'BOOK_SPEC', 'BACKMATTER_SPEC', 'APPENDIX_PROMPTS',
    'CHAPTER_SPEC', 'Back_Matter_', 'BACK_MATTER_SPEC', 'BACK_MATTER_',
]

def should_exclude(path: Path) -> bool:
    name = path.name
    for suffix in EXCLUDE_SUFFIXES:
        if suffix in name:
            return True
    return False


def pick_best_file(chapter_dir: Path) -> Path | None:
    """Pick FINAL > DRAFT from a chapter directory, skipping excluded files."""
    candidates = [f for f in chapter_dir.glob('*.md') if not should_exclude(f)]

    # Prefer FINAL
    finals = [f for f in candidates if '_FINAL' in f.name]
    if finals:
        return sorted(finals)[0]

    # Fall back to DRAFT
    drafts = [f for f in candidates if '_DRAFT' in f.name]
    if drafts:
        return sorted(drafts)[0]

    # Last resort: any .md that isn't excluded
    remaining = [f for f in candidates
                 if not any(x in f.name for x in ['OUTLINE', 'BRIEF', 'REPORT'])]
    if remaining:
        return sorted(remaining)[0]

    return None


def _chapter_sort_key(d: Path) -> int:
    """Extract chapter number from directory name for correct numeric ordering."""
    m = re.search(r'Ch[_]?(\d+)', d.name)
    return int(m.group(1)) if m else 999


def discover_chapters(vol_dir: Path) -> list[dict]:
    """Return ordered list of {key, title_hint, file_path} for all chapters."""
    chapter_dirs = sorted(
        [d for d in vol_dir.iterdir() if d.is_dir() and re.match(r'Ch[\d_]', d.name)],
        key=_chapter_sort_key,
    )
    sections = []
    for chdir in chapter_dirs:
        fpath = pick_best_file(chdir)
        if fpath is None:
            print(f"  WARNING: No content file found in {chdir.name} — skipping")
            continue
        # Extract chapter number for key
        m = re.match(r'Ch[_]?(\d+)', chdir.name)
        num = m.group(1) if m else chdir.name
        sections.append({'key': f'Ch{num}', 'file_path': fpath})
    return sections


def discover_back_matter(vol_dir: Path, back_matter_dir: str,
                         include_patterns: list[str] | None = None) -> list[dict]:
    """Return ordered list of back-matter files."""
    bm_dir = vol_dir / back_matter_dir
    if not bm_dir.exists():
        return []

    files = sorted([f for f in bm_dir.glob('*.md') if not should_exclude(f)])

    if include_patterns:
        files = [f for f in files
                 if any(p in f.name for p in include_patterns)]

    return [{'key': f.stem[:30], 'file_path': f} for f in files]


# ---------------------------------------------------------------------------
# Volume configuration
# ---------------------------------------------------------------------------

VOLUMES = [
    {
        'num': 1, 'key': 'Vol1',
        'folder': 'Vol_1_Architecture_of_Reality',
        'title': 'Genesis Physics: The Foundations, Volume 1 — Architecture of Reality',
        'author': 'Jeff Raymond',
        'back_matter_dir': 'Manuscript',
        'back_matter_patterns': ['AppA_', 'AppB_', 'AppC_', 'Bibliography_',
                                 'ProblemSets_Ch01', 'ProblemSets_Ch03',
                                 'ProblemSets_Ch05', 'ProblemSets_Ch07'],
    },
    {
        'num': 2, 'key': 'Vol2',
        'folder': 'Vol_2_Forces_and_Fields',
        'title': 'Genesis Physics: The Foundations, Volume 2 — Forces and Fields',
        'author': 'Jeff Raymond',
        'back_matter_dir': 'Back_Matter',
        'back_matter_patterns': None,
    },
    {
        'num': 3, 'key': 'Vol3',
        'folder': 'Vol_3_Matter_and_Motion',
        'title': 'Genesis Physics: The Foundations, Volume 3 — Matter and Motion',
        'author': 'Jeff Raymond',
        'back_matter_dir': 'Back_Matter',
        'back_matter_patterns': None,
    },
    {
        'num': 4, 'key': 'Vol4',
        'folder': 'Vol_4_The_Quantum_World',
        'title': 'Genesis Physics: The Foundations, Volume 4 — The Quantum World',
        'author': 'Jeff Raymond',
        'back_matter_dir': 'Back_Matter',
        'back_matter_patterns': None,
    },
    {
        'num': 5, 'key': 'Vol5',
        'folder': 'Vol_5_The_Cosmos',
        'title': 'Genesis Physics: The Foundations, Volume 5 — The Cosmos',
        'author': 'Jeff Raymond',
        'back_matter_dir': 'Back_Matter',
        'back_matter_patterns': None,
    },
    {
        'num': 6, 'key': 'Vol6',
        'folder': 'Vol_6_Predictions_and_Simulations',
        'title': 'Genesis Physics: The Foundations, Volume 6 — Predictions and Simulations',
        'author': 'Jeff Raymond',
        'back_matter_dir': 'Back_Matter',
        'back_matter_patterns': ['APPENDIX_A', 'APPENDIX_B', 'APPENDIX_D',
                                 'APPENDIX_E', 'APPENDIX_F', 'Bibliography'],
    },
]


# ---------------------------------------------------------------------------
# Process a single file
# ---------------------------------------------------------------------------

def process_file(fpath: Path, key: str, out_dir: Path) -> dict:
    raw = fpath.read_text(encoding='utf-8', errors='replace')
    title, body = clean_markdown(raw)

    if not title:
        # Derive title from directory or filename
        parent = fpath.parent.name
        # "Ch_01_Axioms_and_Definitions" → "Axioms and Definitions"
        m = re.match(r'Ch[_\d]+_(.*)', parent)
        if m:
            title = m.group(1).replace('_', ' ')
        else:
            title = fpath.stem.replace('_', ' ')

    clean_file = out_dir / f'{key}_clean.txt'
    clean_file.write_text(body, encoding='utf-8')

    return {
        'key': key,
        'title': title,
        'source_file': str(fpath),
        'clean_file': str(clean_file),
        'word_count': len(body.split()),
        'char_count': len(body),
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def preprocess_volume(vol_cfg: dict) -> list[dict]:
    vol_dir = BASE / vol_cfg['folder']
    audio_dir = vol_dir / 'audio book'
    chapters_dir = audio_dir / 'chapters'
    chapters_dir.mkdir(parents=True, exist_ok=True)

    print(f"\n{'='*60}")
    print(f"  {vol_cfg['title']}")
    print(f"{'='*60}")

    sections = discover_chapters(vol_dir)
    back_matter = discover_back_matter(
        vol_dir, vol_cfg['back_matter_dir'],
        vol_cfg.get('back_matter_patterns'))

    all_sections = sections + back_matter

    if not all_sections:
        print(f"  WARNING: No content found for {vol_cfg['key']}")
        return []

    metadata = []
    for sec in all_sections:
        info = process_file(sec['file_path'], sec['key'], chapters_dir)
        metadata.append(info)
        print(f"  {info['key']}: {info['title']!r}  ({info['word_count']:,} words)")

    # Write per-volume metadata
    meta_file = audio_dir / f'chapter_titles_{vol_cfg["key"]}.json'
    meta_data_with_vol = {
        'volume': vol_cfg,
        'chapters': metadata,
    }
    meta_file.write_text(json.dumps(meta_data_with_vol, indent=2, ensure_ascii=False),
                         encoding='utf-8')

    total_words = sum(m['word_count'] for m in metadata)
    print(f"\n  Total: {len(metadata)} sections, {total_words:,} words")
    print(f"  Metadata: {meta_file}")

    return metadata


def main():
    print("=== Book 0: The Foundations — Preprocessing All 6 Volumes ===")

    for vol_cfg in VOLUMES:
        preprocess_volume(vol_cfg)

    print("\n=== Preprocessing complete for all 6 volumes ===")


if __name__ == '__main__':
    main()
