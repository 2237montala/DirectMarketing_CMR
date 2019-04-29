# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CreateAccount.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets
import re
#import numpy as np

class UI_CreateAccount(QtWidgets.QDialog):
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
        self.password_tf.setEchoMode(QtWidgets.QLineEdit.Password)

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

    def create_account(self):
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
        self.create_account_done_signal.emit(account_info)
        self.hide()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = UI_CreateAccount()
    #ui.setup()
    ui.show()
    sys.exit(app.exec_())
