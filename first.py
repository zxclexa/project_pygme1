from random import randrange

from PyQt5.QtGui import QPainter, QColor
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(9, 9, 381, 231))
        self.widget.setObjectName("widget")
        self.startButton = QtWidgets.QPushButton(Dialog)
        self.startButton.setGeometry(QtCore.QRect(180, 250, 51, 41))
        self.startButton.setObjectName("startButton")

        #self.startButton.clicked.connect(self.paintEvent(self))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.startButton.setText(_translate("Dialog", "circle"))



    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        self.draw_ellipse(painter)
        painter.end()
    def draw_ellipse(self, painter):
        painter.setBrush(QColor(randrange(255), randrange(255), randrange(255)))
        painter.drawEllipse(randrange(200), randrange(200), randrange(80), randrange(80))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())