import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class TourGuideUI(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'GIYA - Customers UI'
        self.x = 250
        self.y = 125
        self.width = 1270
        self.height = 680
        self.Icon = "TGUIDE\Logo.png"
        self.setWindowTitle(self.title)
        self.resize(self.width, self.height)
        self.setFixedSize
        self.setWindowIcon(QIcon(self.Icon))
        self.imagePath = ""

        #profile details
        self.name = "Ivan Norvy Guzman"
        self.email = "qinbguzman@tip.edu.ph"
        self.location = "Marikina City, Metro Manila, Philippines"
        self.username = "qinbguzman"
        
        
        self.initUI()

    def initUI(self):
        self.menuBar()
        self.DashBoardButtons()
        self.RecentActivities()
        self.show()


    def DashBoardButtons(self):
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
        self.button1 = QPushButton("", self)
        self.button1.setIcon(QIcon("TGUIDE\Dashboard.png"))
        self.button1.setToolTip("Go to your DASHBOARD.")
        self.button1.setIconSize(QSize(60,60))
        self.button1.setGeometry(14,90,70,70)
        self.button1.setStyleSheet("background-color:transparent")
        #self.button3.clicked.connect(self.dashboardPage)
        self.textbox1 = QLabel("DASHBOARD", self)
        self.textbox1.setStyleSheet("font-family:arial;font-weight:bold;color:#F5F5F5")
        self.textbox1.move(16,160)
        #About Us Page
        self.button2 = QPushButton("", self)
        self.button2.setIcon(QIcon("TGUIDE\AboutUs.png"))
        self.button2.setToolTip("Know About Us.")
        self.button2.setIconSize(QSize(45,45))
        self.button2.setGeometry(25,500,50,50)
        self.button2.setStyleSheet("background-color:transparent")
        #self.button4.clicked.connect(self.aboutUsPage)
        self.textbox2 = QLabel("ABOUT US", self)
        self.textbox2.setStyleSheet("font-family:arial;font-weight:bold;color:white")
        self.textbox2.move(22,560)
        #Profile
        self.button3 = QPushButton("", self)
        self.button3.setIcon(QIcon("TGUIDE\profilePageico.png"))
        self.button3.setToolTip("Go to your Profile")
        self.button3.setIconSize(QSize(70,70))
        self.button3.setGeometry(10,195,80,80)
        self.button3.setStyleSheet("background-color:transparent")
        self.textbox3 = QLabel("PROFILE", self)
        self.textbox3.setStyleSheet("font-family:arial;font-weight:bold;color:white")
        self.textbox3.move(27,275)
        #History Events
        self.button4 = QPushButton("", self)
        self.button4.setIcon(QIcon("TGUIDE\historyEvents.png"))
        self.button4.setToolTip("Go to your Profile")
        self.button4.setIconSize(QSize(50,50))
        self.button4.setGeometry(20,315,60,60)
        self.button4.setStyleSheet("background-color:transparent")
        self.textbox3 = QLabel("ACTIVITIES", self)
        self.textbox3.setStyleSheet("font-family:arial;font-weight:bold;color:white")
        self.textbox3.move(20,380)
        #Sign Out 
        self.button5 = QPushButton("SIGN OUT", self)
        self.button5.setIcon(QIcon("TGUIDE\signOutico.png"))
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
        self.buttonPic = QPushButton("", self)
        self.buttonPic.setIcon(QIcon("TGUIDE\ProfileBlank.ico"))
        self.buttonPic.setIconSize(QSize(70,50))
        self.buttonPic.setGeometry(1200,0,70,60)
        #self.buttonPic.setStyleSheet("background-color:transparent")
        self.label = QLabel(self)
        self.label.setGeometry(1200,0,70,60)
        self.textboxUsername = QLabel(f"{self.username}", self)
        self.textboxUsername.move(1110,30)
        self.textboxUsername.setStyleSheet("font-family:arial;font-weight:bold;font-size:14px")
        self.textboxUsername1 = QLabel("Welcome to GIYA,", self)
        self.textboxUsername1.move(1110,10)

    def profilePage(self):
        #profile picture 
        self.buttonUploadPic = QPushButton("", self)
        self.buttonUploadPic.setIcon(QIcon("TGUIDE\ProfileBlank.ico"))
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
        #Recent Activities
        self.dashActivities = QLabel(self)
        self.dashActivities.setStyleSheet("background-color:#415886;border: 0px 1px 0px 0px outset #666e7f")
        self.dashActivities.setGeometry(140,250,400,200)

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
    def RecentActivities(self):
        self.setStyleSheet("""
        QWidget{
            color:#F8F8FF
        }
        """)
        self.NameHeader=QLabel(self.name.upper()+"'s"+" Activity log",self)
        self.NameHeader.setGeometry(143,20,300,28)
        self.NameHeader.setStyleSheet("color:#000000")
        self.ActivityHeader=QLabel("RECENT ACTIVITIES",self)
        self.ActivityHeader.setGeometry(140,80,295,30)
        self.ActivityHeader.setStyleSheet("""color:#000000;font-family: Century Gothic; font-size: 30px; font-style: normal; font-variant: normal; font-weight: 700; line-height: 15px;
                                              padding-left:5px;color:#000000;background-color:Transparent;
                                              border: 2px solid #494F5B;border-width:0px 0px 2px 0px;""")
#------------------ACTIVITY         1--------------------------------------------------------------------------------

        self.A1Border=QLabel("",self)
        self.A1Border.setGeometry(140,120,1100,200)
        self.A1Border.setStyleSheet("border: 2px solid #5E7E58;background-color:#F8F8FF")
        self.Activity1=QLabel("ACTIVITY 1", self)
        self.Activity1.setGeometry(140,120,75,199)
        self.Activity1.setStyleSheet("""padding-left:5px;color:#000000;background-color:#AAB1BB;
                                        border: 2px solid #5E7E58;border-width:50px 3px 50px 3px;""")
        self.TextBoxD1=QLabel("EVENT NAME HERE "+ "\n\n\n\n"+"CUSTOMER NAME HERE"+"\n\n"+"EVENT DATE HERE"+"\n\n""EVENT RATING HERE",self)
        self.TextBoxD1.setGeometry(230,86,250,250)
        self.TextBoxD1.setStyleSheet("color:#000000;font-size:15px;font-family:Arial;")
        self.FestivalBoxD1=QLabel("",self)
        self.FestivalImage1=QPixmap("TGUIDE\Magayon.1.jpg")
        self.FestivalBoxD1.setGeometry(588,122,650,196)
        self.FestivalBoxD1.setPixmap(self.FestivalImage1)
        self.FestivalBoxD1.setScaledContents(True)
        self.HistoButton1=QPushButton("View Details",self)
        self.HistoButton1.setStyleSheet("background-color:#5E7E58")
        self.HistoButton1.setGeometry(400,270,180,40)

#------------------ACTIVITY         2----------------------------------------------------------------------------------------------

        self.A2Border=QLabel("",self)
        self.A2Border.setGeometry(140,330,1100,170)
        self.A2Border.setStyleSheet("border: 2px solid #7EA57F;background-color:#F8F8FF")
        self.Activity2=QLabel("ACTIVITY 2", self)
        self.Activity2.setGeometry(140,332,75,168)
        self.Activity2.setStyleSheet("""padding-left:5px;color:#000000;background-color:#BBC1C9;
                                        border: 2px solid #7EA57F;border-width:40px 3px 40px 3px;""")

        self.TextBoxD2=QLabel("\nEVENT NAME HERE "+ "\n\n\n"+"CUSTOMER NAME HERE"+"\n\n"+"EVENT DATE HERE"+"\n\n""EVENT RATING HERE",self)
        self.TextBoxD2.setGeometry(230,330,250,150)
        self.TextBoxD2.setStyleSheet("color:#000000;font-size:15px;font-family:Arial;")
        self.FestivalBoxD2=QLabel("",self)
        self.FestivalImage2=QPixmap("TGUIDE\Festival Pics\Malatarlak Festival.3.jpg")
        self.FestivalBoxD2.setGeometry(588,332,650,166)
        self.FestivalBoxD2.setPixmap(self.FestivalImage2)
        self.FestivalBoxD2.setScaledContents(True)
        self.HistoButton2=QPushButton("View Details",self)
        self.HistoButton2.setStyleSheet("background-color:#7EA57F")
        self.HistoButton2.setGeometry(400,450,180,40)
#------------------ACTIVITY         3----------------------------------------------------------------------------------------------

        self.A3Border=QLabel("",self)
        self.A3Border.setGeometry(140,511,1100,169)
        self.A3Border.setStyleSheet("border: 2px solid #A2BEA7;background-color:#F8F8FF")
        self.Activity3=QLabel("ACTIVITY 3", self)
        self.Activity3.setGeometry(140,513,75,167)
        self.Activity3.setStyleSheet("""padding-left:5px;color:#000000;background-color:#C9CED4;
                                        border: 2px solid #A2BEA7;border-width:40px 3px 40px 3px;""")
        self.TextBoxD3=QLabel("\nEVENT NAME HERE "+ "\n\n\n"+"CUSTOMER NAME HERE"+"\n\n"+"EVENT DATE HERE"+"\n\n""EVENT RATING HERE",self)
        self.TextBoxD3.setGeometry(230,513,250,150)
        self.TextBoxD3.setStyleSheet("color:#000000;font-size:15px;font-family:Arial;")
        self.FestivalBoxD3=QLabel("",self)
        self.FestivalImage3=QPixmap("TGUIDE\Festival Pics\DRAWER.jpg")
        self.FestivalBoxD3.setGeometry(588,513,650,165)
        self.FestivalBoxD3.setPixmap(self.FestivalImage3)
        self.FestivalBoxD3.setScaledContents(True)
        self.HistoButton3=QPushButton("View Details",self)
        self.HistoButton3.setStyleSheet("background-color:#A2BEA7")
        self.HistoButton3.setGeometry(400,630,180,40)
#-----------------------------------------------------------------------------------------------------------------
#executes the application
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = TourGuideUI()
    sys.exit(app.exec_())