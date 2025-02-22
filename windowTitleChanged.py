from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

import sys
from random import choice

window_title=[
    "My App",
    "My App",
    "Still My App",
    "Still My App",
    "what on earth",
    "what on earth",
    "This is Surperising",
    "This is Surperising",
    "Something went wrong"  
]

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()


        self.n_times_clicked=0

        self.setWindowTitle("My App")

        self.button=QPushButton("Press Me!")
        self.button.clicked.connect(self.the_button_clicked)

        self.windowTitleChanged.connect(self.the_window_title_changed)

        self.setCentralWidget(self.button)

    def the_button_clicked(self):
        print("Clicked")
        new_window_title=choice(window_title)
        print("Setting title changed : %s" % window_title)
        self.setWindowTitle(new_window_title)

    def the_window_title_changed(self, window_title):
        print("Window Title changed: %s" % window_title)

        if window_title == "Something went wrong":
            self.button.setDisabled(True)

app=QApplication(sys.argv)
window=MainWindow()
window.show()

app.exec()