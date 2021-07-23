# -*- coding: utf-8 -*-
from PIL import Image
from PIL import ImageEnhance

below = Image.open("below.png")
above = Image.open("above.png")

below = below.convert("L")
below = below.convert('RGBA')
below = ImageEnhance.Brightness(below).enhance(0.6)
above = above.convert("L")
above = above.convert('RGBA')
above = ImageEnhance.Brightness(above).enhance(1.2)
above = above.resize(below.size)
max_x, max_y = below.size

x = -1
y = -1
while x < max_x - 1:
    x += 1
    y = -1
    while y < max_y - 1:
        y += 1

        P_above = above.getpixel((x , y))[0]
        P_below = below.getpixel((x , y))[0]

        alpha = 255 - P_above + P_below
        P_MirageTank = P_below * 255 // alpha
        below.putpixel((x , y),(P_MirageTank,P_MirageTank,P_MirageTank,alpha))

below.save("MirageTank.png")