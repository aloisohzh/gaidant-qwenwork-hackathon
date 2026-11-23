"""Fit reviewed footage without cropping; never overwrite an output."""
import argparse
from pathlib import Path
import subprocess


def build(source, output, ffmpeg="ffmpeg", privacy_reviewed=False):
    source, output = Path(source), Path(output)
    if not privacy_reviewed:
        raise ValueError("Full-source privacy review is required")
    if not source.is_file():
        raise FileNotFoundError(source)
    if output.exists():
        raise FileExistsError(output)
    if not output.parent.is_dir():
        raise FileNotFoundError(output.parent)
    filters = (
        "scale=1920:1080:force_original_aspect_ratio=decrease:force_divisible_by=2,"
        "pad=1920:1080:(ow-iw)/2:(oh-ih)/2:color=black,setsar=1,fps=30"
    )
    subprocess.run([
        str(ffmpeg), "-nostdin", "-n", "-v", "error", "-i", str(source),
        "-map", "0:v:0", "-vf", filters, "-an", "-map_metadata", "-1",
        "-map_chapters", "-1", "-c:v", "libx264", "-preset", "fast",
        "-crf", "19", "-pix_fmt", "yuv420p", "-movflags", "+faststart",
        "-f", "mp4", str(output),
    ], check=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source")
    parser.add_argument("output")
    parser.add_argument("--ffmpeg", default="ffmpeg")
    parser.add_argument("--privacy-reviewed", action="store_true")
    args = parser.parse_args()
    build(args.source, args.output, args.ffmpeg, args.privacy_reviewed)
