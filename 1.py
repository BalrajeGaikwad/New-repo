import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")


        button=QPushButton("Press me!")
        button.setCheckable(True)
        button.clicked.connect(self.button_clicked)
        button.clicked.connect(self.the_button_was_toggled)

        self.setCentralWidget(button)

    def button_clicked(self):
        print("Clicked")

    def the_button_was_toggled(self, checked):
        print("Checked?", checked)



app=QApplication(sys.argv)
window=MainWindow()
window.show()

app.exec()