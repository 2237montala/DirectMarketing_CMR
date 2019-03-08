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
        row_count = 0
        print(type(row_list[0][0]))
        print(type(row_list[0][2]))
        for row in row_list:
            self.add_item(table,row_count,row)
            row_count += 1

    def add_item(self,table,row_num,row):
        col = 0
        for value in row:
            item = QTableWidgetItem(value)
            item.setFlags(Qt.ItemIsEnabled)
            #0x0080 align vertical centered
            #0x0004 align horizontally centered
            item.setTextAlignment(0x0080 | 0x0004)
            table.setItem(row_num,col,item)
            col = col + 1

    def update_table(self, row_list,header_list):
        print("updating table")
        print(row_list)
        table = self.get_table()
        print(table.rowCount())
        table.setRowCount(len(row_list))
        table.setColumnCount(len(header_list))
        table.setHorizontalHeaderLabels(header_list)
        self.add_items(table,row_list)

        #1 = stretch to max string length
        table.horizontalHeader().setSectionResizeMode(1)
        self.set_table(table)
        print(self.get_table().rowCount())

    def get_table(self):
        return self.table

    def set_table(self,new_table):
        self.table = new_table


    def update_button_click(self):
        print("Button clicked")
        self.update_table(self.db.get_table(self.curr_table)
                         ,self.db.get_headers(self.curr_table))

    #Add widgets
    def add_widgets(self):
        self.table = QTableWidget(1,5)
        self.updateButton = QPushButton("Update Table")
        self.updateButton.clicked.connect(self.update_button_click)

        layout = QGridLayout()
        layout.addWidget(self.table)
        layout.addWidget(self.updateButton)
        return layout

    # Main run method
    def run(self,screen_width,screen_height):
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

        app.exec_()
