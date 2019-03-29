# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LogIn_Page.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from UI_CreateAccount import Ui_CreateAccount

class Ui_Form(object):
    
    def handleButton(self):
        print('hello')
        self.window = QtWidgets.QMainWindow()
        print('hel')
        self.ui = Ui_CreateAccount()
        print('hell')
        self.ui.setupUi1(self.window)
        self.window.show()
    
    
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1119, 774)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(240, 140, 571, 57))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(240, 230, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(240, 360, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.UserName_TXTfield = QtWidgets.QTextBrowser(Form)
        self.UserName_TXTfield.setGeometry(QtCore.QRect(390, 230, 411, 51))
        self.UserName_TXTfield.setObjectName("UserName_TXTfield")
        self.Password_TXTfield = QtWidgets.QTextBrowser(Form)
        self.Password_TXTfield.setGeometry(QtCore.QRect(390, 350, 411, 51))
        self.Password_TXTfield.setObjectName("Password_TXTfield")
        self.pushButton_CreateAccount = QtWidgets.QPushButton(Form)
        self.pushButton_CreateAccount.setGeometry(QtCore.QRect(560, 460, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_CreateAccount.setFont(font)
        self.pushButton_CreateAccount.setObjectName("pushButton_CreateAccount")
        self.pushButton_CreateAccount.clicked.connect(self.handleButton)
        self.pushButton_LogIn = QtWidgets.QPushButton(Form)
        self.pushButton_LogIn.setGeometry(QtCore.QRect(330, 460, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_LogIn.setFont(font)
        self.pushButton_LogIn.setObjectName("pushButton_LogIn")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Chicago Turnkey Properties"))
        self.label_2.setText(_translate("Form", "Username:"))
        self.label_3.setText(_translate("Form", "Password:"))
        self.UserName_TXTfield.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.Password_TXTfield.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton_CreateAccount.setText(_translate("Form", "Create Account"))
        self.pushButton_LogIn.setText(_translate("Form", "LogIn"))

        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
