import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class App(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
    def mainWindow(self):
        self.show()