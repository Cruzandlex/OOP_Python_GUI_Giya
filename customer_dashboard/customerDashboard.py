import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class mainUserUI(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'GIYA - Customers UI'
        self.x = 0
        self.y = 0
        self.width = 1270
        self.height = 680
        self.Icon = "appLogoico.png"
        self.setWindowTitle(self.title)
        self.setGeometry(self.x, self.y, self.width, self.height)
        self.setWindowIcon(QIcon(self.Icon))

        #profile details
        self.name = "Ivan Norvy Guzman"
        self.email = "qinbguzman@tip.edu.ph"
        self.location = "Marikina City, Metro Manila, Philippines"

        self.initUI()
        self.menuBar()
        self.profilePage()
        self.show()

    def initUI(self):
        self.backgroudTaskbar = QLabel(self)
        self.backgroudTaskbar.setStyleSheet("background-color:#494F5B;border: 0px 1px 0px 0px outset #666e7f")
        self.backgroudTaskbar.setGeometry(0,0,100,680)
        self.lineTaskbar1 = QLabel(self)
        self.lineTaskbar1.setStyleSheet("background-color:#2d3139")
        self.lineTaskbar1.setGeometry(0,60,100,2)
        self.backgroudLogo = QLabel(self)
        self.backgroudLogo.setStyleSheet("background-color:#d5d7dd")
        self.backgroudLogo.setGeometry(0,0,100,60)
        self.lineTaskbar = QLabel(self)
        self.lineTaskbar.setStyleSheet("background-color:#aaafbb")
        self.lineTaskbar.setGeometry(100,60,1280,2)
        self.backgroudBar = QLabel(self)
        self.backgroudBar.setStyleSheet("background-color:#f1f2f4;border: 1px outset #c6cad2")
        self.backgroudBar.setGeometry(100,0,1100,60)
        self.logo = QLabel(self)
        self.logo.resize(50,50)
        self.logo.move(22,5)
        self.pixmap = QPixmap(self.Icon)
        self.logo.setPixmap(QPixmap(self.pixmap))
        self.logo.setScaledContents(True)
        #Taskbar Buttons
        #Dashboard Page
        self.button3 = QPushButton("", self)
        self.button3.setIcon(QIcon("dashboardico.ico"))
        self.button3.setToolTip("Go to your DASHBOARD.")
        self.button3.setIconSize(QSize(50,50))
        self.button3.setGeometry(18,90,60,60)
        self.button3.setStyleSheet("background-color:transparent")
        #self.button3.clicked.connect(self.dashboardPage)
        self.textbox3 = QLabel("DASHBOARD", self)
        self.textbox3.setStyleSheet("font-family:arial;font-weight:bold;color:#F5F5F5")
        self.textbox3.move(16,160)
        #settings menu bar
        self.buttonSettings = QPushButton("", self)
        self.buttonSettings.setIcon(QIcon("settingico.ico"))
        self.buttonSettings.setIconSize(QSize(70,70))
        self.buttonSettings.setGeometry(15,190,70,70)
        self.buttonSettings.clicked.connect(self.settingsPage)
        self.buttonSettings.setStyleSheet("background-color:transparent")
        self.textbox3 = QLabel("SETTINGS", self)
        self.textbox3.setStyleSheet("font-family:arial;font-weight:bold;color:#F5F5F5")
        self.textbox3.move(22,265)
        #About Us Page
        self.button4 = QPushButton("", self)
        self.button4.setIcon(QIcon("aboutUsico.ico"))
        self.button4.setToolTip("Know About Us.")
        self.button4.setIconSize(QSize(45,45))
        self.button4.setGeometry(25,340,50,50)
        self.button4.setStyleSheet("background-color:transparent")
        #self.button4.clicked.connect(self.aboutUsPage)
        self.textbox4 = QLabel("ABOUT US", self)
        self.textbox4.setStyleSheet("font-family:arial;font-weight:bold;color:white")
        self.textbox4.move(22,400)
        #Sign Out 
        self.button5 = QPushButton("SIGN OUT", self)
        self.button5.setIcon(QIcon("signOutico.ico"))
        self.button5.setToolTip("Sign Out.")
        self.button5.setIconSize(QSize(30,30))
        self.button5.move(3,620)
        self.button5.resize(90,30)
        self.button5.setStyleSheet("background-color:transparent;color:white")
        #self.button5.clicked.connect(self.signOut)

    def menuBar(self):
        self.textDash = QLabel("Dashboard", self)
        self.textDash.move(130,15)
        self.textDash.setStyleSheet("font-family:century gothic;font-size:24px")
        self.taskBarButton = QPushButton("", self)
        self.taskBarButton.setIcon(QIcon("taskBar.png"))
        self.taskBarButton.setIconSize(QSize(30,30))
        self.taskBarButton.setGeometry(270,12,40,40)
        self.taskBarButton.setStyleSheet("background-color:transparent")
        self.styleChoice = QLabel("Window")
        self.buttonUploadPic = QPushButton("", self)
        self.buttonUploadPic.setIcon(QIcon("uploadImageico.ico"))
        self.buttonUploadPic.setIconSize(QSize(70,50))
        self.buttonUploadPic.setGeometry(1200,0,70,60)
        self.buttonUploadPic.setStyleSheet("background-color:transparent")
        self.messageButton = QPushButton("", self)
        self.messageButton.setIcon(QIcon("message.png"))
        self.messageButton.setIconSize(QSize(40,40))
        self.messageButton.setGeometry(1140,5,50,50)
        self.messageButton.setStyleSheet("background-color:transparent")

    def profilePage(self):
        #profile picture 
        self.buttonUploadPic = QPushButton("", self)
        self.buttonUploadPic.setIcon(QIcon("uploadImageico.ico"))
        self.buttonUploadPic.setIconSize(QSize(110,110))
        self.buttonUploadPic.resize(120,120)
        self.buttonUploadPic.move(140,80)
        self.buttonUploadPic2 = QPushButton("Upload image", self)
        self.buttonUploadPic2.resize(120,25)
        self.buttonUploadPic2.move(140,200)
        self.buttonUploadPic.clicked.connect(self.uploadProfilePic)
        self.buttonUploadPic2.clicked.connect(self.uploadProfilePic)
        self.label = QLabel(self)
        self.label.setGeometry(140,80,120,120)
        #profile details
        self.prfName = QLabel(f"{self.name}", self)
        self.prfName.resize(300,28)
        self.prfName.move(290,98)
        self.prfName.setStyleSheet("font-family:arial;font:bold;font-size:26px")
        self.prfEmail = QLabel(f"{self.email}", self)
        self.prfEmail.resize(300,17)
        self.prfEmail.move(290,130)
        self.prfEmail.setStyleSheet("font-family:arial;font-size:14px")
        self.prfLocation = QLabel(f"{self.location}", self)
        self.prfLocation.resize(300,17)
        self.prfLocation.move(290,158)
        self.prfLocation.setStyleSheet("font-family:arial;font-size:14px")

    def settingsPage(self):
        #not yet functioning (new window function)
        self.initUI()
        self.menuBar()
        self.show()
        self.buttonSettings.setStyleSheet("background-color:white;color:black;border-width:1px;border-style:outset;border-radius:5px;border-color:black;font:bold 12px")
        self.settings = QLabel("Welcome to Settings", self)
        self.settings.resize(300,10)
        self.settings.move(300,300)

    def uploadProfilePic(self):
        self.image = QFileDialog.getOpenFileName(self,'Open File','c\\','image file(*.jpg)')
        self.imagePath = self.image[0]
        self.pixmap = QPixmap(self.imagePath)
        self.label.setPixmap(QPixmap(self.pixmap))
        self.label.setScaledContents(True)


#executes the application
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = mainUserUI()
    sys.exit(app.exec_())