import sys
from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MainWindow(QWidget):
    def TourGuideDashboard(self):
        super().__init__()
        self.title="TOUR GUIDE DASHBOARD"
        self.x=500 # or left
        self.y=100 # or top
        self.width=850
        self.height=650
        self.setGeometry(self.x,self.y,self.width,self.height)
        self.initUI()
        self.stylesheet= """
        QMainWindow{
            background-color:color:#1C1F21;
        }
        QLabel{
            background-color: ;color:#CCF20D;padding-left:5px;
        }
        """
        self.setStyleSheet(self.stylesheet)

    def initUI(self):
        self.NameLabel=QLabel("Tour Guide Name",self)
        self.NameLabel.setGeometry(500,200,100,100)
        self.topButtonSplitter = QSplitter(Qt.Horizontal)
        self.topButtonSplitter.setGeometry(150,650,3,850)

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