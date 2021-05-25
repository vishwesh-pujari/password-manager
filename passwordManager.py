"""Main File of Password Manager"""

import sqlite3
connection = sqlite3.connect('passwordManager.db')
cursor = connection.cursor()

import os
from dotenv import load_dotenv
load_dotenv()

from cryptography.fernet import Fernet # For password encryption

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(612, 428)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.username = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.username.setFont(font)
        self.username.setText("")
        self.username.setAlignment(QtCore.Qt.AlignCenter)
        self.username.setObjectName("username")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.username)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.password.setFont(font)
        self.password.setText("")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setAlignment(QtCore.Qt.AlignCenter)
        self.password.setObjectName("password")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.password)
        self.verticalLayout.addLayout(self.formLayout)
        self.logIn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.logIn.setFont(font)
        self.logIn.setObjectName("logIn")
        self.verticalLayout.addWidget(self.logIn)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem2)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.signUp = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.signUp.setFont(font)
        self.signUp.setObjectName("signUp")
        self.verticalLayout.addWidget(self.signUp)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 612, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.signUp.clicked.connect(self.signUpPopUp)
        self.logIn.clicked.connect(self.logInPopUp)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_5.setText(_translate("MainWindow", "Welcome to Password Manager"))
        self.label_6.setText(_translate("MainWindow", "Go Ahead and Forget Your Passwords!!"))
        self.label_3.setText(_translate("MainWindow", "Log-In"))
        self.label.setText(_translate("MainWindow", "Username"))
        self.label_2.setText(_translate("MainWindow", "Password"))
        self.logIn.setText(_translate("MainWindow", "Log In"))
        self.label_4.setText(_translate("MainWindow", "Don\'t have an account? Sign Up"))
        self.signUp.setText(_translate("MainWindow", "Sign Up"))

    def warn(self,msg):
        Dialog=QtWidgets.QMessageBox()
        Dialog.setText(msg)
        Dialog.setWindowTitle("Password Manager")
        Dialog.exec()

    def signUpPopUp(self):
        from signUp import Ui_Dialog
        Dialog = QtWidgets.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog)
        ret = Dialog.exec()

    def logInPopUp(self):
        if (self.username.text() != '' and self.password.text() != ''):
            if (not (self.validateUsername())):
                self.warn("Invalid Username")
            elif (not (self.validatePassword())):
                self.warn("Invalid Password. Please try again")
            else:
                cursor.execute("INSERT INTO LogInHistory VALUES('"+self.username.text()+"');")
                connection.commit()
                from afterLogIn import Ui_Dialog
                Dialog = QtWidgets.QDialog()
                ui = Ui_Dialog()
                ui.setupUi(Dialog)
                ret = Dialog.exec()
        else:
            self.warn("Please Enter Username and Password")

    def validateUsername(self):
        cursor.execute("SELECT Username FROM Users")
        usernames = cursor.fetchall()
        username = self.username.text()
        for i in range(len(usernames)):
            if (username == usernames[i][0]):
                return True
        return False

    def validatePassword(self):
        username = self.username.text()
        password = self.password.text()

        cursor.execute("SELECT Password FROM Users WHERE Username == '"+username+"'")
        correctPassword = cursor.fetchone()

        # Instance the Fernet class with the key which is already generated and stored
            # in the .env file

        key = os.getenv('KEY')
        fernet = Fernet(key)

        # Decrypt the password which we have got from the database

        decMessage = fernet.decrypt(correctPassword[0]).decode()

        #if (correctPassword[0] != password):
        #    return False
        if (decMessage != password):
            return False
        else:
            return True

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
