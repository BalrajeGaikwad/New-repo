import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()


        self.setWindowTitle("My App")

        self.button=QPushButton("Press Me!")
        self.button.clicked.connect(self.btn_was_clicked)

        self.setCentralWidget(self.button)

    def btn_was_clicked(self):
        self.button.setText("You already Clicked me.")
        self.button.setEnabled(False)

        self.setWindowTitle("My One Shot APP")

app=QApplication(sys.argv)
window=MainWindow()
window.show()

app.exec()