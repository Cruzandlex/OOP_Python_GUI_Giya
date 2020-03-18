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
        self.profilePage()
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
        self.logo.setGeometry(22,5,50,50)
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
        self.buttonUploadPic.setGeometry(140,80,120,120)
        self.buttonUploadPic2 = QPushButton("Upload image", self)
        self.buttonUploadPic2.setGeometry(140,200,120,25)
        self.buttonUploadPic.clicked.connect(self.uploadProfilePic)
        self.buttonUploadPic2.clicked.connect(self.uploadProfilePic)
        self.label = QLabel(self)
        self.label.setGeometry(140,80,120,120)
        #profile details
        self.prfName = QLabel(f"{self.name}", self)
        self.prfName.setGeometry(290,98,300,28)
        self.prfName.setStyleSheet("font-family:arial;font:bold;font-size:26px")
        self.prfEmail = QLabel(f"{self.email}", self)
        self.prfEmail.setGeometry(290,130,300,17)
        self.prfEmail.setStyleSheet("font-family:arial;font-size:14px")
        self.prfLocation = QLabel(f"{self.location}", self)
        self.prfLocation.setGeometry(290,158,300,17)
        self.prfLocation.setStyleSheet("font-family:arial;font-size:14px")
#------------------------Left Portion---------------------------------------------------------------

        self.ProfileBio = QLabel(self)
        self.ProfileBio.setStyleSheet("background-color:#FFFFFF;border 0px 1px 0px 0px outset #666e7f;border-radius:20px;")
        self.ProfileBio.setGeometry(140,250,420,400)
        self.BioIcon=QLabel(self)
        self.BioIcon.setPixmap(QPixmap("customer_dashboard\AboutMe.png"))
        self.BioIcon.setScaledContents(True)
        self.BioIcon.setGeometry(145,255,50,50)
        self.BioIcon.setStyleSheet("background-color:Transparent")
        self.BioHeader=QLabel("About Me",self)
        self.BioHeader.setGeometry(140,255,420,60)
        self.BioHeader.setStyleSheet("""color:#000000;font-family: Arial; font-size: 20px; font-style: normal; font-variant: normal; font-weight: 700; line-height: 15px;
                                              padding-left:160px;color:#000000;background-color:Transparent;
                                              border: 2px solid #494F5B;border-width:0px 0px 2px 0px;""")
        self.BioText=QLabel("You can edit this text.",self)
        self.BioText.setWordWrap(True)
        self.BioText.setGeometry(150,330,380,290)
        self.BioText.setStyleSheet("background-color:transparent")
#----------------------------Right Portion-----------------------------------------------------------
        self.RightPartLayout=QLabel(self)
        self.RightPartLayout.setGeometry(600,62,700,700)
        self.RightPartLayout.setStyleSheet("Background-color:#CFD0D3")
        self.BiodataBox = QLabel(self)
        self.BiodataBox.setStyleSheet("background-color:#FFFFFF;border 0px 1px 0px 0px outset #666e7f;border-radius:20px;")
        self.BiodataBox.setGeometry(637,200,600,450)
        self.BiodataLogo=QLabel("",self)
        self.BiodataLogo.setScaledContents(True)
        self.BiodataLogo.setPixmap(QPixmap("customer_dashboard\Biodata.png"))
        self.BiodataLogo.setGeometry(645,200,50,50)
        self.BiodataHeader=QLabel(self.name.upper()+"'s "+"Bio data",self)
        self.BiodataHeader.setGeometry(637,200,600,60)
        self.BiodataHeader.setStyleSheet("""color:#000000;font-family: Arial; font-size: 20px; font-style: normal; font-variant: normal; font-weight: 700; line-height: 15px;
                                              padding-left:130px;color:#000000;background-color:Transparent;
                                              border: 2px solid #494F5B;border-width:0px 0px 2px 0px;""")

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>     
        self.RatingBox=QLabel(self)
        self.RatingBox.setGeometry(637,80,410,50)
        self.RatingBox.setStyleSheet("background-color:#FFFFFF;border 0px 1px 0px 0px outset #666e7f;")
        self.RatingLogo=QLabel(self)
        self.RatingLogo.setGeometry(637.5,80,45,50)
        self.RatingLogo.setPixmap(QPixmap("customer_dashboard\BookmarkRating.jpg"))
        self.RatingLogo.setScaledContents(True)
        self.RatingsHeader=QLabel("Ratings: ",self)
        self.RatingsHeader.setGeometry(685,85,100,35)
        self.RatingsHeader.setStyleSheet("Font-size:22px;font-family:Arial;")
        self.StarBlack=QPixmap("StarBlack.png")
        self.StarYellow=QPixmap("StarYellow2.png")
        self.Rating1=QLabel(self)
        self.Rating1.setScaledContents(True)
        self.Rating1.setGeometry(790,83,45,45)
        self.Rating1.setPixmap(self.StarYellow)
        self.Rating2=QLabel(self)
        self.Rating2.setScaledContents(True)
        self.Rating2.setGeometry(838,83,45,45)
        self.Rating2.setPixmap(self.StarYellow)
        self.Rating3=QLabel(self)
        self.Rating3.setScaledContents(True)
        self.Rating3.setGeometry(886,83,45,45)
        self.Rating3.setPixmap(self.StarYellow)
        self.Rating4=QLabel(self)
        self.Rating4.setScaledContents(True)
        self.Rating4.setGeometry(934,83,45,45)
        self.Rating4.setPixmap(self.StarYellow)
        self.Rating5=QLabel(self)
        self.Rating5.setScaledContents(True)
        self.Rating5.setGeometry(982,83,45,45)
        self.Rating5.setPixmap(self.StarBlack)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>        
        self.DateStartBox=QLabel(self)
        self.DateStartBox.setGeometry(637,138,410,50)
        self.DateStartBox.setStyleSheet("background-color:#FFFFFF;")
        self.DateStartLogo=QLabel(self)
        self.DateStartLogo.setPixmap(QPixmap("customer_dashboard\Date.png"))
        self.DateStartLogo.setGeometry(637,138,45,50)
        self.DateStartLogo.setScaledContents(True)
        self.DateStartHeader=QLabel("Date started:",self)
        self.DateStartHeader.setGeometry(685,138,160,50)
        self.DateStartHeader.setStyleSheet("Font-size:22px;font-family:Arial;")
        self.DateStartText=QLabel("November 26, 2000",self)
        self.DateStartText.setGeometry(835,138,200,50)
        self.DateStartText.setStyleSheet("Font-size:22px;font-family:Arial;")
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>        
        self.LocBox=QLabel(self)
        self.LocBox.setGeometry(1070,80,165,108)
        self.LocBox.setStyleSheet("background-color:#FFFFFF;")
        self.LocLogo=QLabel(self)
        self.LocLogo.setGeometry(1070,95,80,80)
        self.LocLogo.setPixmap(QPixmap("PhilLandmark.ico"))
        self.LocLogo.setScaledContents(True)
        self.LocText=QLabel("Region\n     V",self)
        self.LocText.setStyleSheet("Font-size:22px;font-family:Arial;")
        self.LocText.setGeometry(1150,85,100,100)
#----------------------------------------------------------------------------------------------------


    def settingsPage(self):
        #not yet functioning (new window function)
        self.initUI()
        self.menuBar()
        self.show()
        self.buttonSettings.setStyleSheet("background-color:white;color:black;border-width:1px;border-style:outset;border-radius:5px;border-color:black;font:bold 12px")
        self.settings = QLabel("Welcome to Settings", self)
        self.settings.setGeometry(300,300,300,10)

    def uploadProfilePic(self):
        self.image = QFileDialog.getOpenFileName(self,'Open File','c\\','image file(*.jpg)')
        self.imagePath = self.image[0]
        self.pixmap = QPixmap(self.imagePath)
        self.label.setPixmap(QPixmap(self.pixmap))
        self.label.setScaledContents(True)
    def RecentActivities(self):## JUST NEEDS TO BE CONNECTED TO DATABASE
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