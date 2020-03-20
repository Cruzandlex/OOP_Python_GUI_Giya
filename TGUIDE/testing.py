import sys
from PyQt5.QtGui     import *
from PyQt5.QtCore    import *
from PyQt5.QtWidgets import *

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "App"

        self.width = 680
        self.height = 500
        self.setFixedSize(self.width,self.height)











        self.Homepage()

    def Homepage(self):
        self.setWindowTitle(self.title)
        buttonWindow1 = QPushButton('Dashboard', self)
        buttonWindow1.move(100, 100)
        buttonWindow1.clicked.connect(self.Dashboard)
        self.lineEdit1 = QLineEdit("Type here what you want to transfer for [Window1].", self)
        self.lineEdit1.setGeometry(250, 100, 400, 30)

        buttonWindow2 = QPushButton('Profile', self)
        buttonWindow2.move(100, 200)
        buttonWindow2.clicked.connect(self.Profile)        
        self.lineEdit2 = QLineEdit("Type here what you want to transfer for [Window2].", self)
        self.lineEdit2.setGeometry(250, 200, 400, 30)


        buttonWindow3 = QPushButton('History', self)
        buttonWindow3.move(100, 300)
        buttonWindow3.clicked.connect(self.Profile)        
        self.lineEdit2 = QLineEdit("Type here what you want to transfer for [Window2].", self)
        self.lineEdit2.setGeometry(250, 300, 400, 30)

        self.show()

    @pyqtSlot()
    def Dashboard(self):
        self.statusBar().showMessage("Switched to window 1")
        self.cams = Window1(self.lineEdit1.text()) 
        self.cams.show()
        self.close()

    @pyqtSlot()
    def Profile(self):
        self.statusBar().showMessage("Switched to window 2")
        self.cams = Window2(self.lineEdit2.text()) 
        self.cams.show()
        self.close()
    @pyqtSlot()
    def ActivityLog(self):
        self.statusBar().showMessage("Switched to window 2")
        self.cams = Window2(self.lineEdit2.text()) 
        self.cams.show()
        self.close()


class Window1(QDialog):
    def __init__(self, value, parent=None):
        super().__init__(parent)
        self.setFixedSize
        self.setWindowTitle('Window1')
        self.setWindowIcon(self.style().standardIcon(QStyle.SP_FileDialogInfoView))

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
        self.setFixedSize

        self.setWindowTitle('Window2')
        self.setWindowIcon(self.style().standardIcon(QStyle.SP_FileDialogInfoView))

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


if __name__ == '__main__':
    app=QApplication(sys.argv)
    ex=Window()
    sys.exit(app.exec_())