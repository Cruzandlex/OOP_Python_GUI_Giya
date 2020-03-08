import sys
from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.title="TOUR GUIDE DASHBOARD"
        self.x=500 # or left
        self.y=100 # or top
        self.width=750
        self.height=600
        self.setGeometry(self.x,self.y,self.width,self.height)
        self.initUI()

    def initUI(self):
        #DriverName.setFont(QtGui.QFont("Sanserif",20))
        #DriverName.setStyleSheet('color:Princessblue')
        #DriverName.setGeometry (150,0,100,100)
        vbox=QVBoxLayout()
        self.B1Icon= QLabel(self)
        pixmap = QPixmap('User.ico')
        self.B1Icon.setPixmap(pixmap)
        
        
        self.Label1=QHBoxLayout()
        Text=QLabel("               Profile",self)
        self.Label1.addWidget(Text)
        self.Label1.addStretch()


        vbox.addWidget(self.B1Icon)
        vbox.addLayout(self.Label1)
        vbox.addStretch()
        
    
        
        
        
        vbox2=QVBoxLayout()
        self.Test=QPushButton("Vbox2ButtonTest",self)
        vbox2.addWidget(self.Test)
        




        #Main Layout
        hboxmain=QHBoxLayout()
        hboxmain.addLayout(vbox)
        hboxmain.addLayout(vbox2)
        self.setLayout(hboxmain)



        self.show()




    """def initUI(self):
        oImage = QImage("AspenGold.jpg")
        sImage = oImage.scaled(QSize(300,200))                   # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))                        
        self.setPalette(palette)

        self.Icon= QLabel(self)
        pixmap = QPixmap('User.ico')
        self.Icon.setPixmap(pixmap)
        self.Icon.setGeometry(15,10,200,150)
        self.show()"""

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Mainwindow = MainWindow()
    sys.exit(app.exec_())