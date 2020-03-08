import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from datetime import datetime
import calendar

class mainUserUI(QMainWindow):
    global currentYear, currentMonth
    currentMonth = datetime.now().month
    currentYear = datetime.now().year

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

        self.initUI()
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
        self.button1.clicked.connect(self.profilePage)
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
        self.button2.clicked.connect(self.homePage)
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
        self.button3.clicked.connect(self.dashboardPage)
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
        self.button4.clicked.connect(self.aboutUsPage)
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
        self.button5.clicked.connect(self.signOut)
        #Calendar for festivals
        self.calendar = QCalendarWidget(self)
        self.calendar.resize(600,500)
        self.calendar.move(130,50)

    def homePage(self):
        print("home clicked.")

    def profilePage(self):
        print("profile clikced.")

    def dashboardPage(self):
        print("dashboard clicked.")

    def aboutUsPage(self):
        print("about us clicked.")
    
    def signOut(self):
        print("sign out.")

#executes the application
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = mainUserUI()
    sys.exit(app.exec_())