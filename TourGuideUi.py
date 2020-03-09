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
        color:#E9ED68;background-color:#000000;
        padding-left:5px;
        font-size: 20px;
        }
        """
        self.setStyleSheet(self.stylesheet)
        self.show()
    def TourGuideUI(self):
        self.UserSide()
        self.RatingSide()
        self.show()
    def UserSide(self):
        self.setWindowTitle("TOUR GUIDE UI")
        self.setGeometry(self.x,self.y,self.width,self.height)
        self.Icon=QLabel(self)
        pixmap=QPixmap('BlankIcon.ico')
        self.Icon.setPixmap(pixmap)
        self.Icon.setGeometry(150,100,400,150)
        self.Icon.setStyleSheet("""
        border-radius: 25px;
        border: 2px solid #E9ED68;background: #FFFFFF;
        padding: 20px;width: 200px;height: 150px;
        """)
        self.nameBox=QLabel("Driver Name",self)
        self.nameBox.setGeometry(310,122,220,28)
        self.HomeLocation=QLabel("Location/Region",self)
        self.HomeLocation.setGeometry(310,161,220,28)
        self.Loyalty=QLabel("Loyalty level:   ",self)
        self.Loyalty.setGeometry(310,200,220,28)
        self.nameBox.setObjectName("Texts")
        self.HomeLocation.setObjectName("Texts")
        self.Loyalty.setObjectName("Texts")
    def RatingSide(self):

    

    #@pyqtSlot()
if __name__=='__main__':
    app=QApplication(sys.argv)
    ex=App()
    sys.exit(app.exec_())