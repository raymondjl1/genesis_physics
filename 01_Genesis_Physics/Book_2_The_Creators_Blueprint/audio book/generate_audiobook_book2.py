"""
generate_audiobook_book2.py — TTS generation + M4B packaging for Book 2

Reads chapter_titles_book2.json, generates per-chapter MP3 via edge-tts,
then packages everything as a single M4B with embedded chapter markers.

Output: 00_Audio/Book2_The_Creators_Blueprint.m4b
"""

import asyncio
import json
import os
import subprocess
import sys
from pathlib import Path

import edge_tts

BASE = Path(__file__).parent
CHAPTERS_DIR = BASE / "chapters"
CHAPTERS_DIR.mkdir(parents=True, exist_ok=True)

META_FILE = BASE / "chapter_titles_book2.json"
OUTPUT_M4B = BASE / "Book2_The_Creators_Blueprint.m4b"
CONCAT_MP3 = BASE / "book2_concat.mp3"
CONCAT_LIST = BASE / "book2_concat_list.txt"
FFMETA_FILE = BASE / "book2_ffmetadata.txt"

VOICE = "en-US-AndrewNeural"
BOOK_TITLE = "Genesis Physics: The Creator's Blueprint"
BOOK_AUTHOR = "Jeff Raymond"

# Hardcoded ffmpeg path — winget install does not update PATH in current shell
FFMPEG = (
    r"C:\Users\JeffRaymond\AppData\Local\Microsoft\WinGet\Packages"
    r"\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe"
    r"\ffmpeg-8.1-full_build\bin\ffmpeg.exe"
)
FFPROBE = FFMPEG.replace("ffmpeg.exe", "ffprobe.exe")


def find_ffmpeg():
    """Return working ffmpeg path or raise."""
    if Path(FFMPEG).exists():
        return FFMPEG
    # Try PATH as fallback
    try:
        subprocess.run(["ffmpeg", "-version"], capture_output=True, check=True)
        return "ffmpeg"
    except Exception:
        pass
    raise RuntimeError(
        f"ffmpeg not found. Expected: {FFMPEG}\n"
        "Run: winget install Gyan.FFmpeg"
    )


def get_duration_ms(mp3_path: Path) -> int:
    """Return audio duration in milliseconds using ffprobe."""
    result = subprocess.run(
        [
            FFPROBE, "-v", "quiet",
            "-print_format", "json",
            "-show_streams",
            str(mp3_path),
        ],
        capture_output=True, text=True, check=True,
    )
    data = json.loads(result.stdout)
    for stream in data.get("streams", []):
        if stream.get("codec_type") == "audio":
            return int(float(stream["duration"]) * 1000)
    raise ValueError(f"No audio stream in {mp3_path}")


async def generate_mp3(text: str, mp3_path: Path):
    """Generate TTS MP3 for one chapter (cached if exists)."""
    if mp3_path.exists() and mp3_path.stat().st_size > 10_000:
        print(f"    Cached: {mp3_path.name}")
        return
    print(f"    Generating: {mp3_path.name} ({len(text):,} chars)...")
    communicate = edge_tts.Communicate(text, VOICE)
    await communicate.save(str(mp3_path))
    size_mb = mp3_path.stat().st_size / 1_048_576
    print(f"    Done: {mp3_path.name} ({size_mb:.1f} MB)")


async def generate_all_mp3s(chapters: list) -> list:
    """Generate TTS for each chapter sequentially. Returns list of MP3 paths."""
    mp3_paths = []
    for idx, ch in enumerate(chapters, 1):
        key = ch["key"]
        clean_file = Path(ch["clean_file"])
        text = f"{ch['title']}.\n\n" + clean_file.read_text(encoding="utf-8")
        mp3_path = CHAPTERS_DIR / f"{key}.mp3"
        print(f"  [{idx}/{len(chapters)}] {key}: {ch['title']}")
        await generate_mp3(text, mp3_path)
        mp3_paths.append(mp3_path)
    return mp3_paths


def build_concat_and_meta(chapters: list, mp3_paths: list):
    """Build ffmpeg concat list and FFMETADATA chapter markers."""
    ffmpeg = find_ffmpeg()

    # Get durations
    print("\nMeasuring chapter durations...")
    durations_ms = []
    for mp3_path in mp3_paths:
        d = get_duration_ms(mp3_path)
        durations_ms.append(d)
        minutes = d // 60000
        seconds = (d % 60000) / 1000
        print(f"  {mp3_path.name}: {minutes}m {seconds:.0f}s")

    # Write concat list
    with open(CONCAT_LIST, "w", encoding="utf-8") as f:
        for mp3_path in mp3_paths:
            f.write(f"file '{mp3_path.resolve()}'\n")

    # Build FFMETADATA
    lines = [
        ";FFMETADATA1",
        f"title={BOOK_TITLE}",
        f"artist={BOOK_AUTHOR}",
        f"album={BOOK_TITLE}",
        f"genre=Audiobook",
        "",
    ]
    cursor_ms = 0
    for ch, dur_ms in zip(chapters, durations_ms):
        start = cursor_ms
        end = cursor_ms + dur_ms
        lines += [
            "[CHAPTER]",
            "TIMEBASE=1/1000",
            f"START={start}",
            f"END={end}",
            f"title={ch['title']}",
            "",
        ]
        cursor_ms = end

    FFMETA_FILE.write_text("\n".join(lines), encoding="utf-8")

    total_ms = sum(durations_ms)
    total_min = total_ms // 60000
    total_sec = (total_ms % 60000) / 1000
    print(f"\nTotal runtime: {total_min}m {total_sec:.0f}s ({total_min/60:.2f} hours)")

    return ffmpeg


def concatenate_and_package(ffmpeg: str):
    """Concatenate MP3s and package as M4B with chapter markers."""
    print("\nConcatenating chapter MP3s...")
    subprocess.run(
        [
            ffmpeg, "-y",
            "-f", "concat", "-safe", "0",
            "-i", str(CONCAT_LIST),
            "-c", "copy",
            str(CONCAT_MP3),
        ],
        check=True,
    )
    size_mb = CONCAT_MP3.stat().st_size / 1_048_576
    print(f"Concatenated: {CONCAT_MP3.name} ({size_mb:.1f} MB)")

    print("\nPackaging M4B audiobook...")
    subprocess.run(
        [
            ffmpeg, "-y",
            "-i", str(CONCAT_MP3),
            "-i", str(FFMETA_FILE),
            "-map_metadata", "1",
            "-map", "0:a",
            "-c:a", "aac",
            "-b:a", "64k",
            str(OUTPUT_M4B),
        ],
        check=True,
    )
    size_mb = OUTPUT_M4B.stat().st_size / 1_048_576
    print(f"\nOutput: {OUTPUT_M4B}")
    print(f"Size: {size_mb:.1f} MB")


async def main():
    print("=== Book 2: The Creator's Blueprint — Audiobook Generation ===\n")

    if not META_FILE.exists():
        print(f"ERROR: {META_FILE} not found. Run preprocess_book2.py first.")
        sys.exit(1)

    chapters = json.loads(META_FILE.read_text(encoding="utf-8"))
    print(f"Loaded {len(chapters)} chapters/sections from metadata.\n")

    # Step 1: Generate TTS MP3s
    print("Step 1: Generating TTS audio (en-US-AndrewNeural)...")
    mp3_paths = await generate_all_mp3s(chapters)

    # Step 2: Build chapter markers and concat list
    print("\nStep 2: Building chapter markers...")
    ffmpeg = build_concat_and_meta(chapters, mp3_paths)

    # Step 3: Concatenate and package
    print("\nStep 3: Packaging M4B...")
    concatenate_and_package(ffmpeg)

    # Cleanup concat MP3 (intermediate)
    if CONCAT_MP3.exists():
        CONCAT_MP3.unlink()
        print("Cleaned up intermediate concat MP3.")

    print("\n=== COMPLETE ===")
    print(f"Audiobook: {OUTPUT_M4B}")
    final_size = OUTPUT_M4B.stat().st_size / 1_048_576
    print(f"Size: {final_size:.1f} MB")
    print(
        "\nTransfer to Samsung Galaxy S25:"
        "\n  Option A (USB): Connect phone, copy M4B to phone storage, open in Voice - Offline Audiobook Player."
        "\n  Option B (OneDrive): The file is already in OneDrive — open the OneDrive app on your phone, download it, then open in Voice player."
        "\n  Player: 'Voice - Offline Audiobook Player' (free, Google Play Store)"
    )


if __name__ == "__main__":
    asyncio.run(main())
