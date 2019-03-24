#https://pythonspot.com/pyqt5/
import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from DatabaseManager import DatabaseManager
from file_browser import file_browser
from csv_importer import csv_importer_popup

class GUI():
    def __init__(self,db_file):
        super().__init__()
        self.db = DatabaseManager(db_file)
        self.curr_table = "Divorce"
        self.tables = ['Absentee','Divorce','Lis_Pendents','Probate']

    def create_menu_bar(self):
        #Create a new menu bar
        mainMenu = QMenuBar()
        fileMenu = mainMenu.addMenu('File')
        editMenu = mainMenu.addMenu('Edit')

        #Adds a action called import csv that calls the method
        #when clicked
        #editMenu.addAction('Import CSV',self.open_file_browser)
        editMenu.addAction('Import CSV',self.open_csv_import)

        #Does the same things as the line above it
        #imprtCSV = QAction('Import CSV',self.window)
        #imprtCSV.triggered.connect(self.open_file_browser)
        #editMenu.addAction(imprtCSV)

        viewMenu = mainMenu.addMenu('View')
        switchTableMenu = viewMenu.addMenu("Switch Table")
        self.add_menu_items(self.db.get_table_names(),switchTableMenu)
        searchMenu = mainMenu.addMenu('Search')
        toolsMenu = mainMenu.addMenu('Tools')

        return mainMenu;

    def add_widgets(self):
        """
        Adds the widgets to the window
        """
        self.table = QTableWidget(1,5)
        self.updateButton = QPushButton("Update Table")
        self.fileBrowserButton = QPushButton("Upload File")
        self.updateButton.clicked.connect(self.update_button_click)
#         self.fileBrowserButton.clicked.connect(self.open_file_browser)
        self.fileBrowserButton.clicked.connect(self.open_csv_import)



        layout = QGridLayout()
        self.menuBar = self.create_menu_bar()
        #addWidget(widget,row,column,row span,col span)
        layout.addWidget(self.menuBar,1,1,1,2)
        layout.addWidget(self.table,2,1,1,2)
        layout.addWidget(self.updateButton,3,1,1,1)
        layout.addWidget(self.fileBrowserButton,3,2,1,1)

        return layout

    def open_file_browser(self):
        """
        Opens a file browser to select a csv to add
        """
        fb = file_browser('CSV File Finder')
        file_loc = fb.open_window()


    def open_csv_import(self):
        #https://stackoverflow.com/questions/4838890/python-pyqt-popup-window
        #Explained how to make another widget pop up
        #Key is to make a widget and use self.widget
        file = file_browser("File Browser").openFileNameDialog()
        if(file != None):
            self.csv_importer = csv_importer_popup("CSV Importer",file,self.tables,'test.db')
            self.csv_importer.show()
            self.csv_importer.connect()
            #window.connect(csv_importer, Qt.SIGNAL('triggered()'),self.update_table)
            #self.db.get_table_names()


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

            item = QTableWidgetItem(value)
            item.setFlags(Qt.ItemIsEnabled)
            #0x0080 align vertical centered
            #0x0004 align horizontally centered
            item.setTextAlignment(0x0080 | 0x0004)
            table.setItem(row_num,col,item)
            col = col + 1

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

    def get_table(self):
        """
        Returns the table in the window
        """
        return self.table

    def set_table(self,new_table):
        """
        Sets the current windows table to the paramater table
        """
        self.table = new_table


    def update_button_click(self):
        """
        Updates table when button is pressed
        """
        print("Button clicked")
        self.update_table(self.db.get_table(self.curr_table)
                         ,self.db.get_headers(self.curr_table))

    def set_curr_table_name(self, new_table_name):
        self.curr_table = new_table_name

    def switch_curr_table(self):
        print(self.menuBar.sender().text())
        self.set_curr_table_name(self.menuBar.sender().text())


    def add_menu_items(self,table_names,menu):
        for name in table_names:
            #menu.addAction(name,(lambda: self.print_action(name)))
            menu.addAction(name,self.switch_curr_table)
            #, self.set_curr_table_name(name)

    # Main run method
    def run(self,screen_width,screen_height):
        """
        Main method to display gui
        """
        w = screen_width
        h = screen_height
        app = QApplication(sys.argv)
        self.window = QWidget()

        self.window.resize(w,h)
        self.window.setLayout(self.add_widgets())
        self.window.show()

        sys.exit(app.exec_())


if __name__ == '__main__':
    data_base_file = 'test.db'
    app = GUI(data_base_file)
    app.run(1650,800)
    #app.update_table([],rows)
