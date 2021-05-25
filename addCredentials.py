import sqlite3
connection = sqlite3.connect('passwordManager.db')
cursor = connection.cursor()

import os
from dotenv import load_dotenv
load_dotenv()

from PyQt5 import QtCore, QtGui, QtWidgets

from cryptography.fernet import Fernet # For password encryption

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(608, 426)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.service = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(16)
        self.service.setFont(font)
        self.service.setAlignment(QtCore.Qt.AlignCenter)
        self.service.setObjectName("service")
        self.verticalLayout.addWidget(self.service)
        self.label_2 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.usernameOnService = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(16)
        self.usernameOnService.setFont(font)
        self.usernameOnService.setAlignment(QtCore.Qt.AlignCenter)
        self.usernameOnService.setObjectName("usernameOnService")
        self.verticalLayout.addWidget(self.usernameOnService)
        self.label_3 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.passwordForService = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(16)
        self.passwordForService.setFont(font)
        self.passwordForService.setAlignment(QtCore.Qt.AlignCenter)
        self.passwordForService.setObjectName("passwordForService")
        self.verticalLayout.addWidget(self.passwordForService)
        self.strongPassword = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.strongPassword.setFont(font)
        self.strongPassword.setObjectName("strongPassword")
        self.verticalLayout.addWidget(self.strongPassword)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem1)
        self.save = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.save.setFont(font)
        self.save.setObjectName("save")
        self.verticalLayout.addWidget(self.save)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.save.clicked.connect(self.saveCredentials)
        self.strongPassword.clicked.connect(self.generateStrongPassword)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Service"))
        self.label_2.setText(_translate("Dialog", "Username on the Service"))
        self.label_3.setText(_translate("Dialog", "Password for the Service"))
        self.strongPassword.setText(_translate("Dialog", "Generate Strong Password"))
        self.save.setText(_translate("Dialog", "Save Credentials"))

    def warn(self,msg):
        Dialog=QtWidgets.QMessageBox()
        Dialog.setText(msg)
        Dialog.setWindowTitle("Password Manager")
        Dialog.exec()

    def generateStrongPassword(self):
        from random import randrange

        strongPassword = ""
        for i in range(2):
            randomAscii = randrange(65, 91)
            strongPassword += chr(randomAscii)
        for i in range(6):
            randomAscii = randrange(97, 123)
            strongPassword += chr(randomAscii)
        randomAscii = randrange(35, 39)
        strongPassword += chr(randomAscii)
        for i in range(3):
            randomAscii = randrange(48, 58)
            strongPassword += chr(randomAscii)
        self.passwordForService.setText(strongPassword)

    def saveCredentials(self):
        currentUser = self.currentUser()
        service = self.service.text()
        usernameOnService = self.usernameOnService.text()
        password = self.passwordForService.text()

        if (service != '' and usernameOnService != '' and password != ''):

            # Password encryption to be done and then stored in database

            # Instance the Fernet class with the key which is already generated and stored
            # in the .env file

            key = os.getenv('KEY')
            fernet = Fernet(key)

            # then use the Fernet class instance 
            # to encrypt the string string must must 
            # be encoded to byte string before encryption
            encPassword = fernet.encrypt(password.encode())

            cursor.execute("INSERT INTO Credentials VALUES(?, ?, ?, ?);", (service, usernameOnService, encPassword, currentUser))
            connection.commit()
            self.warn("Your Credentials are saved Successfully and Securely")
            self.service.setText("")
            self.usernameOnService.setText("")
            self.passwordForService.setText("")
        else:
            self.warn("Please enter Service and Username and Password")

    def currentUser(self):
        cursor.execute("SELECT Username FROM LogInHistory;")
        userList = cursor.fetchall()
        currentUsername = userList[len(userList) - 1][0]
        return currentUsername


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
