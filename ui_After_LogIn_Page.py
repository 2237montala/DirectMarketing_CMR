# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'After_LogIn_Page.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!
# Form implementation generated from reading ui file 'CalendarforSMP.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate, QDateTime
from PyQt5.QtWidgets import QCalendarWidget, QDateEdit
from dialog import *
from ui_ProfilePage import *
from calendar import calendar

from DatabaseManager import DatabaseManager
from file_browser import file_browser
from csv_importer import csv_importer_popup

class Ui_CalendarForm(object):
    
    def __init__(self):
      super(Ui_CalendarForm, self).__init__()
      self.setupUi(CalendarForm)
    
    def EventButton_handler(self):
        self.updateWindow=QtWidgets.QDialogButtonBox()
        self.ui_update = Ui_Dialog()
        self.ui_update.setupUi(self.updateWindow)
        self.updateWindow.show()
        
    def handle_listsPageButton(self):
        print("clicked")
        #self.window2 = QtWidgets.QMainWindow()
        #self.ui2 = whatever the right window is
        #self.ui2.name of class
        #self.window2.show()
        #CalendarForm.hide()
        print("made it")
        
    def handle_profilePageButton(self):
        print("clicked")
        self.window3 = QtWidgets.QWidget()
        self.ui3 = ui_ProfilePage()
        self.ui3.setupUi(self.window3)
        self.window3.show()
        CalendarForm.hide()
        print("made it")
        
    def handle_searchPageButton(self):
        print("clicked")
        #self.window4 = QtWidgets.QMainWindow()
        #self.ui4 = 
        #self.ui4.classname(self.window4)
        #self.window4.show()
        #CalendarForm.hide()
        print("made it")
        
    def handle_homePageButton(self):
        CalendarForm.update()
    
    def handle_refreshButton(self):
        CalendarForm.update()
    
    def showDate(self, date):
        self.label.setText(date.toString("MM-dd-yy"))
        
    def load_from_csv_table(self, date):
        print("should start loading")
        #self.label_3.setText(events)
        
    def setupUi(self, CalendarForm):
        CalendarForm.setObjectName("CalendarForm")
        CalendarForm.setEnabled(True)
        CalendarForm.resize(1650, 950)
        CalendarForm.setLayoutDirection(QtCore.Qt.LeftToRight)
        CalendarForm.setAutoFillBackground(True)
        self.CompNameLabel = QtWidgets.QLabel(CalendarForm)
        self.CompNameLabel.setGeometry(QtCore.QRect(0, 0, 300, 75))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.CompNameLabel.setFont(font)
        self.CompNameLabel.setAutoFillBackground(True)
        self.CompNameLabel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.CompNameLabel.setFrameShadow(QtWidgets.QFrame.Plain)
        self.CompNameLabel.setTextFormat(QtCore.Qt.AutoText)
        self.CompNameLabel.setScaledContents(False)
        self.CompNameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.CompNameLabel.setWordWrap(False)
        self.CompNameLabel.setObjectName("CompNameLabel")
        self.calendar = QtWidgets.QCalendarWidget(CalendarForm)
        self.calendar.setGeometry(QtCore.QRect(75, 175, 750, 700))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.calendar.setFont(font)
        self.calendar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.calendar.setAutoFillBackground(True)
        self.calendar.setFirstDayOfWeek(QtCore.Qt.Sunday)
        self.calendar.setGridVisible(True)
        self.calendar.setSelectionMode(QtWidgets.QCalendarWidget.SingleSelection)
        self.calendar.setHorizontalHeaderFormat(QtWidgets.QCalendarWidget.LongDayNames)
        self.calendar.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.calendar.setNavigationBarVisible(True)
        self.calendar.setDateEditEnabled(True)
        self.calendar.setObjectName("calendar")
        self.horizontalLayoutWidget = QtWidgets.QWidget(CalendarForm)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(1410, 100, 160, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.RefreshButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.RefreshButton.setObjectName("RefreshButton")
        self.horizontalLayout.addWidget(self.RefreshButton)
        self.EventButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.EventButton.setIconSize(QtCore.QSize(20, 20))
        self.EventButton.setCheckable(False)
        self.EventButton.setAutoRepeat(False)
        self.EventButton.setAutoDefault(False)
        self.EventButton.setFlat(False)
        self.EventButton.setObjectName("EventButton")
        self.horizontalLayout.addWidget(self.EventButton)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(CalendarForm)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(1110, 0, 461, 76))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.HomePageButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.HomePageButton.setObjectName("HomePageButton")
        self.horizontalLayout_2.addWidget(self.HomePageButton)
        self.ListsPageButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.ListsPageButton.setObjectName("ListsPageButton")
        self.horizontalLayout_2.addWidget(self.ListsPageButton)
        self.SearchPageButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.SearchPageButton.setObjectName("SearchPageButton")
        self.horizontalLayout_2.addWidget(self.SearchPageButton)
        self.ProfilePageButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.ProfilePageButton.setObjectName("ProfilePageButton")
        self.horizontalLayout_2.addWidget(self.ProfilePageButton)
        self.label = QtWidgets.QLabel(CalendarForm)
        self.label.setGeometry(QtCore.QRect(925, 200, 645, 100))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAutoFillBackground(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(CalendarForm)
        self.label_2.setGeometry(QtCore.QRect(925, 350, 100, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAutoFillBackground(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(CalendarForm)
        self.label_3.setGeometry(QtCore.QRect(1025, 350, 500, 425))
        self.label_3.setAutoFillBackground(True)
        self.label_3.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(CalendarForm)
        self.label_4.setGeometry(QtCore.QRect(925, 775, 100, 50))
        font = QtGui.QFont()
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setAutoFillBackground(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(CalendarForm)
        self.label_5.setGeometry(QtCore.QRect(925, 825, 100, 50))
        font = QtGui.QFont()
        font.setUnderline(True)
        self.label_5.setFont(font)
        self.label_5.setAutoFillBackground(True)
        self.label_5.setObjectName("label_5")
        
        self.retranslateUi(CalendarForm) 
        self.calendar.clicked[QtCore.QDate].connect(self.showDate)
        self.calendar.clicked[QtCore.QDate].connect(self.load_from_csv_table)
        date = self.calendar.selectedDate()
        self.ListsPageButton.clicked.connect(self.handle_listsPageButton)
        self.ProfilePageButton.clicked.connect(self.handle_profilePageButton)
        self.SearchPageButton.clicked.connect(self.handle_searchPageButton)
        self.HomePageButton.clicked.connect(self.handle_homePageButton)
        self.RefreshButton.clicked.connect(self.handle_refreshButton)
        self.EventButton.clicked.connect(self.EventButton_handler)
        QtCore.QMetaObject.connectSlotsByName(CalendarForm)

    def retranslateUi(self, CalendarForm):
        _translate = QtCore.QCoreApplication.translate
        CalendarForm.setWindowTitle(_translate("CalendarForm", "Calendar"))
        self.CompNameLabel.setText(_translate("CalendarForm", "Chicago Turnkey Properties"))
        self.RefreshButton.setText(_translate("CalendarForm", "Refresh"))
        self.EventButton.setText(_translate("CalendarForm", "Add Event"))
        self.HomePageButton.setText(_translate("CalendarForm", "Home"))
        self.ListsPageButton.setText(_translate("CalendarForm", "Leads Page"))
        self.SearchPageButton.setText(_translate("CalendarForm", "Search for Lead"))
        self.ProfilePageButton.setText(_translate("CalendarForm", "Create New Profile"))
        self.label.setText(_translate("CalendarForm", ""))
        self.label_2.setText(_translate("CalendarForm", "Events"))
        self.label_3.setText(_translate("CalendarForm", "Should read in data from sql table"))
        self.label_4.setText(_translate("CalendarForm", "Attached Address"))
        self.label_5.setText(_translate("CalendarForm", "Attached Group"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CalendarForm = QtWidgets.QWidget()
    ui = Ui_CalendarForm()
    ui.setupUi(CalendarForm)
    CalendarForm.show()
    sys.exit(app.exec_())


