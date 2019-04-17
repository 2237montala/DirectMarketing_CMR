from PyQt5 import QtCore, QtGui, QtWidgets
from UI_CreateAccount import *
from PyQt5.Qt import QLineEdit, QMainWindow
from DatabaseManager import DatabaseManager

account_info_table_name = "__ADMIN__Account_Info"
account_columns = ['Password','UserName','FirstName','LastName']

class Ui_LogIn_Page(QtWidgets.QWidget):

    valid_login_signal = QtCore.pyqtSignal()


    def __init__(self, db_file_loc):
        super().__init__()
        self.setup()
        self.db_file_loc = db_file_loc

    def Handle_CreateAccount(self):
        self.createAccountWidget = Ui_CreateAccount()
        self.createAccountWidget.create_account_done_signal.connect(self.create_account_closed)
        self.createAccountWidget.exec_()
        #self.hide()

    def Handle_LogIn(self):
        print("button pressed")
        db = DatabaseManager(self.db_file_loc)
        username = self.UserName_TXTfield.text()
        password = self.Password_TXTfield.text()

        try:
            if db.is_valid_string(username) and db.is_valid_string(password):
                #Both user name and password have to be valid strings to continue
                if not db.doesTableExist(account_info_table_name):
                    print("Must create account before")

                #Gets the account from the databse with the same password
                #If the isn't a match then it returns none
                row_with_entered_pass = db.get_row_at(account_info_table_name,column_name=account_columns[0],column_value=password)
                print(row_with_entered_pass)

                if not row_with_entered_pass == None:
                    #If the there is a password match then save the info
                    password_db = row_with_entered_pass[0]
                    user_name_db =row_with_entered_pass[1]

                    if password_db == password and user_name_db == username:
                        #If the user name and password entered match the
                        #user name and password in the db then it's a valid login
                        self.valid_login()
                    else:
                        ErrorBox = QtWidgets.QMessageBox()
                        ErrorBox.warning(self, 'No Account Found',
                                                    "No account found for the combination of user name and password",
                                                    ErrorBox.Ok)

                else:
                    ErrorBox = QtWidgets.QMessageBox()
                    ErrorBox.warning(self, 'No Account Found',
                                                "No account found for the combination of user name and password",
                                                ErrorBox.Ok)
            else:
                raise Exception()
        except:
            ErrorBox = QtWidgets.QMessageBox()
            ErrorBox.critical(self, 'Text Entry Error',
                                        "Text entries can only have letters numbers, and underscores",
                                        ErrorBox.Ok)

    def setup(self):
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
        self.label_2.setText(_translate("Form", "username:"))
        self.label_3.setText(_translate("Form", "Password:"))
        self.pushButton_CreateAccount.setText(_translate("Form", "Create Account"))
        self.pushButton_LogIn.setText(_translate("Form", "LogIn"))

    def create_account_closed(self, new_account_info):
        #Info comes in as first name, last name, user name, password
        print(new_account_info)

        temp = new_account_info.split('//')

        reformated_data=([0]*4)
        reformated_data[0]=temp[1]
        reformated_data[1]=temp[0]
        reformated_data[2]=temp[2]
        reformated_data[3]=temp[3]

        db = DatabaseManager(self.db_file_loc)

        if not db.doesTableExist(account_info_table_name):
            db.create_table_list(account_info_table_name,account_columns,'string')

        db.add_row_list(account_info_table_name,account_columns,reformated_data)

        self.show()

    def valid_login(self):
        print("Valid login\nEmitting signal")
        self.valid_login_signal.emit()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()

    ui = Ui_LogIn_Page('test.db')

    ui.show()
    sys.exit(app.exec_())
