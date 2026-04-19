#!/usr/bin/env python3
"""
Generate Genesis Physics and MRG Technical Paper audiobooks using edge-tts.
Uses Microsoft's neural TTS voice (en-US-GuyNeural) for natural narration.

Requirements:
    pip install edge-tts

Usage:
    python generate_audiobooks.py

Optional: Install ffmpeg for best-quality concatenation.
    Without ffmpeg, falls back to binary MP3 concatenation (works fine).

Output:
    Genesis_Physics_Audiobook.mp3   (~9 hours, all 26 chapters + appendices)
    MRG_Technical_Paper_Audiobook.mp3  (~1 hour)
"""

import asyncio
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time

try:
    import edge_tts
except ImportError:
    print("edge-tts not installed. Installing now...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "edge-tts"])
    import edge_tts

# Configuration
VOICE = "en-US-GuyNeural"
RATE = "-5%"  # Slightly slower for audiobook clarity
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


def has_ffmpeg():
    """Check if ffmpeg is available."""
    return shutil.which("ffmpeg") is not None


def chunk_text(text, max_chars=4000):
    """
    Split text into chunks at sentence boundaries.
    edge-tts handles large text but chunking gives better control
    and avoids potential timeouts on very long passages.
    """
    chunks = []
    # Split on chapter pause markers first
    sections = re.split(r'\.\.\.\s*\.\.\.\s*\.\.\.', text)

    for section in sections:
        section = section.strip()
        if not section:
            continue

        if len(section) <= max_chars:
            chunks.append(section)
            # Add a pause chunk between sections
            chunks.append("...")
            continue

        # Split long sections at sentence boundaries
        sentences = re.split(r'(?<=[.!?])\s+', section)
        current = ""
        for sentence in sentences:
            if len(current) + len(sentence) + 1 > max_chars and current:
                chunks.append(current.strip())
                current = sentence
            else:
                current = current + " " + sentence if current else sentence
        if current.strip():
            chunks.append(current.strip())
        # Pause between sections
        chunks.append("...")

    # Remove trailing pause
    if chunks and chunks[-1] == "...":
        chunks.pop()

    return [c for c in chunks if c.strip()]


async def generate_chunk(text, output_file, voice=VOICE, rate=RATE, retries=3):
    """Generate a single audio chunk with retry logic."""
    for attempt in range(retries):
        try:
            communicate = edge_tts.Communicate(text, voice, rate=rate)
            await communicate.save(output_file)
            if os.path.exists(output_file) and os.path.getsize(output_file) > 0:
                return True
        except Exception as e:
            if attempt < retries - 1:
                wait = 2 ** attempt
                print(f"    Retry {attempt + 1}/{retries} in {wait}s: {e}")
                await asyncio.sleep(wait)
            else:
                print(f"    FAILED after {retries} attempts: {e}")
    return False


def concatenate_mp3s(mp3_files, output_file):
    """Concatenate MP3 files using ffmpeg (preferred) or binary concat."""
    if has_ffmpeg():
        list_file = output_file + ".filelist.txt"
        with open(list_file, 'w') as f:
            for mp3 in mp3_files:
                f.write(f"file '{mp3}'\n")
        cmd = [
            "ffmpeg", "-y", "-f", "concat", "-safe", "0",
            "-i", list_file, "-c", "copy", output_file
        ]
        result = subprocess.run(cmd, capture_output=True, text=True)
        os.remove(list_file)
        if result.returncode == 0:
            return True
        print(f"  ffmpeg failed, falling back to binary concat: {result.stderr[:200]}")

    # Binary concatenation fallback (works for MP3)
    with open(output_file, 'wb') as outf:
        for mp3 in mp3_files:
            with open(mp3, 'rb') as inf:
                outf.write(inf.read())
    return True


async def generate_audiobook(input_file, output_file, label):
    """Generate a complete audiobook from a text file."""
    print(f"\n{'=' * 60}")
    print(f"  {label}")
    print(f"{'=' * 60}")

    if not os.path.exists(input_file):
        print(f"ERROR: Input file not found: {input_file}")
        return False

    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read()

    word_count = len(text.split())
    est_minutes = word_count / 150  # ~150 wpm with -5% rate
    print(f"  Words: {word_count:,}")
    print(f"  Estimated duration: {est_minutes:.0f} minutes ({est_minutes/60:.1f} hours)")

    chunks = chunk_text(text)
    total = len(chunks)
    print(f"  Chunks: {total}")
    print()

    temp_dir = tempfile.mkdtemp(prefix="audiobook_")
    mp3_files = []
    start = time.time()

    for i, chunk in enumerate(chunks):
        if not chunk.strip():
            continue

        elapsed = time.time() - start
        if i > 0 and elapsed > 0:
            rate = (i) / elapsed
            remaining = (total - i) / rate if rate > 0 else 0
            eta = f" [ETA: {remaining/60:.1f} min]"
        else:
            eta = ""

        chunk_file = os.path.join(temp_dir, f"chunk_{i:04d}.mp3")
        preview = chunk[:60].replace('\n', ' ')
        print(f"  [{i+1}/{total}]{eta} {preview}...", end="", flush=True)

        success = await generate_chunk(chunk, chunk_file)
        if success:
            mp3_files.append(chunk_file)
            size_kb = os.path.getsize(chunk_file) / 1024
            print(f" {size_kb:.0f}KB")
        else:
            print(" SKIP")

    if not mp3_files:
        print("\nERROR: No audio chunks generated!")
        return False

    total_time = time.time() - start
    print(f"\n  Synthesis complete in {total_time/60:.1f} minutes")
    print(f"  Concatenating {len(mp3_files)} chunks...")

    os.makedirs(os.path.dirname(os.path.abspath(output_file)), exist_ok=True)
    concatenate_mp3s(mp3_files, output_file)

    # Cleanup temp files
    for f in mp3_files:
        try:
            os.remove(f)
        except OSError:
            pass
    try:
        os.rmdir(temp_dir)
    except OSError:
        pass

    size_mb = os.path.getsize(output_file) / (1024 * 1024)
    print(f"\n  OUTPUT: {output_file}")
    print(f"  Size: {size_mb:.1f} MB")

    # Show duration if ffmpeg available
    if has_ffmpeg():
        result = subprocess.run(
            ["ffmpeg", "-i", output_file],
            capture_output=True, text=True
        )
        for line in result.stderr.split('\n'):
            if 'Duration' in line:
                print(f"  {line.strip()}")
                break

    return True


async def main():
    print("=" * 60)
    print("  Genesis Physics Audiobook Generator")
    print("  Voice: en-US-GuyNeural (Microsoft Neural TTS)")
    print("=" * 60)

    if has_ffmpeg():
        print("  ffmpeg: found (will use for high-quality concat)")
    else:
        print("  ffmpeg: not found (using binary concat - still works)")
    print()

    # File paths - same directory as this script
    genesis_text = os.path.join(SCRIPT_DIR, "genesis_physics_spoken_text.txt")
    mrg_text = os.path.join(SCRIPT_DIR, "mrg_spoken_text.txt")
    genesis_mp3 = os.path.join(SCRIPT_DIR, "Genesis_Physics_Audiobook.mp3")
    mrg_mp3 = os.path.join(SCRIPT_DIR, "MRG_Technical_Paper_Audiobook.mp3")

    # Generate Genesis Physics audiobook
    success1 = await generate_audiobook(genesis_text, genesis_mp3, "Genesis Physics (26 chapters + appendices)")

    # Generate MRG Technical Paper audiobook
    success2 = await generate_audiobook(mrg_text, mrg_mp3, "MRG Technical Paper")

    print(f"\n{'=' * 60}")
    print("  SUMMARY")
    print(f"{'=' * 60}")
    print(f"  Genesis Physics:    {'DONE' if success1 else 'FAILED'}")
    print(f"  MRG Technical Paper: {'DONE' if success2 else 'FAILED'}")

    if success1 or success2:
        print(f"\n  Files saved to: {SCRIPT_DIR}")
    print()


if __name__ == "__main__":
    asyncio.run(main())
