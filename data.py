from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import *
import sys,sqlitedict

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.LoginUI()
        self.dictionarydb = sqlitedict.SqliteDict("DBS2.db",autocommit=True)
        self.Database=self.dictionarydb.get('Data',[])
        print(self.Database)
        self.currentacc = {}
        #self.dictionarydb.clear()

    def LoginUI(self):
        self.setWindowIcon(QIcon("appLogoico.png"))
        self.setFixedSize(750,550)
        oImage = QImage("back.jpg")
        sImage = oImage.scaled(QSize(750,550),QtCore.Qt.KeepAspectRatio) 
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
        Exit.setFixedWidth(30)
        borderl.addStretch()
        borderl.addWidget(Exit)
        self.UI1.setLayout(borderl)

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
                    self.currentacc=x
                    break
                    self.userl.clear()
                    self.passwl.clear()
                    self.buttonWindow1_onClick()
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
        

    def buttonWindow1_onClick(self):
        self.statusBar().showMessage("Switched to window 1")
        self.cams = Window1(self.lineEdit1.text()) 
        self.cams.show()
        self.close()

    def buttonWindow2_onClick(self):
        self.statusBar().showMessage("Switched to window 2")
        self.cams = Window2(self.lineEdit2.text()) 
        self.cams.show()
        self.close()


class Window1(QDialog):
    def __init__(self, value, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Window1')
        self.setWindowIcon(self.style().standardIcon(QStyle.SP_FileDialogInfoView))
        self.setFixedSize(750,550)
        label1 = QLabel(value)
        self.button = QPushButton()
        self.button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.button.setIcon(self.style().standardIcon(QStyle.SP_ArrowLeft))
        self.button.setIconSize(QSize(200, 200))

        layoutV = QVBoxLayout()
        self.pushButton = QPushButton(self)
        self.pushButton.setStyleSheet('background-color: rgb(0,0,255); color: #fff')
        self.pushButton.setText('Click me!')
        self.pushButton.clicked.connect(self.goMainWindow)
        layoutV.addWidget(self.pushButton)

        layoutH = QHBoxLayout()
        layoutH.addWidget(label1)
        layoutH.addWidget(self.button)
        layoutV.addLayout(layoutH)
        self.setLayout(layoutV)

    def goMainWindow(self):
        self.cams = Window()
        self.cams.show()
        self.close() 


class Window2(QDialog):
    def __init__(self, value, parent=None):
        super().__init__(parent)
        self.UsermainUI()
    def UsermainUI(self):
        self.setWindowIcon(QtGui.QIcon("appLogoico.png"))
        self.setFixedSize(750,550)
        layout = QHBoxLayout()
        self.sidepanel = QGroupBox()
        self.sidepanel.setFixedSize(150,530)
        profile = QGroupBox()
        offers = QGroupBox()
        layout.addWidget(self.sidepanel)
        layout.addWidget(profile)
        layout.addWidget(offers)
        self.setLayout(layout)
        print(self.currentacc)

    """def goMainWindow(self):
        self.cams = Window()
        self.cams.show()
        self.close()  """  


if __name__ == '__main__':
    app=QApplication(sys.argv)
    ex=Window()
    sys.exit(app.exec_())