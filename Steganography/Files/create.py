from PIL import Image
import random

flag = open("flag.txt").readlines()[0].strip()

green = Image.new(mode="RGB", size=(512, 512), color=(77, 162, 20))
pixels = green.load()

diff_pixel = 7

for index, c in enumerate(flag):
    width = green.size[0] // len(flag)
    height = green.size[1] // len(flag)
    for _ in range(ord(c)):
        p = random.randint(0, width-1)+width*index,random.randint(0, height-1)+height*index
        color_index = random.randint(0, 2)
        color = list(pixels[p])
        color[color_index] += diff_pixel
        pixels[p] = tuple(color)

green.save('./v3Rt.png')
