import os

root = r"\path\to\object"

for dirpath, dirnames, filenames in os.walk(root):
    depth = dirpath[len(root):].count(os.sep)
    if depth > 1:
        continue
    print(dirpath)
    for f in filenames[:5]:  # just first 5 to avoid flooding output
        print("  ", f)
    if len(filenames) > 5:
        print(f"   ... ({len(filenames)} files total)")