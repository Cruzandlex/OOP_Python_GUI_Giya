import sys
from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *



class BookPopUp(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.setStyleSheet("""
            QWidget{
                background-color:#FFFFFF
            }
            QPushButton#BlueButton {
                background-color: #2196f3;   
            }

            QPushButton#BlueButton:hover {
                background-color: #494F5B;
                color: #fff;
            }

            QPushButton#BlueButton:pressed {
                background-color: #64b5f6;
            }
            QLabel#Image{
                border: 4px solid, #000000;
                border-radius:124;
            }
            QLabel#BottomText{
                border: 2px solid,#494F5B;border-radius: 5px;background-color:#000000;color:#FFFFFF;
                font-size:15px;font-family:
            } 
            QLabel#Texts{
                font-family: "Arial Narrow", Arial, sans-serif; 
                font-size: 19px; font-style: normal;
                font-variant: normal; font-weight: 700; 
                line-height: 20.9px;padding-left:10px;
                border: 2px solid,#494F5B;border-radius: 5px;
                background-color:#000000;color:#FFFFFF;
                font-size:15px;font-family:
            }""")

        self.setWindowTitle("BOOK")
        self.setGeometry(615,200,650,544)
        self.Design()
        self.LeftPortion()
        self.show()

    def Design(self):
        self.PortionA=QLabel("",self)
        self.PortionB=QLabel("",self)
        self.PortionA.setPixmap(QPixmap("OOP_Python_GUI_Giya\Book-left.jpg"))
        self.PortionB.setPixmap(QPixmap("OOP_Python_GUI_Giya\Book-right.jpg"))
        self.PortionA.setGeometry(0,0,324.5,544)
        self.PortionB.setGeometry(324.5,0,326,544)
    def LeftPortion(self):
        self.DriverName=QLabel("Driver Namespace",self)
        self.DriverName.setGeometry(20,20,200,50)
        self.DriverName.setObjectName("Texts")
        self.LoyaltyLevel=QPushButton("Loyalty",self)
        self.LoyaltyLevel.setEnabled(False)
        self.Crown=QPixmap("OOP_Python_GUI_Giya\Loyal.ico")
        self.LoyaltyLevel.setIcon(QIcon(self.Crown))
        self.LoyaltyLevel.setIconSize(QSize(20,20))
        self.LoyaltyLevel.setGeometry(230,20,75,50)
        self.LoyaltyLevel.setStyleSheet("""
        border: 2px solid,#494F5B;border-radius: 5px;background-color:#000000;color:#FFFFFF;
        font-size:10px;padding-left:3px
        """)
        self.Profile=QLabel("",self)
        self.Profile.setGeometry(40,100,250,250)
        self.Profile.setObjectName("Image")
        self.Profile.setPixmap(QPixmap("OOP_Python_GUI_Giya\BlankIcon.png"))
        self.Profile.setScaledContents(True)
        self.Location=QLabel("LOCATION    ",self)
        self.Location.setObjectName("BottomText")
        self.Location.setGeometry(15,390,140,30)
        self.Location.setStyleSheet("""Font-size:13px;""")
        self.Date=QLabel("00/00/0000",self)
        self.Date.setObjectName("BottomText")
        self.Date.setGeometry(175,390,140,30)
        self.Date.setStyleSheet("border: 2px solid,#494F5B;border-radius: 5px;background-color:#000000;color:#FFFFFF;font-size:15px;font-family: ")
        
        self.Price=QLabel("Price: 0.00php",self)
        self.Price.setGeometry(100,445,120,30)
        self.Price.setStyleSheet("""
        border: 2px solid,#494F5B;border-radius: 5px;background-color:#000000;color:#FFFFFF;
        font-size:15px;font-family:
        """)
        self.Book=QPushButton("BOOK",self)
        self.Book.setGeometry(15,480,300,40)
        self.Book.setStyleSheet("""
        border: 2px solid,#494F5B;border-radius: 5px;background-color:#000000;color:#FFFFFF;
        font-size:15px;font-family:
        """)



class TourGuideUI(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        #1280x720
        self.setGeometry(300,150,1270,680)
        self.Test=QPushButton("This opens the book",self)
        self.Test.setGeometry(615,200,100,200)
        

    def BookPop(self):
        self.PopUp=BookPopUp(self)
        self.PopUp.show()

if __name__=='__main__':
    app=QApplication(sys.argv)
    ex=BookPopUp()
    sys.exit(app.exec_())