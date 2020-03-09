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
            background-color:#1C1F21;
        }
        QLabel#Texts{
        color:#CCF20D;
        padding-left:5px;
        background-color:#000000;
        font-size: 18px;
        border-color: red;
        
        }
        """
        self.setStyleSheet(self.stylesheet)
        self.show()
    def TourGuideUI(self):
        self.setWindowTitle("TOUR GUIDE UI")
        self.setGeometry(self.x,self.y,self.width,self.height)
        self.Icon=QLabel(self)
        pixmap=QPixmap('BlankIcon.ico')
        self.Icon.setPixmap(pixmap)
        self.Icon.setGeometry(150,100,200,150)
        self.nameBox=QLabel("Driver Name",self)
        self.nameBox.setGeometry(300,112,200,28)
        self.HomeLocation=QLabel("Location/Region",self)
        self.HomeLocation.setGeometry(300,147,200,28)
        self.Loyalty=QLabel("Loyalty level:   ",self)
        self.Loyalty.setGeometry(300,182,200,28)
        self.nameBox.setObjectName("Texts")
        self.HomeLocation.setObjectName("Texts")
        self.Loyalty.setObjectName("Texts")

        self.show()

        
    

    #@pyqtSlot()
if __name__=='__main__':
    app=QApplication(sys.argv)
    ex=App()
    sys.exit(app.exec_())