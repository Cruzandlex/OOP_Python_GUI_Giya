from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import *
import sys,sqlitedict

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.dictionarydb = sqlitedict.SqliteDict("DBS2.db",autocommit=True)
        self.Database=self.dictionarydb.get('Data',[])
        print(self.Database)
        #self.dictionarydb.clear()
    def setupUi(self):
        self.application_width  = 750 #Set default height
        self.application_height = 550
        self.stack = QStackedLayout()#stack widget
        self.LoginUI()
        self.SignupUI()
        self.User()
        self.stack.addWidget(self.Login)
        self.stack.addWidget(self.Signup)
        self.stack.addWidget(self.user)

    def User(self):
        self.Login.close()
        x = Main1()
        x.show()

    def LoginUI(self):
        self.cname = ""
        self.cage = ""
        self.csex = ""
        self.cemail = ""
        self.ccontact = ""
        self.cuser = ""
        self.cpass = ""
        self.Login = QWidget()
        self.Login.setWindowIcon(QtGui.QIcon("appLogoico.png"))
        self.Login.setFixedSize(self.application_width,self.application_height)
        oImage = QImage("back.jpg")
        sImage = oImage.scaled(QSize(self.application_width, self.application_height)) 
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))                        
        self.Login.setPalette(palette)
        layout = QHBoxLayout()
        centerlogin = QGroupBox()
        centerlogin.setFixedSize(200,150)
        centerlogin.setStyleSheet("QGroupBox{border: 1px solid black; border-radius: 10px; background-color: rgba(255,255,255,0.7); padding: 10px;} Qlabel{}")
        centerloginlayout = QVBoxLayout()
        user_pass = QFormLayout()
        self.userl = QLineEdit()
        self.passwl = QLineEdit()
        user_pass.addRow(QLabel("Username:"),self.userl)
        user_pass.addRow(QLabel("Password:"),self.passwl)
        user_pass.addRow(QPushButton("Login",clicked = lambda: self.checkuser()),QPushButton("Signup",clicked = lambda: self.stack.setCurrentIndex(1)))
        user_pass.setFormAlignment(QtCore.Qt.AlignCenter)
        exitbutton = QPushButton("",clicked = lambda: self.Login.close())
        exitbutton.setToolTip("Exit Program")
        exitbutton.setIcon(QtGui.QIcon("signOutico.ico"))
        exitbutton.setStyleSheet("background-color:transparent;")
        user_pass.addRow(exitbutton,QLabel(""))
        centerloginlayout.addLayout(user_pass)
        centerlogin.setLayout(centerloginlayout)
        layout.addStretch(1)
        layout.addWidget(centerlogin)
        layout.addStretch(5)
        self.Login.setLayout(layout)
    
    def checkuser(self):#Widget selector changer
        d =False
        if len(self.dictionarydb) == 0:
            error = QMessageBox()
            error.setText("Empty Data Base!")
            error.setWindowIcon(QtGui.QIcon("appLogoico.png"))
            error.setWindowTitle("Error")
            error.exec_()
            self.userl.clear()
            self.passwl.clear()
        else:
            for x in self.Database:
                if x["user"]== self.userl.text() and x["pass"]== self.passwl.text():
                    d=True
                    break
                    self.userl.clear()
                    self.passwl.clear()
            if d == True:
                pass
            else:            
                error = QMessageBox()
                error.setText("Invalid input")
                error.setWindowIcon(QtGui.QIcon("appLogoico.png"))
                error.setWindowTitle("Error")
                error.exec_()
                self.userl.clear()
                self.passwl.clear()
        
    def SignupUI(self):
        self.Signup = QWidget()
        self.Signup.setWindowIcon(QtGui.QIcon("appLogoico.png"))
        self.Signup.setFixedSize(self.application_width,self.application_height)
        oImage = QImage("back.jpg")
        sImage = oImage.scaled(QSize(self.application_width, self.application_height)) 
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))                        
        self.Signup.setPalette(palette)
        layout = QHBoxLayout()
        centerlogin = QGroupBox()
        centerlogin.setFixedSize(300,300)
        centerlogin.setStyleSheet("QGroupBox{border: 1px solid black; border-radius: 10px; background-color: rgba(255,255,255,0.7); padding: 10px;} Qlabel{}")
        centerloginlayout = QVBoxLayout()
        user_pass = QFormLayout()
        self.user = QLineEdit()
        self.passw = QLineEdit()
        self.name = QLineEdit()
        self.age = QLineEdit()
        self.sex = QLineEdit()
        self.email = QLineEdit()
        self.contact = QLineEdit()
        
        user_pass.addWidget(QLabel("                   Signup GIYA"))
        user_pass.addRow(QLabel("Name:"),self.name)
        user_pass.addRow(QLabel("Age:"),self.age)
        user_pass.addRow(QLabel("Sex:"),self.sex)
        user_pass.addRow(QLabel("Email:"),self.email)
        user_pass.addRow(QLabel("Cell No.:"),self.contact)
        user_pass.addRow(QLabel("Username:"),self.user)
        user_pass.addRow(QLabel("Password:"),self.passw)

        user_pass.addRow(QPushButton("Login",clicked = lambda: self.stack.setCurrentIndex(0)),QPushButton("Signup",clicked = lambda: self.signup()))
        user_pass.setFormAlignment(QtCore.Qt.AlignCenter)
        exitbutton = QPushButton("",clicked = lambda: self.Signup.close())
        exitbutton.setToolTip("Exit Program")
        exitbutton.setIcon(QtGui.QIcon("signOutico.ico"))
        exitbutton.setStyleSheet("background-color:transparent;")
        user_pass.addRow(exitbutton,QLabel(""))
        centerloginlayout.addLayout(user_pass)
        centerlogin.setLayout(centerloginlayout)
        layout.addStretch(1)
        layout.addWidget(centerlogin)
        layout.addStretch(5)
        self.Signup.setLayout(layout)

    def signup(self):
        avail = True
        for x in (self.Database):
            if x["user"] == self.user.text():
                error = QMessageBox()
                error.setText("Username already taken")
                error.setWindowIcon(QtGui.QIcon("appLogoico.png"))
                error.setWindowTitle("Error")
                error.exec_()
                avail = False
                break
        if avail == True:
            det = [self.user.text(),self.passw.text(),self.name.text(),self.age.text(),self.sex.text(),self.email.text(),self.contact.text()]
            self.Database.append({"user":det[0],"pass":det[1],"name":det[2],"age":det[3],"sex":det[4],"email":det[5],"contact":det[6]})
            self.dictionarydb['Data'] = self.Database
            self.user.clear()
            self.passw.clear()
            self.name.clear()
            self.age.clear()
            self.sex.clear()
            self.email.clear()
            self.contact.clear()

class Main1(Main):
    def __init__(self):
        super().__init__()
        self.UsermainUI()

    def UsermainUI(self):
        self.ui = QWidget()
        self.ui.setWindowIcon(QtGui.QIcon("appLogoico.png"))
        self.ui.setFixedSize(750,550)
        layout = QHBoxLayout()
        self.ui.sidepanel = QGroupBox()
        self.ui.sidepanel.setFixedSize(150,530)
        profile = QGroupBox()
        offers = QGroupBox()
        layout.addWidget(self.sidepanel)
        layout.addWidget(profile)
        layout.addWidget(offers)
        txt = QLabel(self.cname) 
        layout.addWidget(txt)
        self.ui.setLayout(layout)
        self.ui.show()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    M = Main1()
    sys.exit(app.exec())
