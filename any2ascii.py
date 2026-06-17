from PIL import Image
from numpy import array
from palettes import PALETTES

im_path = "test.jpeg"
W = 50
H = 50
palette = "bars"

im = Image.open(im_path)
resizeed_im = im.resize((W, H))
im_gray = resizeed_im.convert("L")
im_array = array(im_gray)
print(im_array)
N = len(PALETTES[palette])
rows = []
for i in range(H):
    row = ""
    for j in range(W):
        pixel_value = im_array[i][j]
        char_index = int(pixel_value / 256 * N)
        row += PALETTES[palette][char_index]
        #row += PALETTES[palette][char_index]
    rows.append(row)

for row in rows:
    print(row)

art = "\n".join(rows)
with open("art.txt", "w", encoding="utf-8") as f:
    f.write(art)