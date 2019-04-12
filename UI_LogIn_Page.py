from PyQt5 import QtCore, QtGui, QtWidgets
from UI_CreateAccount import *
from ui_After_LogIn_Page import*
from PyQt5.Qt import QLineEdit, QMainWindow

class Ui_LogIn_Page(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()


    def Handle_CreateAccount(self):
        print("hello 1")
        self.createAccountWidget = Ui_CreateAccount()
        self.createAccountWidget.setup()
        self.window.show()
        print("hello tester")

    def Handle_LogIn(self):
        print("button pressed")
        LoginInfo=([0]*2)
        Username = self.UserName_TXTfield.text()
        password = self.Password_TXTfield.text()
        print('read')
        f=open("username_password.txt",'r')
        print('file opened')
        UserInfo = {}
        for line in f:
            x=line.split(";")
            a=x[0]
            b=x[1]
            UserInfo[a]=b
        print('dict made')
        print(UserInfo)
        
        if UserInfo[Username]==password:
            print('match found')
            self.window = QtWidgets.QMainWindow()
            print("test 1")
            self.ui = Ui_After_LogIn_Page()
            print("test 2")
            self.ui.setup2(self.window)
            print("test 3")
            self.window.show()
            print("test 4")
            self.hide()
            print("test 5")

    def setup(self):
        print("Hello whats up has to show twice")
        self.setObjectName("window")
        self.resize(1119, 774)
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(240, 140, 571, 57))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(240, 230, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(240, 360, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.UserName_TXTfield = QtWidgets.QLineEdit(self)
        self.UserName_TXTfield.setGeometry(QtCore.QRect(390, 230, 411, 51))
        self.UserName_TXTfield.setObjectName("UserName_TXTfield")

        font = self.UserName_TXTfield.font()
        font.setPointSize(15) # sets the size to 27
        self.UserName_TXTfield.setFont(font)


        self.Password_TXTfield = QtWidgets.QLineEdit(self)
        self.Password_TXTfield.setGeometry(QtCore.QRect(390, 350, 411, 51))
        self.Password_TXTfield.setObjectName("Password_TXTfield")

        font = self.Password_TXTfield.font()
        font.setPointSize(15) # sets the size to 27
        self.Password_TXTfield.setFont(font)

        self.Password_TXTfield.setEchoMode(QLineEdit.Password)

        self.pushButton_CreateAccount = QtWidgets.QPushButton(self)
        self.pushButton_CreateAccount.setGeometry(QtCore.QRect(560, 460, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_CreateAccount.setFont(font)
        self.pushButton_CreateAccount.setObjectName("pushButton_CreateAccount")
        self.pushButton_CreateAccount.clicked.connect(self.Handle_CreateAccount)
        self.pushButton_LogIn = QtWidgets.QPushButton(self)
        self.pushButton_LogIn.setGeometry(QtCore.QRect(330, 460, 191, 51))
        self.pushButton_LogIn.clicked.connect(self.Handle_LogIn)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_LogIn.setFont(font)
        self.pushButton_LogIn.setObjectName("pushButton_LogIn")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Chicago Turnkey Properties"))
        self.label_2.setText(_translate("Form", "Username:"))
        self.label_3.setText(_translate("Form", "Password:"))
        self.pushButton_CreateAccount.setText(_translate("Form", "Create Account"))
        self.pushButton_LogIn.setText(_translate("Form", "LogIn"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()

    ui = Ui_LogIn_Page()
    ui.setup()
    ui.show()
    sys.exit(app.exec_())
