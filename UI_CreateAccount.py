# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CreateAccount.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets
#import numpy as np

class Ui_CreateAccount(QtWidgets.QWidget):

    def Handle_BackToLogin (self):
        UserInfo=([0]*4)

        UserInfo[0] = self.UserName_TXTfield_CA.text()
        UserInfo[1] = self.Password_TXTfield_CA.text()
        UserInfo[2] = self.FirstName_TXTfield.text()
        UserInfo[3] = self.LastName_TXTfield.text()
        f=open("username_password.txt","a+")
        print("file opened")
        for i in range(2):
            f.write(UserInfo[i] + ";")
        f.write("\n")
        f.close
        print("hello 2")
        self.window = QtWidgets.QMainWindow()
        print("hello 3")
        self.ui = Ui_LogIn_Page()
        print("hello 4")
        self.ui.setupUi3(self.window)

        self.window.show()
        print("hello 6")
        Form1.hide()
        print("hello 7")


    def setup(self, Form):
        Form.setObjectName("Form")
        Form.resize(1118, 772)
        self.pushButton_BackToLogin = QtWidgets.QPushButton(Form)
        self.pushButton_BackToLogin.setGeometry(QtCore.QRect(470, 540, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_BackToLogin.setFont(font)
        self.pushButton_BackToLogin.setObjectName("pushButton_BackToLogin")
        self.pushButton_BackToLogin.clicked.connect(self.Handle_BackToLogin)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(290, 480, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(420, 220, 431, 57))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.UserName_TXTfield_CA = QtWidgets.QLineEdit(Form)
        self.UserName_TXTfield_CA.setGeometry(QtCore.QRect(420, 410, 411, 51))
        self.UserName_TXTfield_CA.setObjectName("UserName_TXTfield_CA")

        font = self.UserName_TXTfield_CA.font()
        font.setPointSize(15) # sets the size to 27
        self.UserName_TXTfield_CA.setFont(font)

        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(270, 410, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.Password_TXTfield_CA = QtWidgets.QLineEdit(Form)
        self.Password_TXTfield_CA.setGeometry(QtCore.QRect(420, 470, 411, 51))
        self.Password_TXTfield_CA.setObjectName("Password_TXTfield_CA")

        font = self.Password_TXTfield_CA.font()
        font.setPointSize(15) # sets the size to 27
        self.Password_TXTfield_CA.setFont(font)

        #self.Password_TXTfield_CA.setEchoMode(QLineEdit.Password)

        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(280, 360, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(280, 290, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.FirstName_TXTfield = QtWidgets.QLineEdit(Form)
        self.FirstName_TXTfield.setGeometry(QtCore.QRect(420, 290, 411, 51))
        self.FirstName_TXTfield.setObjectName("FirstName_TXTfield")

        font = self.FirstName_TXTfield.font()
        font.setPointSize(15) # sets the size to 27
        self.FirstName_TXTfield.setFont(font)

        self.LastName_TXTfield = QtWidgets.QLineEdit(Form)
        self.LastName_TXTfield.setGeometry(QtCore.QRect(420, 350, 411, 51))
        self.LastName_TXTfield.setObjectName("LastName_TXTfield")

        font = self.LastName_TXTfield.font()
        font.setPointSize(15) # sets the size to 27
        self.LastName_TXTfield.setFont(font)

        self.retranslateUi(Form)
        Form.customContextMenuRequested['QPoint'].connect(self.pushButton_BackToLogin.click)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_BackToLogin.setText(_translate("Form", "Create Account"))
        self.label_3.setText(_translate("Form", "Password:"))
        self.label.setText(_translate("Form", "Create an Account"))
#===============================================================================
#         self.UserName_TXTfield_CA.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
# "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
# "p, li { white-space: pre-wrap; }\n"
# "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
# "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_2.setText(_translate("Form", "User Name:"))
#         self.Password_TXTfield_CA.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
# "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
# "p, li { white-space: pre-wrap; }\n"
# "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
# "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_4.setText(_translate("Form", "Last Name:"))
        self.label_5.setText(_translate("Form", "First Name:"))
#         self.FirstName_TXTfield.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
# "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
# "p, li { white-space: pre-wrap; }\n"
# "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
# "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
#         self.LastName_TXTfield.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
# "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
# "p, li { white-space: pre-wrap; }\n"
# "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
# "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
#===============================================================================





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form1 = QtWidgets.QWidget()
    ui = Ui_CreateAccount()
    ui.setup(Form1)
    Form1.show()
    sys.exit(app.exec_())