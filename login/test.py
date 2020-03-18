import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from sqlitedict import *
import sip

sip.setapi('QString', 2)
sip.setapi('QVariant', 2)

class test(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Test")
        self.setGeometry(300,300,300,300)

        self.password = QLineEdit(self)
        self.password.setEchoMode(QLineEdit.Password)
        self.password.move(50, 50)

        self.button = QPushButton("Test", self)
        self.button.clicked.connect(self.test)
        self.button.move(50,150)

        self.label = QLabel("test", self)
        self.label.setGeometry(50,250,2000,50)

        self.show()

    def test(self):
        self.label.setText(self.password.text())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = test()
    sys.exit(app.exec_())