import json
from pillow import image_data
from os import remove
from poya import Poya
import cv2

numbers = {"sum_dots": [], "dots": [], "num": []}

play = True

while play:
    command = input("enter command (Add , Test , Stop , Start )")

    data = command.split(" ")
    if data[0].lower() == "add":
        try:
            p = Poya()
            cv2.imshow("all", cv2.imread(p.file_name))
            cv2.waitKey(300)
            reload = input("enter numbers or reload:")
            while reload == "reload":
                cv2.destroyAllWindows()
                p.get_image()
                cv2.imshow("all", cv2.imread(p.file_name))
                cv2.waitKey(300)
                reload = input("enter numbers or reload:")
            cv2.destroyAllWindows()

            i = 0
            for dots in image_data(p.file_name):
                numbers['sum_dots'].append(dots[0])
                numbers['dots'].append(dots[1])
                numbers['num'].append(reload[i])

                i += 1
            remove(p.file_name)
            del p
        except Exception as e:
            print(str(e))

    elif data[0].lower() == "stop":
        try:
            json.dump(numbers, open("poya.json", "a"))
        except Exception as e:
            print(e)
        play = False
        print("file saved")
