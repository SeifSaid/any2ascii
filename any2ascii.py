from PIL import Image
import numpy as np
from palettes import PALETTES

im_path = "test2.jpg"
MAX_W = 50 
palette_name = "noir"

palette = PALETTES[palette_name]
ramp = palette["ramp"]
square = palette["square"]
N = len(ramp)

im = Image.open(im_path).convert("L")
orig_w, orig_h = im.size

cols = min(MAX_W, orig_w)
rows = max(1, round(cols * orig_h / orig_w))

im_resized = im.resize((cols, rows))
pixels = np.array(im_resized)

lines = []
for r in range(rows):
    line = []
    for c in range(cols):
        idx = min(N - 1, int(pixels[r, c]) * N // 256)
        ch = ramp[idx]
        line.append(ch if square else ch * 2)
    lines.append("".join(line))

art = "\n".join(lines)
print(art)

with open("art.txt", "w", encoding="utf-8") as f:
    f.write(art)
