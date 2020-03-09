import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class mainUserUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'GIYA - Customers UI'
        self.x = 500
        self.y = 100
        self.width = 750
        self.height = 600
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
        #Pagetask Buttons
        #Profile Page
        self.button1 = QPushButton("", self)
        self.button1.setIcon(QIcon("profileico.ico"))
        self.button1.setToolTip("Go to your PROFILE.")
        self.button1.setIconSize(QSize(100,100))
        self.button1.move(10,10)
        self.button1.resize(100,100)
        self.button1.setStyleSheet("background-color:transparent")
        #self.button1.clicked.connect(self.profilePage)
        self.textbox1 = QLabel("PROFILE", self)
        self.textbox1.setStyleSheet("font-family:arial;font-weight:bold")
        self.textbox1.move(40,105)
        #Home Page
        self.button2 = QPushButton("", self)
        self.button2.setIcon(QIcon("homeico.ico"))
        self.button2.setToolTip("Go to HOME page.")
        self.button2.setIconSize(QSize(50,50))
        self.button2.move(11*3,10*15)
        self.button2.resize(50,50)
        self.button2.setStyleSheet("background-color:transparent")
        #self.button2.clicked.connect(self.homePage)
        self.textbox2 = QLabel("HOME", self)
        self.textbox2.setStyleSheet("font-family:arial;font-weight:bold")
        self.textbox2.move(45,100*2)
        #Dashboard Page
        self.button3 = QPushButton("", self)
        self.button3.setIcon(QIcon("dashboardico.ico"))
        self.button3.setToolTip("Go to your DASHBOARD.")
        self.button3.setIconSize(QSize(45,45))
        self.button3.move(12*3,10*25)
        self.button3.resize(50,50)
        self.button3.setStyleSheet("background-color:transparent")
        #self.button3.clicked.connect(self.dashboardPage)
        self.textbox3 = QLabel("DASHBOARD", self)
        self.textbox3.setStyleSheet("font-family:arial;font-weight:bold")
        self.textbox3.move(30,100*3)
        #About Us Page
        self.button4 = QPushButton("", self)
        self.button4.setIcon(QIcon("aboutUsico.ico"))
        self.button4.setToolTip("Know About Us.")
        self.button4.setIconSize(QSize(45,45))
        self.button4.move(12*3,10*35)
        self.button4.resize(50,50)
        self.button4.setStyleSheet("background-color:transparent")
        #self.button4.clicked.connect(self.aboutUsPage)
        self.textbox4 = QLabel("ABOUT US", self)
        self.textbox4.setStyleSheet("font-family:arial;font-weight:bold")
        self.textbox4.move(34,100*4)
        #Sign Out 
        self.button5 = QPushButton("SIGN OUT", self)
        self.button5.setIcon(QIcon("signOutico.ico"))
        self.button5.setToolTip("Sign Out.")
        self.button5.setIconSize(QSize(30,30))
        self.button5.move(12,10*55)
        self.button5.resize(90,30)
        self.button5.setStyleSheet("background-color:transparent")
        #self.button5.clicked.connect(self.signOut)

    def menuBar(self):
        #profile menu bar 
        self.buttonProfile = QPushButton("PROFILE", self)
        self.buttonProfile.setIcon(QIcon("profileDashico.ico"))
        self.buttonProfile.setIconSize(QSize(50,50))
        self.buttonProfile.resize(200,50)
        self.buttonProfile.move(150,5)
        self.buttonProfile.clicked.connect(self.profilePage)
        
        #activities menu bar
        self.buttonActivities = QPushButton("ACTIVITIES", self)
        self.buttonActivities.setIcon(QIcon("activitiesico.ico"))
        self.buttonActivities.setIconSize(QSize(35,35))
        self.buttonActivities.resize(200,50)
        self.buttonActivities.move(350,5)

        #settings menu bar
        self.buttonSettings = QPushButton("SETTINGS", self)
        self.buttonSettings.setIcon(QIcon("settingico.ico"))
        self.buttonSettings.setIconSize(QSize(50,50))
        self.buttonSettings.resize(200,50)
        self.buttonSettings.move(550,5)
        self.buttonSettings.clicked.connect(self.settingsPage)
    
    def profilePage(self):
        self.buttonProfile.setStyleSheet("background-color:white;color:black;border-width:1px;border-style:outset;border-radius:5px;border-color:black;font:bold 12px")
        #profile picture 
        self.buttonUploadPic = QPushButton("", self)
        self.buttonUploadPic.setIcon(QIcon("uploadImageico.ico"))
        self.buttonUploadPic.setIconSize(QSize(100,100))
        self.buttonUploadPic.resize(100,100)
        self.buttonUploadPic.move(170,80)
        self.buttonUploadPic2 = QPushButton("Upload image", self)
        self.buttonUploadPic2.resize(100,25)
        self.buttonUploadPic2.move(170,180)
        self.buttonUploadPic.clicked.connect(self.uploadProfilePic)
        self.buttonUploadPic2.clicked.connect(self.uploadProfilePic)
        self.label = QLabel(self)
        self.label.setGeometry(0,0,100,100)
        self.label.move(170,80)
        #profile details
        self.prfName = QLabel(f"{self.name}", self)
        self.prfName.resize(300,28)
        self.prfName.move(300,88)
        self.prfName.setStyleSheet("font-family:arial;font:bold;font-size:26px")
        self.prfEmail = QLabel(f"{self.email}", self)
        self.prfEmail.resize(300,17)
        self.prfEmail.move(300,120)
        self.prfEmail.setStyleSheet("font-family:arial;font-size:14px")
        self.prfLocation = QLabel(f"{self.location}", self)
        self.prfLocation.resize(300,17)
        self.prfLocation.move(300,148)
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