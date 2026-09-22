"""Regenerate public media. Requires Pillow; pass --ffmpeg PATH for video encoding."""
from pathlib import Path
import argparse
import shutil
import subprocess
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'Assets'
OUT = ROOT / 'docs' / 'media'
OUT.mkdir(parents=True, exist_ok=True)
parser = argparse.ArgumentParser()
parser.add_argument('--ffmpeg')
args = parser.parse_args()

def webp(source, name, widths):
    with Image.open(source) as original:
        for width in widths:
            image = original.convert('RGB')
            image.thumbnail((width, 10000), Image.Resampling.LANCZOS)
            image.save(OUT / f'{name}-{width}.webp', quality=85, method=6)

for number in range(1, 7):
    webp(SOURCE / 'TRAPPIST-1PressStuff' / f'Screenshot ({number}).png', f'station-{number}', [640, 1280, 1920])
    with Image.open(SOURCE / 'TRAPPIST-1PressStuff' / f'Screenshot ({number}).png') as thumb:
        thumb.thumbnail((400, 225))
        thumb.save(OUT / f'station-{number}-thumb.webp', quality=80, method=6)
webp(SOURCE / 'Images' / 'TrappistHeroArt.png', 'trappist-hero', [800, 1600])
webp(SOURCE / 'Images' / 'Adri.jpg', 'adri', [400])
for source, name in [('Signal', 'signal'), ('Hallway', 'hallway'), ('StellarSucker', 'extraction')]:
    webp(SOURCE / 'TRAPPIST-1PressStuff' / f'{source}.gif', name, [640, 1280])
    if name in ['signal', 'hallway']:
        if args.ffmpeg:
            subprocess.run([args.ffmpeg, '-y', '-hide_banner', '-loglevel', 'error', '-i', str(SOURCE / 'TRAPPIST-1PressStuff' / f'{source}.gif'), '-filter_complex', '[0:v]fps=10,scale=640:-1:flags=lanczos,split[a][b];[a]palettegen=max_colors=96:stats_mode=diff[p];[b][p]paletteuse=dither=none:diff_mode=rectangle', '-loop', '0', str(OUT / f'{name}.gif')], check=True)
        elif not (OUT / f'{name}.gif').exists():
            # Preserve ready-to-use optimized copies without requiring FFmpeg.
            shutil.copyfile(SOURCE / 'TRAPPIST-1PressStuff' / f'{source}.gif', OUT / f'{name}.gif')
shutil.copyfile(SOURCE / 'Images' / 'SkeletonWithAKs.gif', OUT / 'skeleton.gif')
with Image.open(SOURCE / 'Images' / 'SkeletonWithAKs.gif') as skeleton:
    skeleton.convert('RGBA').save(OUT / 'skeleton-still.webp', quality=90)
logo = (SOURCE / 'Logos' / 'SYSTM.svg').read_text(encoding='utf-8')
# Tighten only the implementation copy's canvas; retain the original vector paths.
logo = logo.replace('viewBox="0 0 4500 1050"', 'viewBox="470 110 3260 845"')
(OUT / 'systm.svg').write_text(logo, encoding='utf-8')
shutil.copyfile(SOURCE / 'Logos' / 'TRAPPIST-NEGRO.svg', OUT / 'trappist.svg')

if args.ffmpeg:
    for source, name in [('Signal', 'signal'), ('Hallway', 'hallway'), ('StellarSucker', 'extraction')]:
        subprocess.run([args.ffmpeg, '-y', '-hide_banner', '-loglevel', 'error', '-i', str(SOURCE / 'TRAPPIST-1PressStuff' / f'{source}.gif'), '-an', '-vf', 'scale=1280:-2', '-c:v', 'libx264', '-preset', 'medium', '-crf', '24', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', str(OUT / f'{name}.mp4')], check=True)
    subprocess.run([args.ffmpeg, '-y', '-hide_banner', '-loglevel', 'error', '-i', str(SOURCE / 'Videos' / 'Trailer.mp4'), '-map', '0:v:0', '-map', '0:a:0', '-vf', 'scale=1280:-2,fps=30', '-c:v', 'libx264', '-preset', 'medium', '-crf', '23', '-c:a', 'aac', '-b:a', '128k', '-map_metadata', '-1', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', str(OUT / 'trailer.mp4')], check=True)
for path in sorted(OUT.iterdir()):
    print(f'{path.name}: {path.stat().st_size:,} bytes')
