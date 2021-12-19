from PyQt6.QtCore import Qt
from PyQt6.QtGui import QKeyEvent
import ui
import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QTabBar

app = QApplication(sys.argv)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.keyPressEvent = self.myexit
        
        
        # self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

    def myexit(self, event: QKeyEvent):
        if event.key() == Qt.Key.Key_Escape:
            QApplication.quit()
    

class MyWindow(ui.Ui_MainWindow):
    def __init__(self):
        self.window = MainWindow()
        self.setupUi(self.window)
        self.retranslateUi(self.window)
        self.window.show()

window = MyWindow()

app.exec()
