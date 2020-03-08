import sys
from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class App(QMainWindow):

    
    def __init__(self):
        super().__init__()
        self.title="Supplementary Activity -CruzZ"
        self.x=800 # or left
        self.y=350 # or top
        self.width=400
        self.height=400
        self.initUI()

    def initUI(self):
        self.setGeometry(self.x,self.y,self.width,self.height)
        vbox=QHBoxLayout
    def Namespace(self):
        self.GroupBox=QGroupBox("")
        NameLocLoyal=QVBoxLayout()
        Name=QLabel("Tour Guide Name0",self)
        Name.setGeometry(QRect(100,100,150,50))
        Name.setMinimumHeight(40)
        NameLocLoyal.addWidget(Name)
        self.show()


if __name__ == "__main__":

    app = QApplication(sys.argv)
    Mainwindow = App()
    sys.exit(app.exec_())