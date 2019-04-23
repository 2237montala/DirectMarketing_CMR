# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CreateAccount.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets
import re
#import numpy as np

class Ui_CreateAccount(QtWidgets.QDialog):
    create_account_done_signal = QtCore.pyqtSignal('QString')

    def __init__(self):
        super().__init__()
        self.setup()

    def setup(self):
        layout = QtWidgets.QVBoxLayout()

        title = QtWidgets.QLabel("Create Account",self)
        title.setAlignment(QtCore.Qt.AlignCenter)
        title.setFont(QtGui.QFont("Ariel",18,QtGui.QFont.Bold))

        reg_font = QtGui.QFont("Ariel",16)

        self.first_name_tf = QtWidgets.QLineEdit(self)
        self.first_name_tf.setPlaceholderText("First Name")
        self.first_name_tf.setFont(reg_font)

        self.last_name_tf = QtWidgets.QLineEdit(self)
        self.last_name_tf.setPlaceholderText("Last Name")
        self.last_name_tf.setFont(reg_font)

        self.user_name_tf = QtWidgets.QLineEdit(self)
        self.user_name_tf.setPlaceholderText("User Name")
        self.user_name_tf.setFont(reg_font)

        self.password_tf = QtWidgets.QLineEdit(self)
        self.password_tf.setPlaceholderText("Password")
        self.password_tf.setFont(reg_font)

        self.create_account_button = QtWidgets.QPushButton("Create Account",self)
        self.create_account_button.setFont(reg_font)
        self.create_account_button.clicked.connect(self.create_account)

        layout.addWidget(title)
        layout.addWidget(self.first_name_tf)
        layout.addWidget(self.last_name_tf)
        layout.addWidget(self.user_name_tf)
        layout.addWidget(self.password_tf)
        layout.addWidget(self.create_account_button)

        self.setLayout(layout)
        self.resize(self.sizeHint())

    #     self.resize(1118, 772)
    #     self.pushButton_BackToLogin = QtWidgets.QPushButton(self)
    #     self.pushButton_BackToLogin.setGeometry(QtCore.QRect(470, 540, 251, 41))
    #     font = QtGui.QFont()
    #     font.setPointSize(12)
    #     self.pushButton_BackToLogin.setFont(font)
    #     self.pushButton_BackToLogin.setObjectName("pushButton_BackToLogin")
    #     self.pushButton_BackToLogin.clicked.connect(self.Handle_BackToLogin)
    #     self.label_3 = QtWidgets.QLabel(self)
    #     self.label_3.setGeometry(QtCore.QRect(290, 480, 121, 31))
    #     font = QtGui.QFont()
    #     font.setPointSize(16)
    #     self.label_3.setFont(font)
    #     self.label_3.setObjectName("label_3")
    #     self.label = QtWidgets.QLabel(self)
    #     self.label.setGeometry(QtCore.QRect(420, 220, 431, 57))
    #     font = QtGui.QFont()
    #     font.setPointSize(28)
    #     self.label.setFont(font)
    #     self.label.setObjectName("label")
    #     self.UserName_TXTfield_CA = QtWidgets.QLineEdit(self)
    #     self.UserName_TXTfield_CA.setGeometry(QtCore.QRect(420, 410, 411, 51))
    #     self.UserName_TXTfield_CA.setObjectName("UserName_TXTfield_CA")
    #
    #     font = self.UserName_TXTfield_CA.font()
    #     font.setPointSize(15) # sets the size to 27
    #     self.UserName_TXTfield_CA.setFont(font)
    #
    #     self.label_2 = QtWidgets.QLabel(self)
    #     self.label_2.setGeometry(QtCore.QRect(270, 410, 141, 41))
    #     font = QtGui.QFont()
    #     font.setPointSize(16)
    #     self.label_2.setFont(font)
    #     self.label_2.setObjectName("label_2")
    #     self.Password_TXTfield_CA = QtWidgets.QLineEdit(self)
    #     self.Password_TXTfield_CA.setGeometry(QtCore.QRect(420, 470, 411, 51))
    #     self.Password_TXTfield_CA.setObjectName("Password_TXTfield_CA")
    #
    #     font = self.Password_TXTfield_CA.font()
    #     font.setPointSize(15) # sets the size to 27
    #     self.Password_TXTfield_CA.setFont(font)
    #
    #     #self.Password_TXTfield_CA.setEchoMode(QLineEdit.Password)
    #
    #     self.label_4 = QtWidgets.QLabel(self)
    #     self.label_4.setGeometry(QtCore.QRect(280, 360, 141, 31))
    #     font = QtGui.QFont()
    #     font.setPointSize(16)
    #     self.label_4.setFont(font)
    #     self.label_4.setObjectName("label_4")
    #     self.label_5 = QtWidgets.QLabel(self)
    #     self.label_5.setGeometry(QtCore.QRect(280, 290, 141, 41))
    #     font = QtGui.QFont()
    #     font.setPointSize(16)
    #     self.label_5.setFont(font)
    #     self.label_5.setObjectName("label_5")
    #     self.FirstName_TXTfield = QtWidgets.QLineEdit(self)
    #     self.FirstName_TXTfield.setGeometry(QtCore.QRect(420, 290, 411, 51))
    #     self.FirstName_TXTfield.setObjectName("FirstName_TXTfield")
    #
    #     font = self.FirstName_TXTfield.font()
    #     font.setPointSize(15) # sets the size to 27
    #     self.FirstName_TXTfield.setFont(font)
    #
    #     self.LastName_TXTfield = QtWidgets.QLineEdit(self)
    #     self.LastName_TXTfield.setGeometry(QtCore.QRect(420, 350, 411, 51))
    #     self.LastName_TXTfield.setObjectName("LastName_TXTfield")
    #
    #     font = self.LastName_TXTfield.font()
    #     font.setPointSize(15) # sets the size to 27
    #     self.LastName_TXTfield.setFont(font)
    #
    #     self.retranslateUi()
    #     self.customContextMenuRequested['QPoint'].connect(self.pushButton_BackToLogin.click)
    #     QtCore.QMetaObject.connectSlotsByName(self)
    #
    # def retranslateUi(self):
    #     _translate = QtCore.QCoreApplication.translate
    #     self.pushButton_BackToLogin.setText(_translate("Form", "Create Account"))
    #     self.label_3.setText(_translate("Form", "Password:"))
    #     self.label.setText(_translate("Form", "Create an Account"))
    #     self.label_2.setText(_translate("Form", "User Name:"))
    #     self.label_4.setText(_translate("Form", "Last Name:"))
    #     self.label_5.setText(_translate("Form", "First Name:"))

    def create_account(self):
        print('Getting text box values')
        UserInfo=([0]*4)

        UserInfo[0] = self.user_name_tf.text()
        UserInfo[1] = self.password_tf.text()
        UserInfo[2] = self.first_name_tf.text()
        UserInfo[3] = self.last_name_tf.text()

        emptyTextBoxes = False
        for str in UserInfo:
            if not re.match('^[A-Za-z0-9_]*$',str) or str == '':
                emptyTextBoxes = True
                break

        if emptyTextBoxes:
            ErrorBox = QtWidgets.QMessageBox()
            choice  = ErrorBox.critical(self, 'Text Entry Error',
                                        "Table name can only have letters numbers, and underscores",
                                        ErrorBox.Ok)
        else:
            signal_info_str = "//".join(UserInfo)
            self.create_account_done(signal_info_str)

    def create_account_done(self,account_info):
        print("Emiting signal")
        self.create_account_done_signal.emit(account_info)
        self.hide()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_CreateAccount()
    #ui.setup()
    ui.show()
    sys.exit(app.exec_())
