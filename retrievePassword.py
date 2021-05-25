import sqlite3
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
        Dialog.resize(607, 428)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.seeAllServices = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.seeAllServices.setFont(font)
        self.seeAllServices.setObjectName("seeAllServices")
        self.verticalLayout.addWidget(self.seeAllServices)
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
        self.listWidget = QtWidgets.QListWidget(Dialog)
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(16)
        self.listWidget.setFont(font)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
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
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem1)
        self.usernameLabel = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(16)
        self.usernameLabel.setFont(font)
        self.usernameLabel.setObjectName("usernameLabel")
        self.verticalLayout.addWidget(self.usernameLabel)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem2)
        self.label_4 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem3)
        self.passwordLabel = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(16)
        self.passwordLabel.setFont(font)
        self.passwordLabel.setObjectName("passwordLabel")
        self.verticalLayout.addWidget(self.passwordLabel)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.seeAllServices.clicked.connect(self.displayServices)
        self.listWidget.itemDoubleClicked.connect(self.displayUsernameAndPassword)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.seeAllServices.setText(_translate("Dialog", "See All Services"))
        self.label.setText(_translate("Dialog", "Double Click to See Username and Password"))
        self.label_2.setText(_translate("Dialog", "Your Username"))
        self.label_4.setText(_translate("Dialog", "Your Password"))

    def displayServices(self):
        self.listWidget.clear()
        currentUser = self.currentUser()
        cursor.execute("SELECT Service FROM Credentials WHERE Username == '"+currentUser+"'")
        services = []
        while True:
            record = cursor.fetchone()
            if record == None:
                break
            services.append(record[0])
        self.listWidget.addItems(services)

    def currentUser(self):
        cursor.execute("SELECT Username FROM LogInHistory;")
        userList = cursor.fetchall()
        currentUsername = userList[len(userList) - 1][0]
        return currentUsername

    def displayUsernameAndPassword(self, item):
        selectedService = item.text()
        currentUser = self.currentUser()
        cursor.execute("SELECT UsernameOnService, Password FROM Credentials WHERE Username == '"+currentUser+"' and Service == '"+selectedService+"';")
        record = cursor.fetchone()

        # Instance the Fernet class with the key which is already generated and stored
        # in the .env file
        key = os.getenv('KEY')
        fernet = Fernet(key)

        # Decrypt the password which we have got from the database

        decMessage = fernet.decrypt(record[1]).decode()

        self.usernameLabel.setText(record[0])
        self.passwordLabel.setText(decMessage)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
