import sys
from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *



class BookPopUp(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.setStyleSheet("""
        
            QPushButton#Pressable{
                border: 2px solid,#494F5B;border-radius: 5px;background-color:#000000;color:#FFFFFF;
                 font-size:15px;font-family: "Arial Narrow", Arial, sans-serif;
                }
            QPushButton#Pressable:hover{
                
                }
            QPushButton#Pressable:pressed{
                background-color:#000000;color:#FFFFFF;
                }
            QWidget{
                background-color:#FFFFFF
            }
            QLabel#Image{
                border: 4px solid, #000000;
                border-radius:124;font-family: "Arial Narrow", Arial, sans-serif;
            }
            QLabel#BottomText{
                border: 2px solid,#494F5B;border-radius: 5px;background-color:#000000;color:#FFFFFF;
                font-size:15px;font-family: "Arial Narrow", Arial, sans-serif;
            } 
            QLabel#Texts{
                font-family: "Arial Narrow", Arial, sans-serif; 
                font-size: 19px; font-style: normal; font-weight: 700;padding-left:10px;
                border: 2px solid,#494F5B;border-radius: 5px;
                background-color:#000000;color:#FFFFFF;
            }
            QLabel#NoBg{
                background-color:transparent
            }
            """)

        self.setWindowTitle("BOOK")
        self.setGeometry(615,200,650,544)
        self.Design()
        self.LeftPortion()
        self.RightPortion()
        self.show()

    def Design(self):
        self.PortionA=QLabel("",self)
        self.PortionB=QLabel("",self)
        self.PortionA.setPixmap(QPixmap("OOP_Python_GUI_Giya\Book-left.jpg"))
        self.PortionB.setPixmap(QPixmap("OOP_Python_GUI_Giya\Book-right2.jpg"))
        self.PortionA.setGeometry(0,0,324.5,544)
        self.PortionB.setGeometry(324.5,0,326,544)
    def LeftPortion(self):
        self.DriverName=QLabel("TOURGUIDE NAME",self)
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
        self.Price.setObjectName("Texts")
        self.Price.setStyleSheet("border: 2px solid,#494F5B;border-radius: 5px;background-color:#000000;color:#FFFFFF;padding-left:1px")
        self.Book=QPushButton("BOOK",self)
        self.Book.setGeometry(15,480,300,40)
        self.Book.setStyleSheet("""
        border: 2px solid,#494F5B;border-radius: 5px;background-color:#000000;color:#FFFFFF;
        font-size:15px;font-family:
        """)
    def RightPortion(self):
        self.PackageHeader=QLabel("Packaged offers ",self)
        self.PackageHeader.setObjectName("Texts")
        self.PackageHeader.setGeometry(370,20,250,30)
        self.PackageHeader.setStyleSheet("Font-Size:23px;padding-left:45px; border: 2px solid,#494F5B;border-radius: 5px;background-color:#000000;color:#FFFFFF;")
        self.SkillHeader=QLabel("Skills description ",self)
        self.SkillHeader.setObjectName("Texts")
        self.SkillHeader.setStyleSheet("Font-Size:23px;padding-left:45px; border: 2px solid,#494F5B;border-radius: 5px;background-color:#000000;color:#FFFFFF;")
        self.SkillHeader.setGeometry(370,170,250,30)
        self.Ratings=QLabel("Rating: ",self)
        self.Ratings.setObjectName("Texts")
        self.Ratings.setStyleSheet("Font-Size:23px;padding-left:20px; border: 2px solid,#494F5B;border-radius: 5px;background-color:#FFFFFF;color:#000000;")
        self.Ratings.setGeometry(370,308,250,30)
        self.NoStar=QPixmap("OOP_Python_GUI_Giya\StarBlack.png")
        self.Star=QPixmap("OOP_Python_GUI_Giya\StarYellow1.png")#2B2F36 canvas (Darker)

        self.RatingStar1=QLabel("",self)
        self.RatingStar2=QLabel("",self)
        self.RatingStar3=QLabel("",self)
        self.RatingStar4=QLabel("",self)
        self.RatingStar5=QLabel("",self)
        self.RatingStar1.setGeometry(465,310,27,25)
        self.RatingStar2.setGeometry(495,310,27,25)
        self.RatingStar3.setGeometry(525,310,27,25)
        self.RatingStar4.setGeometry(555,310,27,25)
        self.RatingStar5.setGeometry(585,310,27,25)
        self.RatingStar1.setPixmap(self.Star)
        self.RatingStar2.setPixmap(self.Star)
        self.RatingStar3.setPixmap(self.Star)
        self.RatingStar4.setPixmap(self.Star)
        self.RatingStar5.setPixmap(self.NoStar)
        self.RatingStar1.setScaledContents(True)
        self.RatingStar2.setScaledContents(True)
        self.RatingStar3.setScaledContents(True)
        self.RatingStar4.setScaledContents(True)
        self.RatingStar5.setScaledContents(True)
        self.RatingStar1.setObjectName("NoBg")
        self.RatingStar2.setObjectName("NoBg")
        self.RatingStar3.setObjectName("NoBg")
        self.RatingStar4.setObjectName("NoBg")
        self.RatingStar5.setObjectName("NoBg")
#--------------------------------------------------
        self.Picture1=QPixmap("OOP_Python_GUI_Giya\Ibalong.1.jpg")
        self.Picture2=QPixmap("OOP_Python_GUI_Giya\Katalingkasan.1.jpg")
        self.Tour1=QLabel("",self)
        self.Tour1.setGeometry(345,360,290,170)
        self.Tour1.setStyleSheet("border: 5px outset #2B2F36")
        self.Tour1.setPixmap(self.Picture1)
        self.Tour1.setScaledContents(True)
        #self.Tour2=QLabel("",self)
        #self.Tour2.setGeometry(500,360,135,170)
        #self.Tour2.setPixmap(self.Picture2)
        #self.Tour2.setScaledContents(True)


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