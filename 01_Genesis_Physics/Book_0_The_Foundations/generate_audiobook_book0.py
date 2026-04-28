"""
generate_audiobook_book0.py — TTS + M4B packaging for Book 0, all 6 volumes

Reads each volume's chapter_titles_VolN.json (written by preprocess_book0.py),
generates per-chapter MP3 via edge-tts, then packages one M4B per volume.

Output per volume: Vol_N_Name/audio book/VolN_Name.m4b

Usage:
  python generate_audiobook_book0.py           # all 6 volumes
  python generate_audiobook_book0.py 3         # only volume 3
  python generate_audiobook_book0.py 1 2 3     # volumes 1, 2, 3
"""

import asyncio
import json
import subprocess
import sys
from pathlib import Path

# Force UTF-8 output so non-ASCII chapter titles don't crash on Windows cp1252 console
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

import edge_tts

BASE = Path(__file__).parent  # Book_0_The_Foundations/

VOICE = 'en-US-AndrewNeural'
AUTHOR = 'Jeff Raymond'

FFMPEG = (
    r'C:\Users\JeffRaymond\AppData\Local\Microsoft\WinGet\Packages'
    r'\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe'
    r'\ffmpeg-8.1-full_build\bin\ffmpeg.exe'
)
FFPROBE = FFMPEG.replace('ffmpeg.exe', 'ffprobe.exe')

VOL_FOLDERS = {
    1: ('Vol_1_Architecture_of_Reality',   'Vol1_Architecture_of_Reality'),
    2: ('Vol_2_Forces_and_Fields',          'Vol2_Forces_and_Fields'),
    3: ('Vol_3_Matter_and_Motion',          'Vol3_Matter_and_Motion'),
    4: ('Vol_4_The_Quantum_World',          'Vol4_The_Quantum_World'),
    5: ('Vol_5_The_Cosmos',                 'Vol5_The_Cosmos'),
    6: ('Vol_6_Predictions_and_Simulations','Vol6_Predictions_and_Simulations'),
}


def find_ffmpeg():
    if Path(FFMPEG).exists():
        return FFMPEG
    try:
        subprocess.run(['ffmpeg', '-version'], capture_output=True, check=True)
        return 'ffmpeg'
    except Exception:
        pass
    raise RuntimeError(f'ffmpeg not found. Expected: {FFMPEG}')


def get_duration_ms(mp3_path: Path) -> int:
    result = subprocess.run(
        [FFPROBE, '-v', 'quiet', '-print_format', 'json', '-show_streams', str(mp3_path)],
        capture_output=True, text=True, check=True,
    )
    data = json.loads(result.stdout)
    for stream in data.get('streams', []):
        if stream.get('codec_type') == 'audio':
            return int(float(stream['duration']) * 1000)
    raise ValueError(f'No audio stream in {mp3_path}')


async def generate_mp3(text: str, mp3_path: Path):
    if mp3_path.exists() and mp3_path.stat().st_size > 10_000:
        print(f'    Cached: {mp3_path.name}')
        return
    print(f'    Generating: {mp3_path.name} ({len(text):,} chars)...')
    communicate = edge_tts.Communicate(text, VOICE)
    await communicate.save(str(mp3_path))
    size_mb = mp3_path.stat().st_size / 1_048_576
    print(f'    Done: {mp3_path.name} ({size_mb:.1f} MB)')


async def process_volume(vol_num: int):
    vol_folder, vol_stem = VOL_FOLDERS[vol_num]
    vol_dir = BASE / vol_folder
    audio_dir = vol_dir / 'audio book'
    chapters_dir = audio_dir / 'chapters'

    meta_file = audio_dir / f'chapter_titles_Vol{vol_num}.json'
    if not meta_file.exists():
        print(f'\nERROR: {meta_file} not found. Run preprocess_book0.py first.')
        return

    data = json.loads(meta_file.read_text(encoding='utf-8'))
    vol_cfg = data['volume']
    chapters = data['chapters']

    output_m4b = audio_dir / f'{vol_stem}.m4b'
    concat_mp3 = audio_dir / f'{vol_stem}_concat.mp3'
    concat_list = audio_dir / f'{vol_stem}_concat_list.txt'
    ffmeta_file = audio_dir / f'{vol_stem}_ffmetadata.txt'

    print(f'\n{"="*60}')
    print(f'  Volume {vol_num}: {vol_cfg["title"]}')
    print(f'  {len(chapters)} sections')
    print(f'{"="*60}')

    # --- Step 1: Generate TTS MP3s ---
    print(f'\nStep 1: TTS generation ({VOICE})...')
    mp3_paths = []
    for idx, ch in enumerate(chapters, 1):
        key = ch['key']
        clean_file = Path(ch['clean_file'])
        if not clean_file.exists():
            print(f'  WARNING: {clean_file} missing — skipping {key}')
            continue
        text = f"{ch['title']}.\n\n" + clean_file.read_text(encoding='utf-8')
        mp3_path = chapters_dir / f'{key}.mp3'
        print(f'  [{idx}/{len(chapters)}] {key}: {ch["title"]}')
        await generate_mp3(text, mp3_path)
        mp3_paths.append((ch, mp3_path))

    if not mp3_paths:
        print('  ERROR: No MP3s generated.')
        return

    # --- Step 2: Measure durations + build metadata ---
    ffmpeg = find_ffmpeg()
    print(f'\nStep 2: Measuring durations...')
    timeline = []
    cursor_ms = 0
    for ch, mp3_path in mp3_paths:
        dur = get_duration_ms(mp3_path)
        m, s = dur // 60000, (dur % 60000) / 1000
        print(f'  {mp3_path.name}: {m}m {s:.0f}s')
        timeline.append((ch, mp3_path, cursor_ms, cursor_ms + dur))
        cursor_ms += dur

    total_ms = cursor_ms
    total_h = total_ms / 3_600_000
    print(f'  Total: {total_ms//60000}m ({total_h:.2f} hours)')

    # Write concat list
    with open(concat_list, 'w', encoding='utf-8') as f:
        for _, mp3_path, _, _ in timeline:
            f.write(f"file '{mp3_path.resolve()}'\n")

    # Write FFMETADATA
    lines = [
        ';FFMETADATA1',
        f'title={vol_cfg["title"]}',
        f'artist={AUTHOR}',
        f'album={vol_cfg["title"]}',
        'genre=Audiobook',
        '',
    ]
    for ch, _, start, end in timeline:
        lines += [
            '[CHAPTER]',
            'TIMEBASE=1/1000',
            f'START={start}',
            f'END={end}',
            f'title={ch["title"]}',
            '',
        ]
    ffmeta_file.write_text('\n'.join(lines), encoding='utf-8')

    # --- Step 3: Concatenate and package ---
    print(f'\nStep 3: Concatenating MP3s...')
    subprocess.run(
        [ffmpeg, '-y', '-f', 'concat', '-safe', '0',
         '-i', str(concat_list), '-c', 'copy', str(concat_mp3)],
        check=True,
    )

    print(f'Step 4: Packaging M4B...')
    subprocess.run(
        [ffmpeg, '-y',
         '-i', str(concat_mp3),
         '-i', str(ffmeta_file),
         '-map_metadata', '1',
         '-map', '0:a',
         '-c:a', 'aac', '-b:a', '64k',
         str(output_m4b)],
        check=True,
    )

    # Cleanup
    if concat_mp3.exists():
        concat_mp3.unlink()

    size_mb = output_m4b.stat().st_size / 1_048_576
    print(f'\n  [DONE] {output_m4b.name}')
    print(f'    Size: {size_mb:.1f} MB | Runtime: {total_ms//60000}m ({total_h:.2f} hours)')
    print(f'    Chapters: {len(timeline)}')


async def main():
    # Parse volume args
    if len(sys.argv) > 1:
        vol_nums = [int(a) for a in sys.argv[1:] if a.isdigit()]
        if not all(1 <= v <= 6 for v in vol_nums):
            print('Volume numbers must be 1–6.')
            sys.exit(1)
    else:
        vol_nums = list(range(1, 7))

    print(f'=== Book 0: The Foundations — Audiobook Generation ===')
    print(f'Volumes to process: {vol_nums}')

    find_ffmpeg()  # fail fast if ffmpeg missing

    for vol_num in vol_nums:
        await process_volume(vol_num)

    print(f'\n=== ALL COMPLETE ===')
    for vol_num in vol_nums:
        vol_folder, vol_stem = VOL_FOLDERS[vol_num]
        m4b = BASE / vol_folder / 'audio book' / f'{vol_stem}.m4b'
        if m4b.exists():
            size_mb = m4b.stat().st_size / 1_048_576
            print(f'  Vol {vol_num}: {m4b.name}  ({size_mb:.1f} MB)')
        else:
            print(f'  Vol {vol_num}: MISSING — check for errors above')


if __name__ == '__main__':
    asyncio.run(main())
