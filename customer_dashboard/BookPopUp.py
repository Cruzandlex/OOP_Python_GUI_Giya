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
                border:3px solid #1E90FF;border-radius:75px;font-family: "Arial Narrow", Arial, sans-serif;
            }
            QLabel#BottomText{
                border: 2px solid,#494F5B;border-radius: 5px;background-color:#000000;color:#FFFFFF;
                font-size:15px;font-family: "Arial Narrow", Arial, sans-serif;
            } 
            QLabel#Texts{
                font-family: "Arial"; 
                font-size: 19px; font-style: normal; font-weight: 700;background-color: rgba(0, 0, 0, 0.5);
                color:#FFFFFF; qproperty-alignment: AlignCenter;border-radius:10px;border-style:outset;
                border-width:1px;border-color:#808080
            }
            QLabel#NoBg{
                background-color:transparent
            }
            """)

        self.userData={"username":"zandlex","password":"admin","role":"U","msg": ["hello",'hi'],"pending":[],"acc":{"name":"Zandlex Keano M. Cruz","age":"19","sex":
        "Male","EmailAd":"Qzkmcruz@tip.edu.ph","started":"November 26, 2000","FavoriteLoc":"Region V","TotalTours":"0","contact":"09560594126","aboutme":
        "I have no bio data yet to show the people"}}
        self.setWindowTitle("BOOK")
        self.resize(750,550)
        self.setFixedSize
        self.Design()
        self.BookLeftWindow()
        self.BookRightWindow()
        self.show()

    def Design(self):
        '''
        self.backgroundPopUp = QLabel(self)
        self.backgroundPopUp.setStyleSheet("background: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 #A3B6C2, stop:1 #5BC7D7)")
        self.backgroundPopUp.setGeometry(0,0,750,550)
        '''
        self.bg1 = QLabel(self)
        self.bg1.setPixmap(QPixmap("Book-right2.jpg"))
        self.bg1.setGeometry(0,0,330,550)
        self.bg1.setScaledContents(True)

        self.bg2 = QLabel(self)
        self.bg2.setPixmap(QPixmap("Book-left.jpg"))
        self.bg2.setGeometry(330,0,420,550)
        self.bg2.setScaledContents(True)
        
    def BookLeftWindow(self):
        self.Profile = QLabel(self)
        self.Profile.setGeometry(90,10,150,150)
        self.Profile.setObjectName("Image")
        self.Profile.setPixmap(QPixmap("BlackIcon.png"))
        self.Profile.setScaledContents(True)

        self.tourguideName = QLabel(self.userData['acc']['name'], self)
        self.tourguideName.setGeometry(15,165,300,50)
        self.tourguideName.setObjectName("Texts")

        self.NoStar = QPixmap("StarBlack.png")
        self.Star=QPixmap("StarYellow.png")#2B2F36 canvas (Darker)
        self.RatingStar1 = QLabel("",self)
        self.RatingStar2 = QLabel("",self)
        self.RatingStar3 = QLabel("",self)
        self.RatingStar4 = QLabel("",self)
        self.RatingStar5 = QLabel("",self)
        self.RatingStar1.setGeometry(90,220,27,25)
        self.RatingStar2.setGeometry(120,220,27,25)
        self.RatingStar3.setGeometry(150,220,27,25)
        self.RatingStar4.setGeometry(180,220,27,25)
        self.RatingStar5.setGeometry(210,220,27,25)
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

        self.skillsDescript = QLabel("SKILLS DESCRIPTION", self)
        self.skillsText = QLabel(self.userData['acc']['aboutme'], self)
        self.skillsDescript.setStyleSheet("background-color: rgba(0, 0, 0, 0.5);color:#FFFFFF; qproperty-alignment: AlignTop;padding:5px;border-radius:10px;border-style:outset;border-width:1px;border-color:#808080;font-family:arial;font-size:16px;font-weight:bold")
        self.skillsDescript.setGeometry(15,260,300,280)
        self.skillsText.setStyleSheet("background-color:transparent;color:#FFFFFF; qproperty-alignment: AlignTop;padding:5px;border-radius:10px;font-family:arial;font-size:14px;font-weight:bold")
        self.skillsText.setGeometry(15,290,300,250)
        self.skillsText.setWordWrap(True)

        self.skillsDescriptIcon = QLabel(self)
        self.skillsDescriptIcon.setPixmap(QPixmap("skillsDes.png"))
        self.skillsDescriptIcon.setGeometry(201,263,25,25)
        self.skillsDescriptIcon.setStyleSheet("background-color:transparent")
        self.skillsDescriptIcon.setScaledContents(True)

        self.horizontalLine1 = QLabel(self)
        self.horizontalLine1.setStyleSheet("background-color: rgba(255, 255, 255, 0.5);color:#FFFFFF")
        self.horizontalLine1.setGeometry(15,290,300,2)

    def BookRightWindow(self):
        self.packageOffer = QLabel("PACKAGE OFFERS", self)
        self.packageText = QLabel(self.userData['acc']['aboutme'], self)
        self.packageOffer.setStyleSheet("background-color: rgba(0, 0, 0, 0.5);color:#FFFFFF; qproperty-alignment: AlignTop;padding:5px;border-style:outset;border-width:1px;border-color:#808080;border-radius:10px;font-family:arial;font-size:16px;font-weight:bold")
        self.packageOffer.setGeometry(345,15,390,220)
        self.packageText.setStyleSheet("background-color:transparent;color:#FFFFFF; qproperty-alignment: AlignTop;padding:5px;border-radius:10px;font-family:arial;font-size:14px;font-weight:bold")
        self.packageText.setGeometry(345,50,390,185)
        self.packageText.setWordWrap(True)

        self.packageOfferIcon = QLabel(self)
        self.packageOfferIcon.setPixmap(QPixmap("packOff.png"))
        self.packageOfferIcon.setGeometry(510,18,25,25)
        self.packageOfferIcon.setStyleSheet("background-color:transparent")
        self.packageOfferIcon.setScaledContents(True)

        self.horizontalLine2 = QLabel(self)
        self.horizontalLine2.setStyleSheet("background-color: rgba(255, 255, 255, 0.5);color:#FFFFFF")
        self.horizontalLine2.setGeometry(345,45,390,2)

        self.festInfo = QLabel("BOOKING INFO", self)
        self.festInfo.setStyleSheet("background-color: rgba(0, 0, 0, 0.5);color:#FFFFFF; qproperty-alignment: AlignTop;padding:5px;border-style:outset;border-width:1px;border-color:#808080;border-radius:10px;font-family:arial;font-size:16px;font-weight:bold")
        self.festInfo.setGeometry(345,250,390,220)

        self.horizontalLine3 = QLabel(self)
        self.horizontalLine3.setStyleSheet("background-color: rgba(255, 255, 255, 0.5);color:#FFFFFF")
        self.horizontalLine3.setGeometry(345,280,390,2)

        self.festInfoIcon = QLabel(self)
        self.festInfoIcon.setPixmap(QPixmap("bookInfo.png"))
        self.festInfoIcon.setStyleSheet("background-color:transparent")
        self.festInfoIcon.setGeometry(475,252,28,28)
        self.festInfoIcon.setScaledContents(True)

        self.festImage = QLabel(self)
        self.festImage.setPixmap(QPixmap("malasimboF.jpg"))
        self.festImage.setGeometry(355,300,200,150)
        self.festImage.setStyleSheet("background-color:black;border-style:outset;border-width:1px;border-color:#F0FFFF")
        self.festImage.setScaledContents(True)

        self.festNameInfo = QLabel('FESTIVAL NAME',self)
        self.festNameInfo.setStyleSheet("background-color:transparent;color:white;font-family:arial;font-size:14px;font-weight:Bold")
        self.festNameInfo.setGeometry(560,315,170,35)
        self.festNameInfo.setWordWrap(True)
        self.festLocInfo = QLabel('LOCATION',self)
        self.festLocInfo.setStyleSheet("background-color:transparent;color:white;font-family:arial;font-size:14px;font-weight:Bold")
        self.festLocInfo.setGeometry(560,355,170,35)
        self.festLocInfo.setWordWrap(True)
        self.festDateInfo = QLabel('DATE AND TIME',self)
        self.festDateInfo.setStyleSheet("background-color:transparent;color:white;font-family:arial;font-size:14px;font-weight:Bold")
        self.festDateInfo.setGeometry(560,395,170,35)
        self.festDateInfo.setWordWrap(True)

        self.bookButton = QPushButton("BOOK", self)
        self.bookButton.setIcon(QIcon("check.png"))
        self.bookButton.setIconSize(QSize(25,25))
        self.bookButton.setStyleSheet("background: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 #A3B6C2, stop:1 #5BC7D7);color:#001a33;font-family:arial;font-size:16px;font-weight:bold;border-radius:10px;border-width:2px;border-color:#4dff88;border-style:outset")
        self.bookButton.setGeometry(565,485,150,50)

        self.Price = QLabel("Price "+"  "+'PHP'+" "+"800.00", self)
        self.Price.setStyleSheet("background: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 #A3B6C2, stop:1 #5BC7D7);color:#001a33;font-family:arial;font-size:16px;font-weight:bold;border-radius:10px;border-width:2px;border-color:#b3d9ff;border-style:outset")
        self.Price.setGeometry(360,485,200,50)

        self.verticalLine = QLabel(self)
        self.verticalLine.setStyleSheet("background-color:white")
        self.verticalLine.setGeometry(408,487,2,47)

    def BookPop(self):
        self.PopUp = BookPopUp(self)
        self.PopUp.show()

if __name__=='__main__':
    app=QApplication(sys.argv)
    ex=BookPopUp()
    sys.exit(app.exec_())