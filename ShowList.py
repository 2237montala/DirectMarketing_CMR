# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ShowSortLists.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

# Current List of Errors:
# After importing once it doesn't do it again :(

from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSlot
import sys
from DatabaseManager import DatabaseManager
from file_browser import file_browser
from csv_importer import csv_importer_popup
from UI_ProfilePage import UI_ProfilePage

class Ui_MainWindow(QtWidgets.QWidget):
    log_out_signal = QtCore.pyqtSignal()
    goto_profile_signal = QtCore.pyqtSignal()

    def __init__(self,db_file,protected_table_prefix):
        super().__init__()
        self.protected_table_prefix = protected_table_prefix
        self.db = DatabaseManager(db_file,self.protected_table_prefix)
        self.tables_in_db = self.db.get_table_names()
        self.db_file_loc = db_file
        self.curr_table = None


    def setup_main_widget(self,width,height):
        """
        Sets up the widgets for the window
        """
        #self.centralwidget = QtWidgets.QWidget()
        #self.centralwidget.setObjectName("centralwidget")
        #self = QtWidgets.QWidget()
        self.setGeometry(QtCore.QRect(0, 0, width, height))
        self.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName("gridLayout")

        #Search bar text entry
        self.searchBar = QtWidgets.QLineEdit(self)
        self.searchBar.setPlaceholderText("Search Term")
        self.searchBar.returnPressed.connect(self.get_search_key)
        self.searchBar.setObjectName("SearchBar")
        self.gridLayout.addWidget(self.searchBar, 1, 2 ,1, 1)
        self.searchBar.setMaximumWidth(500)

        self.scrollArea = QtWidgets.QScrollArea(self)
        #self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")

        #Scroll Window
        self.table = QtWidgets.QTableWidget(20,10)
        self.table.cellDoubleClicked.connect(self.table_item_clicked)
        self.scrollArea.setWidget(self.table)
        self.gridLayout.addWidget(self.scrollArea, 3, 0, 1, 4)

        self.searchButton = QtWidgets.QPushButton("Search Table", self)
        self.searchButton.setObjectName("searchButton")
        self.searchButton.clicked.connect(self.get_search_key)
        self.gridLayout.addWidget(self.searchButton, 1, 3, 1, 1)

        #Create combo box with the ability to switch tables
        self.comboBox = QtWidgets.QComboBox(self)
        self.comboBox.setObjectName("comboBox")
        self.add_combo_box_items(self.db.get_table_names(),self.comboBox)
        self.comboBox.activated.connect(self.switch_curr_table_comboBox)
        self.gridLayout.addWidget(self.comboBox, 1, 0, 1, 1)
        QtCore.QMetaObject.connectSlotsByName(self)
        print(self.tables_in_db)
        if (self.tables_in_db != []):
            print(self.tables_in_db[0])
            print("Tables in db")
            self.set_curr_table_name(self.tables_in_db[0])
            self.update_table(self.db.get_table(self.tables_in_db[0]), self.db.get_headers(self.tables_in_db[0]))
        else:
            print("Nothing in db")
            pass

    def setup_menu_bar(self):
        """
        Sets up the menu bar. Main windows have their own menu bar and this
        provides a menu bar on completion
        """
        #Menu Bar
        self.menubar = QtWidgets.QMenuBar()
        self.menubar.setDefaultUp(False)
        self.menubar.setNativeMenuBar(True)

        fileMenu = self.menubar.addMenu("File")
        fileMenu.addAction("Log Out", self.log_out)
        editMenu = self.menubar.addMenu("Edit")
        editMenu.addAction('Import CSV',self.open_csv_import)
        editMenu.addSeparator()
        editMenu.addAction('Clear Table',self.clear_table)
        editMenu.addAction('Delete Table',self.delete_table)
        self.viewMenu = self.menubar.addMenu("View")
        self.add_menu_items(self.db.get_table_names()
                            ,self.viewMenu.addMenu("Switch Table"))
        self.viewMenu.addAction("Update Table", self.update_menu_action)

        return self.menubar

    def update_table(self, row_list,header_list):
        """
        Updates the contents of the table using a list of rows
        and a list of column headers
        """
        #Get the table in the windows
        table = self.get_table()
        #Set the number of rows and the number of column
        #Using the lists from parameters
        table.setRowCount(len(row_list))
        table.setColumnCount(len(header_list))

        for i in range(0,len(header_list)):
            header_list[i] = header_list[i].replace('_',' ')

        table.setHorizontalHeaderLabels(header_list)


        #Adds the rows of data
        self.add_items(table,row_list)

        #Resizes the cells to fit text without clipping
        #1 = stretch to max string length
        table.horizontalHeader().setSectionResizeMode(1)
        table.setSelectionBehavior(QtWidgets.QTableView.SelectRows);
        self.set_table(table)

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
            #item.setFlags(QtCore.Qt.ItemIsEditable)
            item.setFlags(QtCore.Qt.ItemIsEnabled)
            #item.setFlags(QtCore.Qt.ItemIsSelectable)
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
        self.update_table(self.db.get_table(self.curr_table)
                         ,self.db.get_headers(self.curr_table))


    def open_csv_import(self):
        """
        Opens the file browser and the csv importer window. On completion
        the table is updated to the imported table
        """
        #https://stackoverflow.com/questions/4838890/python-pyqt-popup-window
        #Explained how to make another widget pop up
        #Key is to make a widget and use self.widget
        file = file_browser("File Browser").openFileNameDialog()
        if(file != None):

            self.csv_importer = csv_importer_popup("CSV Importer",self.db_file_loc,self.tables_in_db,self.protected_table_prefix)
            #This links the import signal to the import close window
            self.csv_importer.importDoneSignal.connect(self.import_closed)
            self.csv_importer.run_popup(file)
            #Runs to the window
            self.csv_importer.exec_()

    def import_closed(self,str):
        """
        When the csv importer is closed a signal is emitted with the table
        name of the imported table. It updates various refernces to the table name
        """
        #This method is called when the import window closed
        print('Refreshing table')
        #Call the update menu action to refresh the table
        self.set_curr_table_name(str)
        self.update_view_menu()
        self.update_combobox()
        self.update_menu_action()


    def set_curr_table_name(self, new_table_name):
        """
        Sets the current table to the paramater
        """
        self.curr_table = new_table_name

    def switch_curr_table_menubar(self):
        """
        When a view -> switch table option is clicked it changes the current
        Table to the option's text and refreshes the table
        """
        self.set_curr_table_name(self.menubar.sender().text())
        self.update_menu_action()

    def switch_curr_table_comboBox(self,selectedItem):
        """
        When a combo box option is clicked it changes the current
        Table to the option's text and refreshes the table
        """
        #print(self.tables_in_db[selectedItem])
        self.set_curr_table_name(self.tables_in_db[selectedItem])
        self.update_menu_action()



    def add_menu_items(self,table_names,menu):
        """
        Adds a action to the menu provided by creating new actions using the
        table names list inputed
        """
        for name in table_names:
            menu.addAction(name,self.switch_curr_table_menubar)

    def add_combo_box_items(self,table_names,comboBox):
        """
        Creates combo box entries for each table in the data base. Each entry
        is clickable and when clicked will update the table
        """
        for name in table_names:
            comboBox.addItem(name)

    def clear_table(self):
        """
        Clears the current table and verifies if the users wants to clear it
        """
        choice  = QtWidgets.QMessageBox.question(self, 'Confirmation',
                                    "Are you sure you want to clear \"%s\" table? \nTHIS OPERATION IS NOT RECOVERABLE" % self.curr_table,
                                    QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if choice == QtWidgets.QMessageBox.Yes:
            self.db.clear_table(self.curr_table)
            self.update_menu_action()

    def delete_table(self):
        """
        Delete the current table and verifies if the users wants to delete it
        """
        choice  = QtWidgets.QMessageBox.question(self, 'Confirmation',
                                    "Are you sure you want to delete \"%s\" table? \nTHIS OPERATION IS NOT RECOVERABLE" % self.curr_table,
                                    QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if choice == QtWidgets.QMessageBox.Yes:
            self.db.delete_table(self.curr_table)
            self.update_view_menu()
            self.update_combobox()
            if (self.tables_in_db != []):
                self.set_curr_table_name(self.tables_in_db[0])
                self.update_table(self.db.get_table(self.tables_in_db[0]), self.db.get_headers(self.tables_in_db[0]))
            else:
                self.set_curr_table_name(None)
                self.update_table([],[])

    def update_view_menu(self):
        """
        Updates the options in the view -> switch table menu to display
        any new tables that were added during an import
        """
        self.viewMenu.clear()
        self.tables_in_db = self.db.get_table_names()
        self.add_menu_items(self.tables_in_db
                            ,self.viewMenu.addMenu("Switch Table"))
        self.viewMenu.addAction("Update Table", self.update_menu_action)

    def update_combobox(self):
        """
        Updates the options in the switch table combo box to display
        any new tables that were added during an import
        """
        self.comboBox.clear()
        self.add_combo_box_items(self.tables_in_db,self.comboBox)


    def table_item_clicked(self,row,column):
        """
        When a cell is clicked inside the table this retrieves its row
        from the data base for the pop up window to display
        """
        #The double clicked signal returns the row and column of the
        #double clicked item. It will automatically pass those into the method
        #if the paramaters are row and column

        selectedRow = self.db.get_row_at(table_name=self.curr_table,row_id = row+1)
        columnHeaders = self.db.get_headers(self.curr_table)
        Table_name= self.curr_table
#         print(selectedRow)
        #self.ui_ProfilePage().filltable(columHeaders, selectedRow, Table_name)\
        try:
            self.UI_P = UI_ProfilePage(columnHeaders, selectedRow)
            self.UI_P.exec_()
        except Exception as er:
            print('Error message:', er.args[0])
            return False

#         self.csv_importer.importDoneSignal.connect(self.import_closed)
#         self.csv_importer.run_popup(file)
#         #Runs to the window
#         self.csv_importer.exec_()

        #Here you would call a method to show the profile page

    def get_search_key(self):
        """
        Gets the text from the search bar and checks if it is a valid entry. If so
        then pass it to the search table method
        """
#         print("CLICKED")
        try:
            key = self.searchBar.displayText()
            if(self.db.is_valid_string(key)):
#                 print(key)
                self.search_table(key)
            elif (key == ""):
                self.update_menu_action()
        except:
            QtWidgets.QMessageBox.critical(self, 'Invalid Text',
                "Search values can only have alphanumeric values",
                QtWidgets.QMessageBox.Ok)

    def search_table(self, search_key):
        """
        Searches the database for the search key inputed
        """
        rows = self.db.search_table(search_key, self.curr_table)
        self.update_table(rows, self.db.get_headers(self.curr_table))



    def log_out(self):
        print("Logging out\nEmitting signal")
        self.log_out_signal.emit()

if __name__ == '__main__':
    data_base_file = 'programData.db'
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    mainWindow.resize(1600 , 900+50)
    leadsTable = Ui_MainWindow(data_base_file,'__ADMIN__')
    leadsTable.setup_main_widget(1600,900)
    mainWindow.setCentralWidget(leadsTable)

    menuBar = leadsTable.setup_menu_bar()
    mainWindow.setMenuBar(menuBar)

    mainWindow.show()

    sys.exit(app.exec_())
