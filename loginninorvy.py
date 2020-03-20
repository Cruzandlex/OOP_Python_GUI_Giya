from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import *
import sys,sqlitedict
from customerDashboard import *

class Signup(QWidget):
    def __init__(self):
        super().__init__()
        self.sign()
        self.dictionarydb = sqlitedict.SqliteDict("DBS2.db",autocommit=True)
        self.Database=self.dictionarydb.get('Data',[])
        self.show()
    def sign(self):
        self.setWindowIcon(QtGui.QIcon("appLogoico.png"))
        self.setFixedSize(750,550)
        oImage = QImage("back.jpg")
        sImage = oImage.scaled(QSize(750,550))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))                        
        self.setPalette(palette)
        layout = QHBoxLayout()
        centerlogin = QGroupBox()
        centerlogin.setFixedSize(300,350)
        centerlogin.setStyleSheet("QGroupBox{border: 1px solid black; border-radius: 10px; background-color: rgba(255,255,255,0.7); padding: 10px;} Qlabel{}")
        centerloginlayout = QVBoxLayout()
        user_pass = QFormLayout()
        self.username = QLineEdit()
        self.password = QLineEdit()
        self.name = QLineEdit()
        self.age = QLineEdit()
        self.sex = QLineEdit()
        self.loc = QLineEdit()
        self.email = QLineEdit()
        self.started = QLineEdit()
        self.favloc = QLineEdit()
        self.contact = QLineEdit()
        
        user_pass.addWidget(QLabel("                   Signup GIYA"))
        user_pass.addRow(QLabel("Name:"),self.name)
        user_pass.addRow(QLabel("Age:"),self.age)
        user_pass.addRow(QLabel("Sex:"),self.sex)
        user_pass.addRow(QLabel("Location:"),self.loc)
        user_pass.addRow(QLabel("Email:"),self.email)
        user_pass.addRow(QLabel("Date:"),self.started)
        user_pass.addRow(QLabel("Fav. Loc:"),self.favloc)
        user_pass.addRow(QLabel("Cell No.:"),self.contact)
        user_pass.addRow(QLabel("Username:"),self.username)
        user_pass.addRow(QLabel("Password:"),self.password)
        user_pass.addRow(QPushButton("Login",clicked = lambda: self.backtologin()),QPushButton("Signup", clicked = lambda: self.validation()))
        user_pass.setFormAlignment(QtCore.Qt.AlignCenter)
        exitbutton = QPushButton("",clicked = lambda: self.close())
        exitbutton.setToolTip("Exit Program")
        exitbutton.setIcon(QtGui.QIcon("signOutico.ico"))
        exitbutton.setStyleSheet("background-color:transparent;")
        user_pass.addRow(exitbutton,QLabel(""))
        centerloginlayout.addLayout(user_pass)
        centerlogin.setLayout(centerloginlayout)
        layout.addStretch(1)
        layout.addWidget(centerlogin)
        layout.addStretch(5)
        self.setLayout(layout)
    def backtologin(self):
        x = Login()
        x.show()
        self.close()
    def validation(self):
        self.Database.append({"username":self.username.text(),"password":self.password.text(),"name":self.name.text(),"age":self.age.text(),"sex":self.sex.text(),"loc":self.loc.text(),"email":self.email.text(),"started":self.started.text(),"favloc":self.favloc.text(),"contact":self.contact.text()})
        self.dictionarydb['Data'] = self.Database

class Login(QWidget):
    def __init__(self):
        super().__init__()
        self.dictionarydb = sqlitedict.SqliteDict("DBS2.db",autocommit=True)
        self.Database=self.dictionarydb.get('Data',[])
        self.login()
        self.show()
    
    def login(self):
        self.setWindowIcon(QIcon("appLogoico.png"))
        self.setFixedSize(750,550)
        oImage = QImage("back.jpg")
        sImage = oImage.scaled(QSize(750,550),QtCore.Qt.KeepAspectRatio) 
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))                        
        self.setPalette(palette)
        layout = QHBoxLayout()
        btn = QPushButton("Ui2")
        layout.addWidget(btn)
        layoutw = QVBoxLayout()
        login = QFormLayout()
        self.u_line = QLineEdit()
        self.p_line = QLineEdit()
        login.setFormAlignment(Qt.AlignLeading|Qt.AlignHCenter|Qt.AlignVCenter)
        login.addRow(QLabel("Username:"),self.u_line)
        login.addRow(QLabel("Password:"),self.p_line)
        login_btn = QPushButton("Login",clicked = lambda: self.checkuser())#database work here
        signup_btn = QPushButton("Signup")
        login.addRow(login_btn)
        login.addRow(QLabel("----------------------------------Or----------------------------------"))
        login.addRow(signup_btn)
        layoutw.addLayout(login)
        border = QGroupBox()
        border.setStyleSheet("QGroupBox{border: 1px solid black; background-color: lightgray;}")
        border.setLayout(layoutw)
        borderl = QVBoxLayout()
        border.setFixedSize(300,150)
        borderl.addStretch()
        borderl.addWidget(border)
        Exit = QPushButton("Exit",clicked = lambda: self.close())
        Exit.setFixedWidth(30)
        borderl.addStretch()
        borderl.addWidget(Exit)
        self.setLayout(borderl)

    def checkuser(self):#Widget selector changer
        d =False
        if len(self.Database) == 0:
            error = QMessageBox()
            error.setText("Empty Data Base!")
            error.setWindowIcon(QtGui.QIcon("appLogoico.png"))
            error.setWindowTitle("Error")
            error.exec_()
            self.u_line.clear()
            self.p_line.clear()
        else:
            for x in self.dictionarydb["Data"]:
                if x["username"]== self.u_line.text() and x["password"]== self.p_line.text():
                    d=True
                    y = dashboardUI(x)
                    y.show()
                    self.close()
                    break
            if d == True:
                pass
            else:            
                error = QMessageBox()
                error.setText("Invalid input")
                error.setWindowIcon(QtGui.QIcon("appLogoico.png"))
                error.setWindowTitle("Error")
                error.exec_()
                self.u_line.clear()
                self.p_line.clear()

if __name__ == '__main__':
    app=QApplication(sys.argv)
    ex=Signup()
    sys.exit(app.exec_())