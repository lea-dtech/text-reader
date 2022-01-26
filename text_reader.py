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
            f=fpath
            self.filterline(f)
        else:
            print("Please Choose file..!")

    def filterline(self,f):
        f=open(f)
        newfile=open("C:/Users/vikram/Desktop/dummy1.txt", "a")
        for line in f:
            if "not ok" or "NOT OK" in line:
                newfile.write(line)
        f.close()
        newfile.close()
        print("Operation Success..!")
        

app=QApplication(sys.argv)

Mainwindow=MainWindow()
widget=QtWidgets.QStackedWidget()
widget.addWidget(Mainwindow)
widget.setFixedWidth(400)
widget.setFixedHeight(300)
widget.show()
sys.exit(app.exec_())
