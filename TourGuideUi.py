import sys
from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class App(QMainWindow):

    
    def __init__(self):
        super().__init__()
        self.x=500 # or left
        self.y=100 # or top
        self.width=850
        self.height=650
        self.TourGuideUI()
        self.stylesheet= """
        QMainWindow{
            background-color:color:#1C1F21;
        }
        QLabel{
            background-color: ;color:#CCF20D;padding-left:5px;
        }
        """
        self.show()
    def TourGuideUI(self):
        self.setWindowTitle("TOUR GUIDE UI")
        self.setGeometry(self.x,self.y,self.width,self.height)
        self.Icon=QLabel(self)
        pixmap=QPixmap('BlankIcon.ico')
        self.Icon.setPixmap(pixmap)
        self.Icon.setGeometry(150,0,200,150)
        self.nameBox=QLabel("Driver Name",self)
        self.nameBox.setGeometry(300,10,100,100)
        self.nameBox.setStyleSheet("
        ")
        self.show()

        
    

    #@pyqtSlot()
if __name__=='__main__':
    app=QApplication(sys.argv)
    ex=App()
    sys.exit(app.exec_())