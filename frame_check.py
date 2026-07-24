from PIL import Image
import os

root = r"\path\to\object"  # adjust
frames = sorted(os.listdir(frame_dir))
print(f"Total frames: {len(frames)}")
print(f"First: {frames[0]}, Last: {frames[-1]}")

img = Image.open(os.path.join(frame_dir, frames[0]))
print(f"Resolution: {img.size}, Mode: {img.mode}")