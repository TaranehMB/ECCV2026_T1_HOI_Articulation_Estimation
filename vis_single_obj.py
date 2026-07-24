import os
from PIL import Image

root = r"\path\to\object"
frame_dir = os.path.join(root, "rgb")  
frame_dir = os.path.join(root, "rgb")

frames = sorted(os.listdir(frame_dir))
imgs = [Image.open(os.path.join(frame_dir, f)).convert("RGB") for f in frames]

# downsize if 1408x1408 is heavy for a gif
imgs = [im.resize((512, 512)) for im in imgs]

out_path = os.path.join(root, "preview.gif")
imgs[0].save(
    out_path,
    save_all=True,
    append_images=imgs[1:],
    duration=100,   # ms per frame — lower = faster playback
    loop=0
)
print(f"Saved: {out_path}")