"""Synthetic media only; no private recordings are accessed."""
import importlib.util
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

SPEC = importlib.util.spec_from_file_location(
    "build_video", Path(__file__).resolve().parents[1] / "scripts" / "build_video.py"
)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)
FFMPEG = os.environ.get("FFMPEG") or shutil.which("ffmpeg")


class BuildTests(unittest.TestCase):
    def test_requires_review(self):
        with self.assertRaises(ValueError):
            MODULE.build("missing.mp4", "unused.mp4")

    def test_refuses_overwrite(self):
        with tempfile.TemporaryDirectory() as folder:
            source = Path(folder) / "source.mp4"
            output = Path(folder) / "output.mp4"
            source.touch()
            output.write_bytes(b"preserve")
            with self.assertRaises(FileExistsError):
                MODULE.build(source, output, privacy_reviewed=True)
            self.assertEqual(output.read_bytes(), b"preserve")

    @unittest.skipUnless(FFMPEG, "FFmpeg required for synthetic integration check")
    def test_full_frame_and_decode(self):
        with tempfile.TemporaryDirectory() as folder:
            source = Path(folder) / "source.mp4"
            output = Path(folder) / "output.mp4"
            subprocess.run([
                FFMPEG, "-nostdin", "-n", "-v", "error", "-f", "lavfi", "-i",
                "color=c=red:s=320x240:r=30:d=0.2", "-vf",
                "drawbox=x=0:y=0:w=iw:h=ih:color=white:t=12",
                "-c:v", "libx264", "-pix_fmt", "yuv420p", str(source),
            ], check=True)
            MODULE.build(source, output, FFMPEG, True)
            result = subprocess.run([
                FFMPEG, "-v", "error", "-i", str(output), "-map", "0:v:0",
                "-pix_fmt", "rgb24", "-f", "rawvideo", "pipe:1",
            ], capture_output=True, check=True)
            width, height = 1920, 1080
            self.assertEqual(len(result.stdout), width * height * 3 * 6)
            frame = result.stdout[:width * height * 3]
            def pixel(x, y):
                start = (y * width + x) * 3
                return tuple(frame[start:start + 3])
            self.assertLess(max(pixel(20, 540)), 20)
            for point in [(250, 540), (1669, 540), (960, 10), (960, 1069)]:
                self.assertGreater(min(pixel(*point)), 200)
            self.assertGreater(pixel(960, 540)[0], 200)
            self.assertLess(pixel(960, 540)[1], 40)
            metadata = subprocess.run([
                FFMPEG, "-v", "info", "-i", str(output), "-f", "null", "-"
            ], capture_output=True, text=True, check=True).stderr
            self.assertIn("1920x1080", metadata)
            self.assertIn("30 fps", metadata)
            self.assertNotIn("Audio:", metadata)


if __name__ == "__main__":
    unittest.main()
