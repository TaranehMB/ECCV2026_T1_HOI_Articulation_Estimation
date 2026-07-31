import os
from PIL import Image

# Path to the main directory containing all your object folders
parent_dir = r"datasets/parent_directory"  # adjust this path as needed

# Loop through every item in the parent directory
for object_name in os.listdir(parent_dir):
    object_dir = os.path.join(parent_dir, object_name)
    
    # Check if the item is a directory
    if os.path.isdir(object_dir):
        frame_dir = os.path.join(object_dir, "rgb")
        
        # Make sure the 'rgb' folder actually exists and isn't empty
        if os.path.exists(frame_dir) and os.path.isdir(frame_dir):
            frames = sorted([
                f for f in os.listdir(frame_dir) 
                if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp'))
            ])
            
            if not frames:
                print(f"Skipping {object_name}: No valid images in 'rgb' folder.")
                continue
            
            # Load images
            imgs = [Image.open(os.path.join(frame_dir, f)).convert("RGB") for f in frames]
            
            # Downsize if needed
            imgs = [im.resize((512, 512)) for im in imgs]
            
            # Save output GIF directly in the object folder
            out_path = os.path.join(object_dir, "preview.gif")
            imgs[0].save(
                out_path,
                save_all=True,
                append_images=imgs[1:],
                duration=100,  # ms per frame
                loop=0
            )
            print(f"Saved: {out_path}")
        else:
            print(f"Skipping {object_name}: 'rgb' folder not found.")