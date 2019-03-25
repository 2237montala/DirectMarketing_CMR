# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ShowSortLists.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5 import QtGui
import sys

from DatabaseManager import DatabaseManager
from file_browser import file_browser
from csv_importer import csv_importer_popup


class Ui_MainWindow(object):
    def __init__(self,db_file):
        #super().__init__()
        self.db = DatabaseManager(db_file)
        self.tables = ['Absentee','Divorce','Lis_Pendents','Probate']
        self.curr_table = self.tables[0]

    def setupUi(self, MainWindow,width,height):
        MainWindow.setObjectName("Direct Marketing CMR")
        MainWindow.resize(width , height)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, width, height))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName("gridLayout")
        self.checkBox_5 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_5.setObjectName("checkBox_5")
        self.gridLayout.addWidget(self.checkBox_5, 2, 2, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 1, 1, 1, 1)
        self.checkBox_4 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_4.setObjectName("checkBox_4")
        self.gridLayout.addWidget(self.checkBox_4, 0, 1, 1, 1)
        self.checkBox_6 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_6.setObjectName("checkBox_6")
        self.gridLayout.addWidget(self.checkBox_6, 2, 1, 1, 1)
        self.checkBox_3 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout.addWidget(self.checkBox_3, 1, 2, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout.addWidget(self.checkBox_2, 0, 2, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(self.gridLayoutWidget)
        #self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")

        #Scroll Window
        self.table = QtWidgets.QTableWidget(10,10)
        #self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 977, 602))
        self.scrollArea.setWidget(self.table)
        self.gridLayout.addWidget(self.scrollArea, 3, 0, 1, 4)

        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 3, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        #Menu Bar
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        ##self.menubar.setGeometry(QtCore.QRect(0, 0, 985, 26))

        self.menubar.setDefaultUp(False)
        self.menubar.setNativeMenuBar(True)

        fileMenu = self.menubar.addMenu("File")
        editMenu = self.menubar.addMenu("Edit")
        editMenu.addAction('Import CSV',self.open_csv_import)
        viewMenu = self.menubar.addMenu("View")
        self.add_menu_items(self.db.get_table_names()
                            ,viewMenu.addMenu("Switch Table"))
        viewMenu.addAction("Update Table", self.update_menu_action)
        searchMenu = self.menubar.addMenu("Search")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.checkBox_5.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_4.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_6.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_3.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_2.setText(_translate("MainWindow", "CheckBox"))
        self.pushButton.setText(_translate("MainWindow", "Search"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Absenty"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Fore Closure"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Divorse"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Lis Pendents"))

    def update_table(self, row_list,header_list):
        """
        Updates the contents of the table using a list of rows
        and a list of column headers
        """
        print("updating table")
        #print(row_list)

        #Get the table in the windows
        table = self.get_table()
        #print(table.rowCount())
        #Set the number of rows and the number of column
        #Using the lists from parameters
        table.setRowCount(len(row_list))
        table.setColumnCount(len(header_list))
        table.setHorizontalHeaderLabels(header_list)

        #Adds the rows of data
        self.add_items(table,row_list)

        #Resizes the cells to fit text without clipping
        #1 = stretch to max string length
        table.horizontalHeader().setSectionResizeMode(1)
        self.set_table(table)
        print(self.get_table().rowCount())

    def add_items(self,table,row_list):
        """
        Adds a list of rows to the table
        """
        row_count = 0
        for row in row_list:
            self.add_item(table,row_count,row)
            row_count += 1

    def add_item(self,table,row_num,row):
        """
        Adds a row to the table by creating table widgets
        The text in the widget is aligned in the center
        """
        col = 0
        for value in row:
            if type(value) == int:
                value = str(value)

            item = QtWidgets.QTableWidgetItem(value)
            item.setFlags(QtCore.Qt.ItemIsEnabled)
            #0x0080 align vertical centered
            #0x0004 align horizontally centered
            item.setTextAlignment(0x0080 | 0x0004)
            table.setItem(row_num,col,item)
            col = col + 1

    def set_table(self,new_table):
        """
        Sets the current windows table to the paramater table
        """
        self.table = new_table

    def get_table(self):
        """
        Returns the table in the window
        """
        return self.table

    def update_menu_action(self):
        """
        Updates table when button is pressed
        """
        print("Button clicked")
        self.update_table(self.db.get_table(self.curr_table)
                         ,self.db.get_headers(self.curr_table))

    def open_csv_import(self):
        #https://stackoverflow.com/questions/4838890/python-pyqt-popup-window
        #Explained how to make another widget pop up
        #Key is to make a widget and use self.widget
        file = file_browser("File Browser").openFileNameDialog()
        if(file != None):
            self.csv_importer = csv_importer_popup("CSV Importer",file,self.tables,'test.db')
            self.csv_importer.show()
            #window.connect(csv_importer, Qt.SIGNAL('triggered()'),self.update_table)
            #self.db.get_table_names()

    def set_curr_table_name(self, new_table_name):
        self.curr_table = new_table_name

    def switch_curr_table(self):
        print(self.menubar.sender().text())
        self.set_curr_table_name(self.menubar.sender().text())

    def add_menu_items(self,table_names,menu):
        for name in table_names:
            #menu.addAction(name,(lambda: self.print_action(name)))
            menu.addAction(name,self.switch_curr_table)
            #, self.set_curr_table_name(name)

    def run(self,width,height):
        app = QtWidgets.QApplication(sys.argv)
        mainWindow = QMainWindow()
        self.setupUi(mainWindow,width,height)
        mainWindow.show()

        sys.exit(app.exec_())


if __name__ == '__main__':
    data_base_file = 'test.db'
    app = Ui_MainWindow(data_base_file)
    app.run(1600,900)
