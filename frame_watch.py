import os
from PIL import Image
import matplotlib.pyplot as plt

root = r"F:\Taraneh\university\Job and Phd applications\ECCV2026-challenge\datasets\articulation data\kitchen_9_obj1"
frame_dir = os.path.join(root, "rgb")  
frames = sorted(os.listdir(frame_dir))
print(f"Total frames: {len(frames)}")
print(f"Naming pattern: {frames[:3]}")

img0 = Image.open(os.path.join(frame_dir, frames[0]))
print(f"Resolution: {img0.size}, mode: {img0.mode}")

fig, axes = plt.subplots(1, 4, figsize=(16,4))
indices = [0, len(frames)//3, 2*len(frames)//3, len(frames)-1]
for ax, i in zip(axes, indices):
    img = Image.open(os.path.join(frame_dir, frames[i]))
    ax.imshow(img)
    ax.set_title(f"frame {i}")
    ax.axis('off')
plt.show()