import numpy as np
import cv2


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


def count_h(image, x, y):
    y2 = y3 = 0
    for x1 in range(x):
        for y1 in range(y):
            if image[y1, x1] == 0:
                y3 += 1
        if y3 > y2:
            y2 = y3
        y3 = 0
    return y2


def delete_nose(image):
    bsum = 0
    y, x = image.shape
    x2 = x3 = 0
    black = 0
    for y1 in range(y):
        for x1 in range(x):
            if image[y1, x1] == 255:
                continue
            else:
                b = count_black(image, x - 1, y - 1, y1, x1)
                x3 += 1
                black += 1
                if b < 4:
                    image[y1, x1] = 255
                else:
                    bsum += b
        if x2 < x3:
            x2 = x3
        x3 = 0
    cv2.imshow("test" + str(bsum), image)
    return [bsum, black, x2, count_h(image, x, y)]
