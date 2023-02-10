import sys
from random import randrange

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog


class Window(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('circles.ui', self)
        #self.startButton.clicked.connect(self.draw_ellipse)
        #a =


    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        self.draw_ellipse(painter)
        painter.end()
    def draw_ellipse(self, painter):
        painter.setBrush(QColor(251, 255, 31))
        painter.drawEllipse(randrange(200), randrange(200), randrange(80), randrange(80))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    zxc = Window()
    zxc.show()
    sys.exit(app.exec())