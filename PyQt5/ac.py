import sys
from unittest import result
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets,QtCore
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QDialog, QApplication, QWidget,QMessageBox
# from PyQt5.QtGui import QPixmap
import mysql.connector

try:
    conn=mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="test"
    )
except:
    print("Database Connection Error !")
    sys.exit()

class Activity(QDialog):
    def __init__(self):
        super(Activity,self).__init__()
        loadUi("D:\Program\Python\PyQt5\designer.ui",self)
        self.signup.clicked.connect(self.gotosignup)
        self.login.clicked.connect(self.gotologin)
        self.signup.setEnabled(False)   # Enable and Disable push button


    def gotologin(self):
        login=LoginScreen()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotosignup(self):
        create=SignUpScreen()
        widget.addWidget(create)
        widget.setCurrentIndex(widget.currentIndex()+1)

class LoginScreen(QDialog):
    def __init__(self):
        super(LoginScreen,self).__init__()
        loadUi("D:\Program\Python\PyQt5\login.ui",self)
        self.signup.clicked.connect(self.gotosignup)
        self.login.clicked.connect(self.loginUser)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)

    def gotosignup(self):
        # LoginScreen.hide(self)   #incorrect
        create=SignUpScreen()
        widget.addWidget(create)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def loginUser(self):
        email=self.username.text()
        pas=self.password.text()
        if (email=="admin")and(pas=="admin"):
            crud_window=CRUDWindow()
            widget.addWidget(crud_window)
            widget.setCurrentIndex(widget.currentIndex()+1)
            # self.error.setText("Successfully Login")
        else:
            self.error.setText("Login Failed")

class SignUpScreen(QDialog):
    def __init__(self):
        super(SignUpScreen,self).__init__()
        loadUi("D:\program\python\PyQt5\signup.ui",self)
        self.login.clicked.connect(self.gotologin)
        self.signup.clicked.connect(self.signupUser)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        # self.username.setText("hi")

    def gotologin(self):
        login=LoginScreen()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def signupUser(self):
        email=self.username.text()
        pas=self.password.text()
        print(email,pas)

class CRUDWindow(QDialog):
    def __init__(self):
        super(CRUDWindow,self).__init__()
        loadUi("D:\program\python\PyQt5\\table.ui",self)
        self.showData()
        self.add_btn.clicked.connect(self.add)
        self.search_btn.clicked.connect(self.searchData)
        self.clear_btn.clicked.connect(self.clearField)
        self.delete_btn.clicked.connect(self.deleteData)
        self.update_btn.clicked.connect(self.updateData)
        self.delete_btn.setEnabled(False)
        self.update_btn.setEnabled(False)
        self.tableWidget.cellDoubleClicked.connect(self.searchData)
        self.comboBox_name.activated.connect(self.serchEmail)
        self.tableWidget.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        self.Id=0


    def add(self):
        name=self.lineEdit_name.text()
        phone=self.lineEdit_phone.text()
        email=self.lineEdit_email.text()
        if ((len(name)==0)or(len(email)==0))or(len(phone)!=10):
            # self.error.setText("Please Fill correct data in All Field")
            msg_1=QMessageBox()
            msg_1.setIcon(QMessageBox.Information)
            msg_1.setWindowTitle("Error")
            msg_1.setText("Please Fill correct data in All Field !")
            msg_1.exec_()
            return
        c=conn.cursor()
        query="INSERT INTO users (name,phone,email)VALUES(%s,%s,%s)"
        val=(name,phone,email)
        try:
            c.execute(query,val)
            conn.commit()
            c.close()
            self.clearField()
            self.showData()
        except:
            c.close()
            # self.error.setText("SQL Execution Failed !")
            msg_2=QMessageBox()
            msg_2.setIcon(QMessageBox.Information)
            msg_2.setWindowTitle("Error")
            msg_2.setText("SQL Execution Failed !")
            msg_2.exec_()
            return
        # self.error.setText("Successfully Added!")

    def deleteData(self):
        c=conn.cursor()
        query="DELETE FROM users WHERE id=%s"
        val=[self.Id]
        try:
            c.execute(query,val)
            conn.commit()
            c.close()
            self.clearField()
            self.showData()
        except:
            c.close()
            # self.error.setText("SQL Execution Failed !")
            msg_2=QMessageBox()
            msg_2.setIcon(QMessageBox.Information)
            msg_2.setWindowTitle("Error")
            msg_2.setText("SQL Execution Failed !")
            msg_2.exec_()
            return

    def searchData(self):
        try:
            self.index = self.tableWidget.selectedItems()
            value = (self.index[0].text())
        except:
            msg_3=QMessageBox()
            msg_3.setIcon(QMessageBox.Information)
            msg_3.setWindowTitle("Error")
            msg_3.setText("You have not selected any Row from Table !")
            msg_3.exec_()
            return
        query="SELECT * FROM users WHERE id=%s"
        c=conn.cursor()
        c.execute(query,[int(value)])
        result=c.fetchone()
        if result:
            self.lineEdit_name.setText(result[1])
            self.lineEdit_phone.setText(str(result[2]))
            self.lineEdit_email.setText(result[3])
            self.Id=result[0]
            index=self.comboBox_name.findText(result[1],QtCore.Qt.MatchFixedString)
            if index!=-1:
                self.comboBox_name.setCurrentIndex(index)
            self.delete_btn.setEnabled(True)
            self.update_btn.setEnabled(True)
            self.add_btn.setEnabled(False)
        c.close()
        print(self.dateEdit.date())
        print(self.dateEdit.date().day())
        print(self.dateEdit.date().month())
        print(self.dateEdit.date().year())

    def updateData(self):
        name=self.lineEdit_name.text()
        phone=self.lineEdit_phone.text()
        email=self.lineEdit_email.text()
        if ((len(name)==0)or(len(email)==0))or(len(phone)!=10):
            # self.error.setText("Please Fill correct data in All Field")
            msg_4=QMessageBox()
            msg_4.setIcon(QMessageBox.Information)
            msg_4.setWindowTitle("Error")
            msg_4.setText("Please Fill correct data in All Field !")
            msg_4.exec_()
            return
        c=conn.cursor()
        query="UPDATE users SET name=%s,phone=%s,email=%s WHERE id=%s"
        val=(name,phone,email,self.Id)
        try:
            c.execute(query,val)
            conn.commit()
            c.close()
            self.clearField()
            self.showData()
        except:
            c.close()
            # self.error.setText("SQL Execution Failed !")
            msg_5=QMessageBox()
            msg_5.setIcon(QMessageBox.Information)
            msg_5.setWindowTitle("Error")
            msg_5.setText("SQL Execution Failed !")
            msg_5.exec_()
            return
        self.clearField()
        self.showData()
        # date
        d = QDate(2020, 6, 10)
        # setting date to the date edit
        self.dateEdit.setDate(d)
        

    def clearField(self):
        self.lineEdit_name.setText("")
        self.lineEdit_phone.setText("")
        self.lineEdit_email.setText("")
        self.Id=0
        self.delete_btn.setEnabled(False)
        self.update_btn.setEnabled(False)
        self.add_btn.setEnabled(True)

    def selectedCell(self):
        self.index = self.tableWidget.selectedItems()
        value = (self.index[0].text())
        msg=QMessageBox()
        msg.setWindowTitle("Clicked")
        # msg.setIcon(QMessageBox.Critical)
        # msg.setIcon(QMessageBox.Warning)
        # msg.setIcon(QMessageBox.Information)
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Retry|QMessageBox.Abort|QMessageBox.Save)
        msg.setDefaultButton(QMessageBox.Abort)
        msg.setInformativeText("Informative Text, ya !")
        msg.setDetailedText("detailed text!")
        msg.setText(f"this is the main text, {value}!")
        msg.buttonClicked.connect(self.pop_upBtn_click)
        m=msg.exec_()

    def pop_upBtn_click(self,i):
        print(i.text())


    def showData(self):
        c=conn.cursor()
        c.execute("SELECT * FROM users")
        result=c.fetchall()
        self.tableWidget.setRowCount(0)
        self.comboBox_name.clear()
        for row_number,row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            # print(row_data)
            self.comboBox_name.addItem(row_data[1])
            for column_number,data in enumerate(row_data):
                # print(data)
                self.tableWidget.setItem(row_number,column_number,QtWidgets.QTableWidgetItem(str(data)))
        c.close()

    def serchEmail(self):
        name=self.comboBox_name.currentText()
        c=conn.cursor()
        query="SELECT email FROM users WHERE name=%s"
        val=[name]
        try:
            c.execute(query,val)
            result=c.fetchone()
        except:
            c.close()
            msg_6=QMessageBox()
            msg_6.setIcon(QMessageBox.Information)
            msg_6.setWindowTitle("Error")
            msg_6.setText("SQL Execution Failed !")
            msg_6.exec_()
            return
        self.comboBox_email.clear()
        self.comboBox_email.addItem(result[0])




        


# main
app = QApplication(sys.argv)
welcome = Activity()
# welcome.setWindowTitle("DBMS")
widget = QtWidgets.QStackedWidget()
widget.addWidget(welcome)
widget.setFixedHeight(820)
widget.setFixedWidth(821)
widget.show()
try:
    # conn.close()
    sys.exit(app.exec_())
except:
    conn.close()
    print("Exiting")

'''
QMessageBox.Ok
QMessageBox.Save
QMessageBox.Cancel
QMessageBox.Close
QMessageBox.Yes
QMessageBox.No
QMessageBox.Abort
QMessageBox.Retry
QMessageBox.Ignore
'''