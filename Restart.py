import sys
from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


StyleSheet = '''
QPushButton#BlueButton {
    background-color: #2196f3;
    /* Ограничьте минимальный размер */
    min-width:  96px;
    max-width:  96px;
    min-height: 96px;
    max-height: 96px;
    border-radius: 48px;        /* круглый */
}

QPushButton#BlueButton:hover {
    background-color: #64b5f6;
    color: #fff;
}

QPushButton#BlueButton:pressed {
    background-color: #bbdefb;
}
'''
class BookPopUp(QDialog):
    def __init__(self, parent=None):
        super().__init__()
        self.setGeometry(615,200,650,544)
        self.Test=QPushButton("What",self)
        self.Test.setObjectName("BlueButton")
        self.show()

class TourGuideUI(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        #1280x720
        self.setGeometry(300,150,1270,680)
        self.show()

if __name__ == '__main__':
    app=QApplication(sys.argv)
    ex=BookPopUp()
    sys.exit(app.exec_())