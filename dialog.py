# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CalendarDialouge.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    
    def __init__(self):
      super(Ui_Dialog, self).__init__()
    
    def handle_acceptClick(self):
        eventDate = self.DateLineEdit.text()
        eventEdit = self.textEdit.toPlainText()
#         print(eventDate)
#         print(eventEdit)
        #save information in both line edits
        Dialog.hide()
        
    def handle_rejectClick(self):
        Dialog.close()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(350, 400)
        Dialog.setAutoFillBackground(True)
        self.DateLabel = QtWidgets.QLabel(Dialog)
        self.DateLabel.setGeometry(QtCore.QRect(20, 20, 50, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.DateLabel.setFont(font)
        self.DateLabel.setObjectName("DateLabel")
        self.EventLabel = QtWidgets.QLabel(Dialog)
        self.EventLabel.setGeometry(QtCore.QRect(20, 60, 50, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.EventLabel.setFont(font)
        self.EventLabel.setObjectName("EventLabel")
        self.DateLineEdit = QtWidgets.QLineEdit(Dialog)
        self.DateLineEdit.setGeometry(QtCore.QRect(80, 20, 200, 25))
        self.DateLineEdit.setObjectName("DateLineEdit")
        self.AddAddressButton = QtWidgets.QPushButton(Dialog)
        self.AddAddressButton.setGeometry(QtCore.QRect(20, 305, 75, 25))
        self.AddAddressButton.setObjectName("AddAddressButton")
        self.AddGroupButton = QtWidgets.QPushButton(Dialog)
        self.AddGroupButton.setGeometry(QtCore.QRect(180, 305, 75, 25))
        self.AddGroupButton.setObjectName("AddGroupButton")
        self.AddressLabel = QtWidgets.QLabel(Dialog)
        self.AddressLabel.setGeometry(QtCore.QRect(105, 305, 75, 25))
        self.AddressLabel.setObjectName("AddressLabel")
        self.GroupLabel = QtWidgets.QLabel(Dialog)
        self.GroupLabel.setGeometry(QtCore.QRect(260, 305, 75, 25))
        self.GroupLabel.setObjectName("GroupLabel")
        self.ExampleLabel = QtWidgets.QLabel(Dialog)
        self.ExampleLabel.setGeometry(QtCore.QRect(80, 50, 115, 13))
        self.ExampleLabel.setObjectName("ExampleLabel")
        self.CancelButton = QtWidgets.QPushButton(Dialog)
        self.CancelButton.setGeometry(QtCore.QRect(260, 360, 75, 25))
        self.CancelButton.setObjectName("CancelButton")
        self.OkButton = QtWidgets.QPushButton(Dialog)
        self.OkButton.setGeometry(QtCore.QRect(180, 360, 75, 25))
        self.OkButton.setObjectName("OkButton")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(20, 95, 260, 200))
        self.textEdit.setObjectName("textEdit")
        
        self.retranslateUi(Dialog)
        self.OkButton.clicked.connect(self.handle_acceptClick)
        self.CancelButton.clicked.connect(self.handle_rejectClick)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.DateLabel.setText(_translate("Dialog", "Date"))
        self.EventLabel.setText(_translate("Dialog", "Event"))
        self.AddAddressButton.setText(_translate("Dialog", "Add Address"))
        self.AddGroupButton.setText(_translate("Dialog", "Add Group"))
        self.AddressLabel.setText(_translate("Dialog", "None"))
        self.GroupLabel.setText(_translate("Dialog", "None"))
        self.ExampleLabel.setText(_translate("Dialog", "Example: MM/DD/YY"))
        self.CancelButton.setText(_translate("Dialog", "Cancel"))
        self.OkButton.setText(_translate("Dialog", "OK"))


if __name__ == "__main__":
    global Dialog
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


