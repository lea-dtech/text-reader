import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
from PyQt5.uic import loadUi

class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("gui.ui",self)
        self.Browse.clicked.connect(self.browsefiles)

    def browsefiles(self):
        fname=QFileDialog.getOpenFileName(self, "open file", "c:/users",'TXT files(*.txt)')
        fpath=fname[0]
        if fname[0]!="":
            f=open(fpath)
            print(f.read())
            f.close()
        

app=QApplication(sys.argv)

Mainwindow=MainWindow()
widget=QtWidgets.QStackedWidget()
widget.addWidget(Mainwindow)
widget.setFixedWidth(400)
widget.setFixedHeight(300)
widget.show()
sys.exit(app.exec_())
