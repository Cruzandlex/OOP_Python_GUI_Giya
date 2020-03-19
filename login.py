import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from sqlitedict import *
from signup import Signup


class Login(QMainWindow, Signup):
    

    def __init__(self):
        super().__init__()
        self.tourist_accounts_db = SqliteDict("giya_accounts_tourist.db", autocommit=True)
        self.loginWindow()

    def loginWindow(self):
        #Fixed Window Size Setup
        self.setFixedSize(300, 500)
        self.setWindowTitle("Giya Login")
        #self.setStyleSheet(login_stylesheet)
        
        #Login Form
        self.username1 = QLineEdit(self)
        self.username1.setGeometry(20, 200, 260, 30)
        self.username1.setObjectName("txtbox")

        self.username_label = QLabel("Username", self)
        self.username_label.setGeometry(20, 220, 260, 30)
        self.username_label.setObjectName("under")

        self.password1 = QLineEdit(self)
        self.password1.setEchoMode(QLineEdit.Password)
        self.password1.setGeometry(20, 250, 260, 30)
        self.password1.setObjectName("txtbox")

        self.password_label = QLabel("Password", self)
        self.password_label.setGeometry(20, 270, 260, 30)
        self.password_label.setObjectName("under")
        
        self.login_button = QPushButton("Login", self)
        self.login_button.setGeometry(30, 300, 240, 30)
        self.login_button.setObjectName("loginButton")
        self.login_button.setAutoDefault(True)
        self.login_button.clicked.connect(self.login_auth)
        self.password1.returnPressed.connect(self.login_button.click) 

        self.signup_button = QPushButton("Signup", self)
        self.signup_button.setGeometry(30, 340, 240, 30)
        self.signup_button.setObjectName("signupButton")
        self.signup_button.setAutoDefault(True)
        self.signup_button.clicked.connect(self.open_signup)
        #Output
        self.show()

    def login_auth(self):
        print(self.username1.text())

    def open_signup(self):
        self.hide() # hiding the initial window
        signup_window = Signup() # instatiansing the 2nd window
        while signup_window.isActiveWindow() == True: # checking the state of 2nd window
            continue
        if signup_window.isActiveWindow() == False: # when the 2nd window closes
            self.show() # the initial winodw opens

# code for the login_auth
"""
        temp_db = self.tourist_accounts_db.get("tourist_data", [])
        indicator = True
        print(len(temp_db))
        for i in range(len(temp_db)):
            print(self.username1.text())
            print(self.password1.text())
            print(type(temp_db[i]["username"]))
            print(type(temp_db[i]["password"]))
            print(temp_db[i]["username"])
            print(temp_db[i]["password"])
            #if self.username.text() == (temp_db[i]["username"]) and self.password.text() == temp_db[i]["password"]:
             #   print("Successfully Logged In")
              #  indicator = False
        if indicator == True:
            print("Login Failed")
"""
    
            

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Login()
    sys.exit(app.exec_())