from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit
from PyQt5.QtGui import QTextBlock, QPixmap, QKeyEvent
from PyQt5.QtCore import Qt
import sys
from os import remove
from poya import Poya
from pillow import image_data
import json
import sqlite3
from threading import Thread, Timer


# Start the event loop.


class app(QWidget):
    def __init__(self):
        super().__init__()
        self.connection = sqlite3.connect("poya.sqlite")
        self.controller = self.connection.cursor()
        label = QLabel(self)
        self.poya = Poya()
        pixmap = QPixmap(self.poya.file_name)
        label.setPixmap(pixmap)
        label.move(int(250 - pixmap.width() / 2), int(250.0 - pixmap.height() / 2))
        self.label = label
        self.resize(500, 500)
        self.ts = QLineEdit(self)
        self.ts.setAlignment(Qt.AlignCenter)
        self.ts.resize(160, 30)
        self.ts.setMaxLength(5)
        self.ts.move(int(250 - self.ts.width() / 2), 250 + pixmap.height())
        self.ts.keyPressEvent = self.onkeypress
        self.show()
        self.numbers = {"sum_dots": [], "dots": [], "num": []}

    def onkeypress(self, e: QKeyEvent):
        text = self.ts.text()
        key = e.key()
        print(key)
        if key in [16777221, 16777220] and len(text) == 5:
            self.add_new(text)
        elif e.key() == 43:
            self.poya.get_image()
            self.label.setPixmap(QPixmap(self.poya.file_name))
        elif 47 < key < 58:
            self.ts.setText(text + chr(key))
        elif key == 16777219:
            self.ts.setText(text[:-1])

    def add_new(self, number):
        try:
            i = 0
            for dots in image_data(self.poya.file_name):
                self.controller.execute(
                    "INSERT INTO"
                    " dataset (site, sum_dots, dots, label)"
                    " VALUES  ('{}',{},{},'{}')".format("pooya.sadjad.ac.ir", dots[0], dots[1], str(number[i])))
                self.connection.commit()
                self.numbers['sum_dots'].append(dots[0])
                self.numbers['dots'].append(dots[1])
                self.numbers['num'].append(number[i])

                i += 1
            remove(self.poya.file_name)
            del self.poya
            self.poya = Poya()
            self.label.setPixmap(QPixmap(self.poya.file_name))
            self.ts.setText("")

        except Exception as e:
            print(str(e))


if __name__ == '__main__':

    app1 = QApplication(sys.argv)
    ex = app()
    sys.exit(app1.exec_())


# c.execute(
#     "CREATE TABLE dataset "
#     "(id INTEGER PRIMARY KEY AUTOINCREMENT ,"
#     " site TEXT NOT NULL ,"
#     "sum_dots INTEGER NOT NULL ,"
#     "dots INTEGER NOT NULL ,"
#     "label TEXT NOT NULL );")

