from PyQt5 import QtCore, QtGui, QtWidgets
from UI_CreateAccount import *
from PyQt5.Qt import QLineEdit, QMainWindow
from DatabaseManager import DatabaseManager

#account_info_table_name = "Account_Info"
account_columns = ['Password','UserName','FirstName','LastName']

class Ui_LogIn_Page(QtWidgets.QWidget):
    valid_login_signal = QtCore.pyqtSignal()

    def __init__(self, db_file_loc, table_prefix):
        super().__init__()
        self.protected_table_prefix = table_prefix
        self.setup()
        self.db_file_loc = db_file_loc
        self.account_info_table_name = table_prefix + "Account_Info"
        print(self.account_info_table_name)

    def setup(self):
        self.setObjectName("Login_Page")
        layout = QtWidgets.QGridLayout()
        layout.setContentsMargins(5,5,5,5)

        #labels
        self.login_label = QtWidgets.QLabel("Welcome",self)
        self.login_label.setAlignment(QtCore.Qt.AlignCenter)
        self.login_label.setFont(QtGui.QFont("Ariel",18,QtGui.QFont.Bold))

        reg_font = QtGui.QFont("Ariel",16)

        #text fields
        self.user_name_tf = QtWidgets.QLineEdit(self)
        self.user_name_tf.setPlaceholderText("Username")
        self.user_name_tf.setMaximumSize(450,30)
        self.user_name_tf.setFont(reg_font)
        self.password_tf = QtWidgets.QLineEdit(self)
        self.password_tf.setPlaceholderText("Password")
        self.password_tf.setMaximumSize(450,30)
        self.password_tf.setFont(reg_font)

        #buttons
        self.login_button = QtWidgets.QPushButton(self)
        self.login_button.setText("Log In")
        self.login_button.setMaximumSize(125,30)
        self.login_button.setFont(reg_font)
        self.login_button.clicked.connect(self.Handle_LogIn)
        self.create_account_button = QtWidgets.QPushButton(self)
        self.create_account_button.setText("Create Account")
        self.create_account_button.setMaximumSize(325,30)
        self.create_account_button.setFont(reg_font)
        self.create_account_button.clicked.connect(self.Handle_CreateAccount)

        layout.addWidget(self.login_label,0,0,1,2)
        #layout.addWidget(self.user_name_label,1,0,1,1)
        layout.addWidget(self.user_name_tf,1,0,1,2)
        #layout.addWidget(self.password_label,2,0,1,1)
        layout.addWidget(self.password_tf,2,0,1,2)
        layout.addWidget(self.login_button,3,0,1,1)
        layout.addWidget(self.create_account_button,3,1,1,1)

        layout.setAlignment(QtCore.Qt.AlignCenter)

        self.setLayout(layout)
        self.resize(self.sizeHint())
        #self.setMaximumSize(1600,900)
    #
    #     self.resize(1119, 774)
    #     self.label = QtWidgets.QLabel(self)
    #     self.label.setGeometry(QtCore.QRect(240, 140, 571, 57))
    #     font = QtGui.QFont()
    #     font.setPointSize(28)
    #     self.label.setFont(font)
    #     self.label.setObjectName("label")
    #     self.label_2 = QtWidgets.QLabel(self)
    #     self.label_2.setGeometry(QtCore.QRect(240, 230, 131, 41))
    #     font = QtGui.QFont()
    #     font.setPointSize(16)
    #     self.label_2.setFont(font)
    #     self.label_2.setObjectName("label_2")
    #     self.label_3 = QtWidgets.QLabel(self)
    #     self.label_3.setGeometry(QtCore.QRect(240, 360, 151, 31))
    #     font = QtGui.QFont()
    #     font.setPointSize(16)
    #     self.label_3.setFont(font)
    #     self.label_3.setObjectName("label_3")
    #     self.UserName_TXTfield = QtWidgets.QLineEdit(self)
    #     self.UserName_TXTfield.setGeometry(QtCore.QRect(390, 230, 411, 51))
    #     self.UserName_TXTfield.setObjectName("UserName_TXTfield")
    #
    #     font = self.UserName_TXTfield.font()
    #     font.setPointSize(15) # sets the size to 27
    #     self.UserName_TXTfield.setFont(font)
    #
    #
    #     self.Password_TXTfield = QtWidgets.QLineEdit(self)
    #     self.Password_TXTfield.setGeometry(QtCore.QRect(390, 350, 411, 51))
    #     self.Password_TXTfield.setObjectName("Password_TXTfield")
    #
    #     font = self.Password_TXTfield.font()
    #     font.setPointSize(15) # sets the size to 27
    #     self.Password_TXTfield.setFont(font)
    #
    #     self.Password_TXTfield.setEchoMode(QLineEdit.Password)
    #
    #     self.pushButton_CreateAccount = QtWidgets.QPushButton(self)
    #     self.pushButton_CreateAccount.setGeometry(QtCore.QRect(560, 460, 191, 51))
    #     font = QtGui.QFont()
    #     font.setPointSize(12)
    #     self.pushButton_CreateAccount.setFont(font)
    #     self.pushButton_CreateAccount.setObjectName("pushButton_CreateAccount")
    #     self.pushButton_CreateAccount.clicked.connect(self.Handle_CreateAccount)
    #     self.pushButton_LogIn = QtWidgets.QPushButton(self)
    #     self.pushButton_LogIn.setGeometry(QtCore.QRect(330, 460, 191, 51))
    #     self.pushButton_LogIn.clicked.connect(self.Handle_LogIn)
    #     font = QtGui.QFont()
    #     font.setPointSize(12)
    #     self.pushButton_LogIn.setFont(font)
    #     self.pushButton_LogIn.setObjectName("pushButton_LogIn")
    #
    #     self.retranslateUi()
    #     QtCore.QMetaObject.connectSlotsByName(self)
    #
    # def retranslateUi(self):
    #     _translate = QtCore.QCoreApplication.translate
    #     self.setWindowTitle(_translate("Form", "Form"))
    #     self.label.setText(_translate("Form", "Chicago Turnkey Properties"))
    #     self.label_2.setText(_translate("Form", "username:"))
    #     self.label_3.setText(_translate("Form", "Password:"))
    #     self.pushButton_CreateAccount.setText(_translate("Form", "Create Account"))
    #     self.pushButton_LogIn.setText(_translate("Form", "LogIn"))

    def Handle_CreateAccount(self):
        self.createAccountWidget = Ui_CreateAccount()
        self.createAccountWidget.create_account_done_signal.connect(self.create_account_closed)
        self.createAccountWidget.exec_()
        #self.hide()

    def Handle_LogIn(self):
        print("button pressed")
        db = DatabaseManager(self.db_file_loc,self.protected_table_prefix)
        username = self.user_name_tf.text()
        password = self.password_tf.text()

        try:
            if db.is_valid_string(username) and db.is_valid_string(password):
                #Both user name and password have to be valid strings to continue
                if not db.doesTableExist(self.account_info_table_name):
                    print("Must create account before")

                #Gets the account from the databse with the same password
                #If the isn't a match then it returns none
                row_with_entered_pass = db.get_row_at(self.account_info_table_name,column_name=account_columns[0],column_value=password)
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



    def create_account_closed(self, new_account_info):
        #Info comes in as first name, last name, user name, password
        print(new_account_info)

        temp = new_account_info.split('//')

        reformated_data=([0]*4)
        reformated_data[0]=temp[1]
        reformated_data[1]=temp[0]
        reformated_data[2]=temp[2]
        reformated_data[3]=temp[3]

        db = DatabaseManager(self.db_file_loc,self.protected_table_prefix)

        if not db.doesTableExist(self.account_info_table_name):
            db.create_table_list(self.account_info_table_name,account_columns,'string')

        db.add_row_list(self.account_info_table_name,account_columns,reformated_data)

        self.show()

    def valid_login(self):
        print("Valid login\nEmitting signal")
        self.valid_login_signal.emit()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()

    ui = Ui_LogIn_Page('test.db','__ADMIN__')

    ui.show()
    sys.exit(app.exec_())
