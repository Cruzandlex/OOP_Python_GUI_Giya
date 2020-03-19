import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from sqlitedict import *
from datetime import *

class Signup(QWidget):
    
    def __init__(self):
        super().__init__()
        self.tourist_accounts_db = SqliteDict("giya_accounts_tourist.db", autocommit=True)
        dummy = QLineEdit("")
        self.textboxSlots = [dummy]
        self.loginWindow()

    def loginWindow(self):
        #Fixed Window Size Setup
        self.setFixedSize(300, 500)
        self.setWindowTitle("Giya Signup")
        
        #Signup Form
        labels = ["First Name", "Last Name", "Age", "Email", "Contact No.", "Username", "Password"]
        position = [20, 80]

        #title
        self.title_label = QLabel("Signup", self)
        self.title_label.setGeometry(20,40,260,30)
        
        #all textboxes
        for i in range(len(labels)):

            self.textbox = QLineEdit(self)
            self.textbox.setGeometry(position[0], position[1]+i*50, 260, 30)
            if labels[i] == "Password":
                self.textbox.setEchoMode(QLineEdit.Password)
            if i == 0:
                self.textboxSlots[0] = self.textbox
            else:
                self.textboxSlots.append(self.textbox) 

            self.label = QLabel(labels[i], self)
            self.label.setGeometry(position[0], position[1]+20+i*50, 260, 30)

        self.signup_button = QPushButton("Signup", self, clicked = lambda:self.signup())
        self.signup_button.setGeometry(20, 100+7*50, 260, 30)

        self.show()

    def signup(self):
        temp_db = self.tourist_accounts_db.get("tourist_data", [])
        temp_data = {"name":"", "age":"", "email":"", "contact no":"", "username":"", "password":"", "history":[], "event":None, "date started":""}
        temp_data["name"] = self.textboxSlots[0].text() + " " + self.textboxSlots[1].text()
        temp_data["age"] = self.textboxSlots[2].text()
        temp_data["email"] = self.textboxSlots[3].text()
        temp_data["contact no"] = self.textboxSlots[4].text()
        temp_data["username"] = self.textboxSlots[5].text()
        temp_data["password"] = self.textboxSlots[6].text()
        temp_data["date started"] = date.today()
        temp_db.append(temp_data)
        self.tourist_accounts_db["tourist_data"] = temp_db
        self.hide()
        if self.isHidden():
            self.close()
            
            

"""      
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Login()
    sys.exit(app.exec_())
"""
