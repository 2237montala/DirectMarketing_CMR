# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LogIn_Window.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5 import QtGui

from ui_After_LogIn_Page import Ui_After_LogIn_Page
import sys
#import PyQt5


<<<<<<< HEAD
class Ui_MainWindow(object):
    
    def loginClicked(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_After_LogIn_Page()
        self.ui.setupUi(self.window)
        self.window.show()
        print('correct')
    
    def setupUi(self, MainWindow):
=======
class Ui_LogIn(object):
    #def __init__(self):
     #   super().__init__()
    def setupUi_LogIn(self, MainWindow):
>>>>>>> 8dd98511040fea55db4f0d1a688f0cd10bc84aec
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1650, 950)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1650, 200))
        font = QtGui.QFont()
        font.setPointSize(65)
        self.label.setFont(font)
        self.label.setAutoFillBackground(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(400, 300, 200, 50))
        self.label_2.setAutoFillBackground(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(400, 450, 200, 50))
        self.label_3.setAutoFillBackground(True)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(700, 600, 200, 50))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.loginClicked)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(650, 300, 400, 50))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(650, 450, 400, 50))
        self.lineEdit_2.setObjectName("lineEdit_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi1(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi1(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Chicago Turnkey Properties"))
        self.label_2.setText(_translate("MainWindow", "Username"))
        self.label_3.setText(_translate("MainWindow", "Password"))
        self.pushButton.setText(_translate("MainWindow", "Log In"))
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Ui_LogIn()
    #self.window = QWidget()
    #mainWindow = QMainWindow()
    mainWindow = QMainWindow()
    main.setupUi_LogIn(mainWindow)
    main.retranslateUi1(mainWindow)
    mainWindow.show()

    ex = main
    app.exec_()
