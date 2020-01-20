import cv2
import numpy as np
from delete_noase import delete_nose


def image_data(path):
    image = cv2.cvtColor(cv2.imread(path), cv2.COLOR_BGR2GRAY)
    numbers = list()
    p = 0
    for x in range(1, 6):

        if x != 1:
            p += 10
        print(x, p)

        numbers.append(image[0:, 16 * x + p - 3: 16 * (x + 1) + p + 10])
        numbers[-1] = cv2.threshold(numbers[-1], 50, 255, cv2.THRESH_BINARY)[1]
        dots = delete_nose(numbers[-1])
        # cv2.imshow("start :{} and stop : {}".format(16 * x + p, 16 * (x + 1) + p), numbers[-1])
        # cv2.waitKey(500)
        # key = input("enter image label:")
        # cv2.destroyAllWindows()
        yield dots
