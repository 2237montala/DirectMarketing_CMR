#https://pythonspot.com/pyqt5/
import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from DatabaseManager import DatabaseManager

class GUI:
    def __init__(self,db_file):
        self.db = DatabaseManager(db_file)
        self.curr_table = "Probate"
        #rows = db.return_table(new_table)

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
        Sets the current windows table to the paramter table
        """
        self.table = new_table


    def update_button_click(self):
        """
        Updates table when button is pressed
        """
        print("Button clicked")
        self.update_table(self.db.get_table(self.curr_table)
                         ,self.db.get_headers(self.curr_table))

    def add_widgets(self):
        """
        Adds the widgets to the window
        """
        self.table = QTableWidget(1,5)
        self.updateButton = QPushButton("Update Table")
        self.updateButton.clicked.connect(self.update_button_click)

        layout = QGridLayout()
        layout.addWidget(self.table)
        layout.addWidget(self.updateButton)
        return layout

    # Main run method
    def run(self,screen_width,screen_height):
        """
        Main method to display gui
        """
        w = screen_width
        h = screen_height
        app = QApplication([])
        self.window = QWidget()

        #headers = ["Name", "Address"];
        #row =     [["Jimmy Qt-Designer","17 Elm St"],
        #           ["John Smith", "1175 Deerfield Rd"],
        #           ["Ulysses Cardenas","1105 Adams Ave"]]


        self.window.resize(w,h)
        self.window.setLayout(self.add_widgets())
        self.window.show()

        sys.exit(app.exec_())
