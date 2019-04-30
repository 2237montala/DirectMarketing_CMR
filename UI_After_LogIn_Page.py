from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate, QDateTime
from PyQt5.QtWidgets import QCalendarWidget, QDateEdit
from dialog import *
from UI_ProfilePage import *
from calendar import calendar

from DatabaseManager import DatabaseManager
from file_browser import file_browser
from csv_importer import csv_importer_popup

Event_Columns = ['Date', 'Event', 'Address', 'Group']

class Ui_CalendarForm(QtWidgets.QDialog):

    def __init__(self, db_file, protected_table_prefix):
        try:
          super().__init__()
          self.setupUi()
          # for the table
          self.protected_table_prefix = protected_table_prefix
          self.db = DatabaseManager(db_file,self.protected_table_prefix)
          self.db_file_loc = db_file
          self.event_info_table_name = protected_table_prefix + "Event_Information"
        except Exception as er:
            print('Error message:', er.args[0])
            return False

    # creates method that handles the add event button and opens the dialog window
    def EventButton_handler(self):
        try:
            ui_update = Ui_Dialog('test.db', '__ADMIN__')
            ui_update.calendar_dialog_signal.connect(lambda: self.offpass())
            ui_update.exec_()
        except Exception as er:
            print('Error message:', er.args[0])
            return False
        #self.calendar.
    #passes
    def offpass(self):
        print('')
    
    # creates method that handles lists page button and changes widget to the show lists page
    def handle_listsPageButton(self):
        print("clicked")
        #self.window2 = QtWidgets.QMainWindow()
        #self.ui2 = whatever the right window is
        #self.ui2.name of class
        #self.window2.show()
        #CalendarForm.hide()
        print("made it")

    # creates method that handles the profile page button and it opens the profile page 
    def handle_profilePageButton(self):
        print("clicked")
        self.window3 = QtWidgets.QWidget()
        self.ui3 = ui_ProfilePage()
        self.ui3.setupUi(self.window3)
        self.window3.show()
        self.hide()
        print("made it")

    # creates method that handles the search page button and it should open the show list ui page
    def handle_searchPageButton(self):
        print("clicked")
        #self.window4 = QtWidgets.QMainWindow()
        #self.ui4 =
        #self.ui4.classname(self.window4)
        #self.window4.show()
        #CalendarForm.hide()
        print("made it")

    # creates method that handles the home page button and it just refreshes the page
    def handle_homePageButton(self):
        self.update()

    # creates a method that refreshes the page
    def handle_refreshButton(self):
        self.update()

    # creates a method that sets the label on the page to the date that is selected from the calendar
    def showDate(self, date):
        try:
            dater = date.toString("MM-dd-yy")
            self.label.setText(dater)
            if not self.db.doesTableExist(self.event_info_table_name):
                self.label_3.setText('No Event')
            row = self.db.get_row_at(self.event_info_table_name,Event_Columns[0],dater)
            if not row == None:
                self.label_3.setText(row[1])
            else:
                self.label_3.setText('NO event')
        except Exception as er:
            print('Error message:', er.args[0])
            return False

    def setupUi(self):
        # auto generated code from Qt Designer, creates all elements of the page
        try:
            self.setObjectName("CalendarForm")
            self.setEnabled(True)
            self.resize(1650, 950)
            self.setLayoutDirection(QtCore.Qt.LeftToRight)
            self.setAutoFillBackground(True)
            self.CompNameLabel = QtWidgets.QLabel(self)
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
            self.calendar = QtWidgets.QCalendarWidget(self)
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
            self.horizontalLayoutWidget = QtWidgets.QWidget(self)
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
            self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self)
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
            self.label = QtWidgets.QLabel(self)
            self.label.setGeometry(QtCore.QRect(975, 159, 150, 50))
            font = QtGui.QFont()
            font.setPointSize(22)
            font.setBold(True)
            font.setWeight(75)
            self.label.setFont(font)
            self.label.setAutoFillBackground(False)
            self.label.setObjectName("label")
            self.label_2 = QtWidgets.QLabel(self)
            self.label_2.setGeometry(QtCore.QRect(875, 134, 300, 100))
            font = QtGui.QFont()
            font.setPointSize(20)
            font.setBold(True)
            font.setUnderline(True)
            font.setWeight(75)
            self.label_2.setFont(font)
            self.label_2.setAutoFillBackground(False)
            self.label_2.setObjectName("label_2")
            self.label_3 = QtWidgets.QTextBrowser(self)
            self.label_3.setGeometry(QtCore.QRect(875, 250, 700, 625))
            self.label_3.setAutoFillBackground(False)
            self.label_3.setAlignment(QtCore.Qt.AlignTop)
            self.label_3.setObjectName("label_3")
            self.label_3.setFontPointSize(20)
            self.label_4 = QtWidgets.QLabel(self)
            self.label_4.setGeometry(QtCore.QRect(925, 775, 100, 50))
            font = QtGui.QFont()
            font.setBold(False)
            font.setUnderline(True)
            font.setWeight(50)
            self.label_4.setFont(font)
            self.label_4.setAutoFillBackground(False)
            self.label_4.setObjectName("label_4")
            self.label_5 = QtWidgets.QLabel(self)
            self.label_5.setGeometry(QtCore.QRect(925, 825, 100, 50))
            font = QtGui.QFont()
            font.setUnderline(True)
            self.label_5.setFont(font)
            self.label_5.setAutoFillBackground(False)
            self.label_5.setObjectName("label_5")
            self.line = QtWidgets.QFrame(self)
            self.line.setGeometry(QtCore.QRect(10, 75, 1630, 20))
            self.line.setFrameShape(QtWidgets.QFrame.HLine)
            self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
            self.line.setObjectName("line")
    
            self.retranslateUi()
            
            # these lines create connects to the buttons with there corresponding methods
            self.calendar.clicked[QtCore.QDate].connect(self.showDate)
            date = self.calendar.selectedDate()
            self.ListsPageButton.clicked.connect(self.handle_listsPageButton)
            self.ProfilePageButton.clicked.connect(self.handle_profilePageButton)
            self.SearchPageButton.clicked.connect(self.handle_searchPageButton)
            self.HomePageButton.clicked.connect(self.handle_homePageButton)
            self.RefreshButton.clicked.connect(self.handle_refreshButton)
            self.EventButton.clicked.connect(self.EventButton_handler)
            QtCore.QMetaObject.connectSlotsByName(self)
        except Exception as er:
            print('Error message:', er.args[0])
            return False
    # code that is auto generated from Qt Designer
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("CalendarForm", "Calendar"))
        self.CompNameLabel.setText(_translate("CalendarForm", "Chicago Turnkey Properties"))
        self.RefreshButton.setText(_translate("CalendarForm", "Refresh"))
        self.EventButton.setText(_translate("CalendarForm", "Add Event"))
        self.HomePageButton.setText(_translate("CalendarForm", "Home"))
        self.ListsPageButton.setText(_translate("CalendarForm", "Leads Page"))
        self.SearchPageButton.setText(_translate("CalendarForm", "Search for Lead"))
        self.ProfilePageButton.setText(_translate("CalendarForm", "Create New Profile"))
        self.label.setText(_translate("CalendarForm", ""))
        self.label_2.setText(_translate("CalendarForm", "Event:"))
        self.label_3.setText(_translate("CalendarForm", " "))
        self.label_4.setText(_translate("CalendarForm", ""))
        self.label_5.setText(_translate("CalendarForm", ""))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_CalendarForm('test.db','__ADMIN__')
    ui.show()
    sys.exit(app.exec_())
