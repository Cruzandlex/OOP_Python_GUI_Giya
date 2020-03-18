import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from sqlitedict import *
import sip

sip.setapi('QString', 2)
sip.setapi('QVariant', 2)

class Login(QWidget):
    

    def __init__(self):
        super().__init__()
        self.tourist_accounts_db = SqliteDict("giya_accounts_tourist.db", autocommit=True)
        self.tourGuide_accounts_db = SqliteDict("giya_accounts_tourGuide.db", autocommit=True)
        self.loginWindow()

    def loginWindow(self):
        #Fixed Window Size Setup
        self.setFixedSize(300, 500)
        self.setWindowFlags(Qt.Window |
                            Qt.CustomizeWindowHint)
        self.setWindowTitle("Giya Login")
        #self.setStyleSheet(login_stylesheet)
        
        #Login Form
        self.username = QLineEdit(self)
        self.username.setGeometry(20, 200, 260, 30)
        self.username.setObjectName("txtbox")

        self.username_label = QLabel("Username", self)
        self.username_label.setGeometry(20, 220, 260, 30)
        self.username_label.setObjectName("under")

        self.password = QLineEdit(self)
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setGeometry(20, 250, 260, 30)
        self.password.setObjectName("txtbox")

        self.password_label = QLabel("Password", self)
        self.password_label.setGeometry(20, 270, 260, 30)
        self.password_label.setObjectName("under")
        
        self.login_button = QPushButton("Login", self)
        self.login_button.setGeometry(30, 350, 240, 30)
        self.login_button.setObjectName("loginButton")
        self.login_button.setAutoDefault(True)
        self.login_button.clicked.connect(self.login_auth)
        self.password.returnPressed.connect(self.login_button.click) 

        self.groupBox1 = QGroupBox("")
        self.groupBox1.setGeometry(0, 0, 300, 30)
        self.groupBox1.setObjectName("headbar")
        
        self.groupBox2 = QGroupBox("")
        self.groupBox2.setGeometry(0, 30, 300, 470)
        self.groupBox2.setObjectName("frame")

        self.radio1 = QRadioButton(self)
        self.radio1.move(30, 300)
        self.radio1.setChecked(True)
        
        self.radio1_label = QLabel("Login as Tourist", self)
        self.radio1_label.move(50, 300)

        self.radio2 = QRadioButton(self)
        self.radio2.move(30, 325)

        self.radio2_label = QLabel("Login as Tour Guide", self)
        self.radio2_label.move(50, 325)
        
        
        #Output
        self.show()

    def login_auth(self):
        if self.radio1.isChecked():
            temp_db = self.tourist_accounts_db.get("tourist_data")
        elif self.radio2.isChecked():
            temp_db = self.tourGuide_accounts_db.get("tourGuide_data")    
        indicator = True
        for i in range(len(temp_db)):
            if self.username.text() == temp_db[i]["username"] and self.password.text() == temp_db[i]["password"]:
                print("Successfully Logged In")
                indicator = False
        if indicator == True:
            print("Login Failed")
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Login()
    sys.exit(app.exec_())