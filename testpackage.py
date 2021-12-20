from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget
import sys


# Subclass QMainWindow to customize the application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(QSize(400, 300))

        self.setWindowTitle("My App")
        button = QPushButton("Press Me!")

        # Set the central widget of the Window.
        self.setCentralWidget(button)


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()
