from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import *
import sys,sqlitedict
from customerDashboard import mainUserUI

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.dictionarydb = sqlitedict.SqliteDict("DBS2.db",autocommit=True)
        self.Database=self.dictionarydb.get('Data',[])
        """self.dictionarydb.clear() #database clear"""
    def setupUi(self):
        self.application_width  = 750 #Set default height
        self.application_height = 550
    
        self.stack = QStackedLayout()#stack widgets
        self.UI_1()#login
        self.UI_2()#sihnup
        self.UI_3()#userdash
        self.UI_5()#chat
        self.UI_6()#change profile
        self.UI_7()#view tour
        
        self.stack.addWidget(self.UI1)
        self.stack.addWidget(self.UI2)
        self.stack.addWidget(self.UI3)
        self.stack.addWidget(self.UI5)
        self.stack.addWidget(self.UI6)
        self.stack.addWidget(self.UI7)

    def change_window(self,x):
        self.stack.setCurrentIndex(x)
    
    def UI_1(self):#login
        self.UI1 = QWidget()
        self.UI1.setWindowIcon(QIcon("appLogoico.png"))
        self.UI1.setFixedSize(self.application_width,self.application_height)
        oImage = QImage("back.jpg")
        sImage = oImage.scaled(QSize(self.application_width, self.application_height),QtCore.Qt.KeepAspectRatio) 
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))                        
        self.UI1.setPalette(palette)
        layout = QHBoxLayout()
        btn = QPushButton("Ui2", clicked = lambda:self.change_window(1))
        layout.addWidget(btn)
        layoutw = QVBoxLayout()
        login = QFormLayout()
        self.u_line = QLineEdit()
        self.p_line = QLineEdit()
        login.setFormAlignment(Qt.AlignLeading|Qt.AlignHCenter|Qt.AlignVCenter)
        login.addRow(QLabel("Username:"),self.u_line)
        login.addRow(QLabel("Password:"),self.p_line)
        login_btn = QPushButton("Login", clicked = lambda:self.Login(self.u_line.text(),self.p_line.text()))#database work here
        signup_btn = QPushButton("Signup", clicked = lambda:self.change_window(1))
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
        Exit = QPushButton("Exit")
        Exit.clicked.connect(self.closing)
        Exit.setFixedWidth(30)
        borderl.addStretch()
        borderl.addWidget(Exit)
        self.UI1.setLayout(borderl)

    def Login(self,user,pas):
        d =False
        if len(self.dictionarydb) == 0:
            QMessageBox.question(self, 'Empty database', "Error, Please SignUp First", QMessageBox.Ok)
        else:
            for x in self.dictionarydb['Data']:
                if x["username"]==user and x["password"]==pas:
                    self.change_window(2)
                    d=True
                    break
            if d == True:
                pass
            else:            
                QMessageBox.question(self, 'Invalid', "Error, Please Check Login Input",QMessageBox.Ok)
                self.u_line.clear()
                self.p_line.clear()
        
    def closing(self):
        self.UI1.close()

    def UI_2(self):#signup
        self.UI2= QWidget()
        self.UI2.setWindowIcon(QIcon("appLogoico.png"))
        self.UI2.setFixedSize(self.application_width,self.application_height)
        oImage = QImage("back.jpg")
        sImage = oImage.scaled(QSize(self.application_width, self.application_height),QtCore.Qt.KeepAspectRatio) 
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))                        
        self.UI2.setPalette(palette)
        layout = QVBoxLayout()
        
        border1 = QFormLayout()
        self.Name = QLineEdit()
        self.Sex = QLineEdit()
        self.Age = QLineEdit()
        self.monum = QLineEdit()
        self.Email = QLineEdit()
        self.Username = QLineEdit()
        self.Password = QLineEdit()
        border1.addRow(QLabel("Name:    "),self.Name)       
        border1.addRow(QLabel("Sex:     "),self.Sex)
        border1.addRow(QLabel("Age:     "),self.Age)
        border1.addRow(QLabel("Mob. no: "),self.monum)
        border1.addRow(QLabel("Email:   "),self.Email)
        border1.addRow(QLabel("Username:"),self.Username)
        border1.addRow(QLabel("Password:"),self.Password)
        border1.addRow(QPushButton("Submit", clicked = lambda: self.signup()),QPushButton("Cancel", clicked = lambda: self.change_window(0)))
        border = QGroupBox()
        border.setStyleSheet("QGroupBox{border: 1px solid black; background-color: lightgray;}")
        border.setFixedSize(300,220)
        border.setLayout(border1)
        layout.addWidget(border)
        self.UI2.setLayout(layout)

    def signup(self):
        self.Database.append({"username":self.Username.text(),"password":self.Password.text(),"role":self.type,"msg":["hello",'hi'],"pending":[],"acc":{"name":self.Name.text(),"age":self.Age.text(),"sex":self.Sex.text(),"email":self.Email.text(),"Monum":self.monum.text()}})
        self.dictionarydb['Data']=self.Database
        self.change_window(0)
        
    def UI_3(self):#userdash
        self.UI3 = QWidget()
        self.UI3.hide()
        x = mainUserUI()
        x.show()
        self.change_window(var)

    def UI_5(self):#chat
        self.UI5= QWidget()
        self.UI5.setWindowIcon(QIcon("appLogoico.png"))
        self.UI5.setWindowTitle("Chat")
        self.UI5.setFixedSize(self.application_width,self.application_height)
        layout = QHBoxLayout()

        self.UI5.setLayout(layout)
    
    def UI_6(self):
        self.UI6= QWidget()
        self.UI6.setWindowIcon(QIcon("appLogoico.png"))
        self.UI6.setFixedSize(self.application_width,self.application_height)
        layout = QHBoxLayout()
        btn = QPushButton("Ui7", clicked = lambda:self.change_window(6))
        layout.addWidget(btn)
        self.UI6.setLayout(layout)
    
    def UI_7(self):
        self.UI7= QWidget()
        self.UI7.setWindowIcon(QIcon("appLogoico.png"))
        self.UI7.setFixedSize(self.application_width,self.application_height)
        layout = QHBoxLayout()
        btn = QPushButton("Ui1", clicked = lambda:self.change_window(0))
        layout.addWidget(btn)
        self.UI7.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    M = Main()
    sys.exit(app.exec())


