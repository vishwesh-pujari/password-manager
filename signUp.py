import sqlite3 # for database
connection = sqlite3.connect('passwordManager.db')
cursor = connection.cursor()

import os
from dotenv import load_dotenv
load_dotenv()

from cryptography.fernet import Fernet # For password encryption

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(604, 415)
        self.formLayoutWidget = QtWidgets.QWidget(Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 120, 581, 170))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.username = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.username.setFont(font)
        self.username.setAlignment(QtCore.Qt.AlignCenter)
        self.username.setObjectName("username")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.username)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.setPassword = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.setPassword.setFont(font)
        self.setPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.setPassword.setAlignment(QtCore.Qt.AlignCenter)
        self.setPassword.setObjectName("setPassword")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.setPassword)
        self.confirmPassword = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.confirmPassword.setFont(font)
        self.confirmPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmPassword.setAlignment(QtCore.Qt.AlignCenter)
        self.confirmPassword.setObjectName("confirmPassword")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.confirmPassword)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout.setItem(3, QtWidgets.QFormLayout.LabelRole, spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout.setItem(5, QtWidgets.QFormLayout.LabelRole, spacerItem1)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 20, 581, 38))
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.signUp = QtWidgets.QPushButton(Dialog)
        self.signUp.setGeometry(QtCore.QRect(210, 300, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.signUp.setFont(font)
        self.signUp.setObjectName("signUp")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.signUp.clicked.connect(self.getInfo)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Username"))
        self.label_4.setText(_translate("Dialog", "Confirm Password"))
        self.label_2.setText(_translate("Dialog", "Set Password"))
        self.label_3.setText(_translate("Dialog", "Sign Up"))
        self.signUp.setText(_translate("Dialog", "Sign Up"))

    def warn(self,msg):
        Dialog=QtWidgets.QMessageBox()
        Dialog.setText(msg)
        Dialog.setWindowTitle("Password Manager")
        Dialog.exec()

    def getInfo(self):
        if (self.username.text() != '' and self.setPassword.text() != '' and self.confirmPassword.text() != ''):
            if (self.setPassword.text() != self.confirmPassword.text()):
                self.warn("Passwords Don't Match. Please try again.")
                self.setPassword.setText("")
                self.confirmPassword.setText("")
            else :
                username = self.username.text()
                if (not (self.validateUsername(username))):
                    self.warn("There exists an account having same username. Cannot sign up")
                else:   
                    """password = self.setPassword.text()
                    cursor.execute("INSERT INTO Users VALUES(?,?);", (username, password))
                    connection.commit()
                    self.warn("Sign-Up Done Successfully. Log into your account now")"""

                    password = self.setPassword.text()

                    # Password encryption to be done and then stored in database

                    # Instance the Fernet class with the key which is already generated and stored
            # in the .env file
                    key = os.getenv('KEY')
                    fernet = Fernet(key)

                    # then use the Fernet class instance 
                    # to encrypt the string string must must 
                    # be encoded to byte string before encryption
                    encPassword = fernet.encrypt(password.encode())

                    cursor.execute("INSERT INTO Users VALUES(?,?);", (username, encPassword))
                    connection.commit()
                    self.warn("Sign-Up Done Successfully. Log into your account now")
        else:
            self.warn("Please Enter Username and Password")
    
    def validateUsername(self, username):
        cursor.execute("SELECT Username FROM Users")
        usernames = cursor.fetchall()
        for i in range(len(usernames)):
            if (username == usernames[i][0]):
                return False
        return True

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
