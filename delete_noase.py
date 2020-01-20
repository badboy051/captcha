import numpy as np


def count_black(image, x, y, y1, x1, getother=True):
    b = 0
    xm = x1 > 0
    xp = x1 < x
    ym = y1 > 0
    yp = y1 < y
    if ym and image[y1 - 1, x1] == 0:
        b += count_black(image, x, y, y1 - 1, x1, False) if getother else 1
    if ym and xm and image[y1 - 1, x1 - 1] == 0:
        b += count_black(image, x, y, y1 - 1, x1 - 1, False) if getother else 1
    if ym and xp and image[y1 - 1, x1 + 1] == 0:
        b += count_black(image, x, y, y1 - 1, x1 + 1, False) if getother else 1
    if xm and image[y1, x1 - 1] == 0:
        b += count_black(image, x, y, y1, x1 - 1, False) if getother else 1
    if xp and image[y1, x1 + 1] == 0:
        b += count_black(image, x, y, y1, x1 + 1, False) if getother else 1
    if yp and image[y1 + 1, x1] == 0:
        b += count_black(image, x, y, y1 + 1, x1, False) if getother else 1
    if yp and xm and image[y1 + 1, x1 - 1] == 0:
        b += count_black(image, x, y, y1 + 1, x1 - 1, False) if getother else 1
    if yp and xp and image[y1 + 1, x1 + 1] == 0:
        b += count_black(image, x, y, y1 + 1, x1 + 1, False) if getother else 1
    return b


def delete_nose(image):
    bsum = 0
    y, x = image.shape
    for y1 in range(y):
        for x1 in range(x):
            if image[y1, x1] == 255:
                continue
            else:

                b = count_black(image, x - 1, y - 1, y1, x1)
                if b < 4:
                    image[y1, x1] = 255
                else:
                    bsum += b
    return [bsum,x * y - np.count_nonzero(image)]
