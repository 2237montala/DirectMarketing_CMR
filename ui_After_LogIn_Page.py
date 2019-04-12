# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'After_LogIn_Page.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5 import QtGui
import sys


#import PyQt5



class Ui_After_LogIn_Page(object):

    def setupUi(self, After_LogIn_Page):
        After_LogIn_Page.setObjectName("MainWindow")
        After_LogIn_Page.resize(1650, 950)
        self.centralwidget = QtWidgets.QWidget(After_LogIn_Page)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 825, 30))
        self.label.setAutoFillBackground(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(825, 0, 825, 30))
        self.label_2.setAutoFillBackground(True)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(700, 0, 100, 30))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.handleButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(600, 0, 100, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(500, 0, 100, 30))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(400, 0, 100, 30))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(1200, 0, 100, 30))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(1300, 0, 100, 30))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(1400, 0, 100, 30))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(1500, 0, 100, 30))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(25, 30, 75, 23))
        self.pushButton_9.setObjectName("pushButton_9")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(150, 100, 1350, 750))
        self.calendarWidget.setObjectName("calendarWidget")
        After_LogIn_Page.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar( After_LogIn_Page)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1650, 21))
        self.menubar.setObjectName("menubar")
        self.menuStuff = QtWidgets.QMenu(self.menubar)
        self.menuStuff.setObjectName("menuStuff")
        self.menudd = QtWidgets.QMenu(self.menubar)
        self.menudd.setObjectName("menudd")
        After_LogIn_Page.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar( After_LogIn_Page)
        self.statusbar.setObjectName("statusbar")
        After_LogIn_Page.setStatusBar(self.statusbar)
        self.actionThings = QtWidgets.QAction( After_LogIn_Page)
        self.actionThings.setObjectName("actionThings")
        self.actionddd = QtWidgets.QAction( After_LogIn_Page)
        self.actionddd.setObjectName("actionddd")
        self.actionkpdskkds = QtWidgets.QAction( After_LogIn_Page)
        self.actionkpdskkds.setObjectName("actionkpdskkds")
        self.menuStuff.addAction(self.actionThings)
        self.menuStuff.addAction(self.actionddd)
        self.menuStuff.addSeparator()
        self.menuStuff.addAction(self.actionkpdskkds)
        self.menubar.addAction(self.menuStuff.menuAction())
        self.menubar.addAction(self.menudd.menuAction())

        self.retranslateUi( After_LogIn_Page)
        QtCore.QMetaObject.connectSlotsByName( After_LogIn_Page)

    def retranslateUi(self,  After_LogIn_Page):
        _translate = QtCore.QCoreApplication.translate
        After_LogIn_Page.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Chicago Turnkey Properties"))
        self.label_2.setText(_translate("MainWindow", "Welcome back, ________"))
        self.pushButton.setText(_translate("MainWindow", "Documents"))
        self.pushButton_2.setText(_translate("MainWindow", "Create New Lead"))
        self.pushButton_3.setText(_translate("MainWindow", "Current Leads"))
        self.pushButton_4.setText(_translate("MainWindow", "Possible Leads"))
        self.pushButton_5.setText(_translate("MainWindow", "Home"))
        self.pushButton_6.setText(_translate("MainWindow", "Profile"))
        self.pushButton_7.setText(_translate("MainWindow", "Search"))
        self.pushButton_8.setText(_translate("MainWindow", "Logout"))
        self.pushButton_9.setText(_translate("MainWindow", "Refresh"))
        self.menuStuff.setTitle(_translate("MainWindow", "Stuff"))
        self.menudd.setTitle(_translate("MainWindow", "dd"))
        self.actionThings.setText(_translate("MainWindow", "Things"))
        self.actionddd.setText(_translate("MainWindow", "ddd"))
        self.actionkpdskkds.setText(_translate("MainWindow", "kpdskkds"))

    def handleButton(self):
        print('Button Clicked!')
        self.window = QtWidgets.QtMainWindow()
        print('Button Clicked!--------------------')
        self.ui = ui_LogIn()
        print('Button Clicked!')
        self.ui.setupUi_LogIn(self.window)
        print('Button Clicked!')
        self.window.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Ui_After_LogIn_Page()
    #self.window = QWidget()
    #mainWindow = QMainWindow()
    mainWindow = QMainWindow()
    main.setupUi(mainWindow)
    main.retranslateUi(mainWindow)
    mainWindow.show()

    ex = main
    app.exec_()
