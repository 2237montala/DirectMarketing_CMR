# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CalendarDialouge.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from DatabaseManager import DatabaseManager
from file_browser import file_browser
from csv_importer import csv_importer_popup

# column header names
Event_Columns = ['Date', 'Event', 'Address', 'Group']

class Ui_Dialog(QtWidgets.QDialog):
    calendar_dialog_signal = QtCore.pyqtSignal()
    
    def __init__(self, db_file, protected_table_prefix):
        try:
              super().__init__()
              self.setupUi()
              self.protected_table_prefix = protected_table_prefix
              self.db = DatabaseManager(db_file,self.protected_table_prefix)
              self.db_file_loc = db_file
              self.event_info_table_name = protected_table_prefix + "Event_Information"
        except Exception as er:
            print('Error message:', er.args[0])
            return False
    # creates method for the ok button that creates variables holding the date and event text typed by the user
    # it will also save the information into the table
    def handle_acceptClick(self):
        eventDate = self.DateLineEdit.text()
        eventEdit = self.textEdit.toPlainText()
#         print(eventDate)
        #print(eventEdit)
        event_data = ([0]*4)
        event_data[0] = eventDate
        event_data[1] = eventEdit
        event_data[2] = ""
        event_data[3] = ""
        # database stuff
        try:
            if not self.db.doesTableExist(self.event_info_table_name):
                self.db.create_table_list(self.event_info_table_name,Event_Columns,'string')
            self.db.add_row_list(self.event_info_table_name,Event_Columns,event_data)
            self.calendar_dialog_signal.emit()
            self.close()
        except Exception as er:
            print('Error message:', er.args[0])
            return False
        
    # creates method for the cancel button that closes the dialog and leaves the calendar widget open
    def handle_rejectClick(self):
        self.close()
        
    # creates method for the add address button for the dialog and opens something to add an address for the event
    def handle_addAddressButton(self):
        self.close()
        
    # creates method for the add group button for the dialog and opens something to add a group for the event
    def handle_addGroupButton(self):
        self.close()

    # auto generated code from Qt Designer that creates all the entities for the calendar dialog and their parameters
    def setupUi(self):
        self.setObjectName("Dialog")
        self.resize(350, 400)
        self.setAutoFillBackground(True)
        self.DateLabel = QtWidgets.QLabel(self)
        self.DateLabel.setGeometry(QtCore.QRect(20, 20, 50, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.DateLabel.setFont(font)
        self.DateLabel.setObjectName("DateLabel")
        self.EventLabel = QtWidgets.QLabel(self)
        self.EventLabel.setGeometry(QtCore.QRect(20, 60, 50, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.EventLabel.setFont(font)
        self.EventLabel.setObjectName("EventLabel")
        self.DateLineEdit = QtWidgets.QLineEdit(self)
        self.DateLineEdit.setGeometry(QtCore.QRect(80, 20, 200, 25))
        self.DateLineEdit.setObjectName("DateLineEdit")
        self.AddAddressButton = QtWidgets.QPushButton(self)
        self.AddAddressButton.setGeometry(QtCore.QRect(20, 305, 75, 25))
        self.AddAddressButton.setObjectName("AddAddressButton")
        self.AddGroupButton = QtWidgets.QPushButton(self)
        self.AddGroupButton.setGeometry(QtCore.QRect(180, 305, 75, 25))
        self.AddGroupButton.setObjectName("AddGroupButton")
        self.AddressLabel = QtWidgets.QLabel(self)
        self.AddressLabel.setGeometry(QtCore.QRect(105, 305, 75, 25))
        self.AddressLabel.setObjectName("AddressLabel")
        self.GroupLabel = QtWidgets.QLabel(self)
        self.GroupLabel.setGeometry(QtCore.QRect(260, 305, 75, 25))
        self.GroupLabel.setObjectName("GroupLabel")
        self.ExampleLabel = QtWidgets.QLabel(self)
        self.ExampleLabel.setGeometry(QtCore.QRect(80, 50, 115, 13))
        self.ExampleLabel.setObjectName("ExampleLabel")
        self.CancelButton = QtWidgets.QPushButton(self)
        self.CancelButton.setGeometry(QtCore.QRect(260, 360, 75, 25))
        self.CancelButton.setObjectName("CancelButton")
        self.OkButton = QtWidgets.QPushButton(self)
        self.OkButton.setGeometry(QtCore.QRect(180, 360, 75, 25))
        self.OkButton.setObjectName("OkButton")
        self.textEdit = QtWidgets.QTextEdit(self)
        self.textEdit.setGeometry(QtCore.QRect(20, 95, 260, 200))
        self.textEdit.setObjectName("textEdit")
        
        self.retranslateUi()
        
        # creates the signal for the ok and reject buttons and connects them with their corresponding functions
        self.OkButton.clicked.connect(self.handle_acceptClick)
        self.CancelButton.clicked.connect(self.handle_rejectClick)
        self.AddAddressButton.clicked.connect(self.handle_addAddressButton)
        self.AddGroupButton.clicked.connect(self.handle_addGroupButton)
        QtCore.QMetaObject.connectSlotsByName(self)

    # auto generated code from Qt Designer
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Dialog"))
        self.DateLabel.setText(_translate("Dialog", "Date"))
        self.EventLabel.setText(_translate("Dialog", "Event"))
        self.AddAddressButton.setText(_translate("Dialog", "Add Address"))
        self.AddGroupButton.setText(_translate("Dialog", "Add Group"))
        self.AddressLabel.setText(_translate("Dialog", "None"))
        self.GroupLabel.setText(_translate("Dialog", "None"))
        self.ExampleLabel.setText(_translate("Dialog", "Example: MM-DD-YY"))
        self.CancelButton.setText(_translate("Dialog", "Cancel"))
        self.OkButton.setText(_translate("Dialog", "OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Dialog('test.db','__ADMIN__')
    ui.show()
    sys.exit(app.exec_())


