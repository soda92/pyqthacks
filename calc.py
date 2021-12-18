import sys
import subprocess
import time
from PyQt5 import QtGui
from PyQt5 import QtWidgets

import win32gui

from PyQt5.QtGui import QWindow
from PyQt5.QtCore import QProcess
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QWidget
from PyQt5 import QtGui

class MainWindow(QMainWindow):

    def initUI(self, hwnd):
        # create a process
        time.sleep(1)
        window = QWindow.fromWinId(hwnd)
        self.createWindowContainer(window, self)
        self.setGeometry(500, 500, 450, 400)
        self.setWindowTitle('File dialog')
        self.show()

    def __init__(self, hwnd, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # self.setWindowTitle("App")
        self.initUI(hwnd)

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.button = QtWidgets.QPushButton('Test', self)
        QtWidgets.QVBoxLayout
        self.button.clicked.connect(self.handleButton)
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.button)

    def handleButton(self):
        print ('Hello World')

    def getHwnd(self):
        return self.effectiveWinId()
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    wind2  = Window()
    wind2.show()
    hwnd = wind2.getHwnd()
    window = MainWindow(hwnd=hwnd)
    app.exec_()
