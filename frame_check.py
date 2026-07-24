from PIL import Image
import os

frame_dir = r"F:\Taraneh\university\Job and Phd applications\ECCV2026-challenge\datasets\articulation data\kitchen_9_obj1\rgb"  # adjust
frames = sorted(os.listdir(frame_dir))
print(f"Total frames: {len(frames)}")
print(f"First: {frames[0]}, Last: {frames[-1]}")

img = Image.open(os.path.join(frame_dir, frames[0]))
print(f"Resolution: {img.size}, Mode: {img.mode}")