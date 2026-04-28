#!/usr/bin/env python3
"""
generate_audiobook_book1.py
Generates Book 1 M4B audiobook from preprocessed chapter text files.
Run preprocess_book1.py first.

Pipeline:
  1. TTS each chapter via edge-tts (en-US-AndrewNeural)
  2. Measure chapter durations with ffprobe
  3. Write FFMETADATA chapter markers
  4. Concatenate MP3s and package as M4B via ffmpeg
"""

import asyncio
import json
import subprocess
import sys
from pathlib import Path

OUTPUT_DIR = Path(r"c:\Users\JeffRaymond\OneDrive - OKSI\Documents\Claude Desktop\Exodus Protocol\01_Genesis_Physics\Book_1_Hidden_Architecture\audio book")
CHAPTERS_DIR = OUTPUT_DIR / "chapters"
VOICE = "en-US-AndrewNeural"
TITLE = "Genesis Physics: The Hidden Architecture"
AUTHOR = "Jeff Raymond"
OUTPUT_M4B = OUTPUT_DIR / "Book1_Hidden_Architecture.m4b"

# ffmpeg/ffprobe — full path from winget install (PATH not yet updated in this shell)
_FFMPEG_BASE = (
    r"C:\Users\JeffRaymond\AppData\Local\Microsoft\WinGet\Packages"
    r"\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe"
    r"\ffmpeg-8.1-full_build\bin"
)
FFMPEG = str(Path(_FFMPEG_BASE) / "ffmpeg.exe")
FFPROBE = str(Path(_FFMPEG_BASE) / "ffprobe.exe")


async def generate_chapter_tts(num: int, title: str, text: str) -> Path:
    """Generate TTS MP3 for one chapter; skip if already cached."""
    import edge_tts

    mp3_path = CHAPTERS_DIR / f"Ch{num:02d}.mp3"
    if mp3_path.exists():
        size_kb = mp3_path.stat().st_size // 1024
        print(f"  Ch{num:02d}: cached ({size_kb} KB)")
        return mp3_path

    print(f"  Ch{num:02d}: '{title}' generating...", end='', flush=True)
    communicate = edge_tts.Communicate(text, VOICE)
    await communicate.save(str(mp3_path))
    size_kb = mp3_path.stat().st_size // 1024
    print(f" done ({size_kb} KB)")
    return mp3_path


def get_duration_ms(mp3_path: Path) -> int:
    """Return audio duration in milliseconds via ffprobe."""
    result = subprocess.run(
        [FFPROBE, '-v', 'quiet', '-print_format', 'json', '-show_streams', str(mp3_path)],
        capture_output=True, text=True, check=True
    )
    data = json.loads(result.stdout)
    for stream in data.get('streams', []):
        if 'duration' in stream:
            return int(float(stream['duration']) * 1000)
    # Fallback: check format level
    result2 = subprocess.run(
        [FFPROBE, '-v', 'quiet', '-print_format', 'json', '-show_format', str(mp3_path)],
        capture_output=True, text=True, check=True
    )
    data2 = json.loads(result2.stdout)
    duration = data2.get('format', {}).get('duration')
    if duration:
        return int(float(duration) * 1000)
    raise RuntimeError(f"Cannot determine duration for {mp3_path}")


async def main():
    meta_path = OUTPUT_DIR / "chapter_titles.json"
    if not meta_path.exists():
        print("ERROR: chapter_titles.json not found.")
        print("Run preprocess_book1.py first.")
        sys.exit(1)

    chapters = json.loads(meta_path.read_text(encoding='utf-8'))
    print(f"Loaded {len(chapters)} chapters\n")

    # ── Step 1: TTS generation ──────────────────────────────────────────────
    print("=== STEP 1: TTS Generation ===")
    for ch in chapters:
        clean_file = CHAPTERS_DIR / ch['clean_file']
        if not clean_file.exists():
            print(f"ERROR: {clean_file} not found. Run preprocess_book1.py first.")
            sys.exit(1)
        text = clean_file.read_text(encoding='utf-8')
        mp3 = await generate_chapter_tts(ch['num'], ch['title'], text)
        ch['mp3_path'] = str(mp3)

    # ── Step 2: Measure durations ───────────────────────────────────────────
    print("\n=== STEP 2: Chapter durations ===")
    cumulative_ms = 0
    for ch in chapters:
        ch['start_ms'] = cumulative_ms
        ch['duration_ms'] = get_duration_ms(Path(ch['mp3_path']))
        cumulative_ms += ch['duration_ms']
        ch['end_ms'] = cumulative_ms
        m, s = divmod(ch['duration_ms'] // 1000, 60)
        print(f"  Ch{ch['num']:02d}: {m}m {s:02d}s")

    total_ms = cumulative_ms
    total_m, total_s = divmod(total_ms // 1000, 60)
    print(f"\n  Total: {total_m}m {total_s:02d}s ({total_m / 60:.1f} h)")

    # ── Step 3: Write concat list ───────────────────────────────────────────
    concat_file = OUTPUT_DIR / "concat_list.txt"
    with open(concat_file, 'w') as f:
        for ch in chapters:
            safe = Path(ch['mp3_path']).as_posix()
            f.write(f"file '{safe}'\n")

    # ── Step 4: Write FFMETADATA ────────────────────────────────────────────
    meta_file = OUTPUT_DIR / "ffmetadata.txt"
    with open(meta_file, 'w', encoding='utf-8') as f:
        f.write(';FFMETADATA1\n')
        f.write(f'title={TITLE}\n')
        f.write(f'artist={AUTHOR}\n')
        f.write(f'album={TITLE}\n')
        f.write('genre=Audiobook\n')
        f.write('comment=Genesis Physics Series — Book 1\n')
        f.write('\n')
        for ch in chapters:
            f.write('[CHAPTER]\n')
            f.write('TIMEBASE=1/1000\n')
            f.write(f'START={ch["start_ms"]}\n')
            f.write(f'END={ch["end_ms"]}\n')
            f.write(f'title={ch["title"]}\n')
            f.write('\n')

    # ── Step 5: Concatenate MP3s ────────────────────────────────────────────
    print("\n=== STEP 3: Concatenating chapters ===")
    concat_mp3 = OUTPUT_DIR / "book1_concat.mp3"
    result = subprocess.run([
        FFMPEG, '-y', '-f', 'concat', '-safe', '0',
        '-i', str(concat_file),
        '-c', 'copy', str(concat_mp3),
    ], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"ERROR:\n{result.stderr[-2000:]}")
        sys.exit(1)
    concat_mb = concat_mp3.stat().st_size / (1024 * 1024)
    print(f"  Concatenated MP3: {concat_mb:.1f} MB")

    # ── Step 6: Package M4B ─────────────────────────────────────────────────
    print("\n=== STEP 4: Packaging M4B ===")
    result = subprocess.run([
        FFMPEG, '-y',
        '-i', str(concat_mp3),
        '-i', str(meta_file),
        '-map_metadata', '1',
        '-map', '0:a',
        '-c:a', 'aac',
        '-b:a', '64k',
        str(OUTPUT_M4B),
    ], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"ERROR:\n{result.stderr[-2000:]}")
        sys.exit(1)

    size_mb = OUTPUT_M4B.stat().st_size / (1024 * 1024)
    print(f"\n{'='*55}")
    print(f"  SUCCESS")
    print(f"  File:     {OUTPUT_M4B}")
    print(f"  Size:     {size_mb:.1f} MB")
    print(f"  Runtime:  {total_m}m {total_s:02d}s  ({total_m / 60:.1f} hours)")
    print(f"  Chapters: {len(chapters)}")
    print(f"  Voice:    {VOICE}")
    print(f"{'='*55}")


if __name__ == '__main__':
    asyncio.run(main())
