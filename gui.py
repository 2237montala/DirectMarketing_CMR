from PyQt5.QtWidgets import *

class GUI:
    def __init__(self):
        pass

    def edit_table(self,row_list):
        self.add_items(self.get_table(),row_list)
        self.get_table().repaint()

    def add_items(self,table,row_list):
        row_count = 0
        for row in row_list:
            self.add_item(table,row_count,row)
            row_count += 1

    def add_item(self,table,row_num,row):
        col = 0
        for str in row:
            item = QTableWidgetItem(str)
            #0x0080 align vertical centered
            #0x0004 align horizontally centered
            item.setTextAlignment(0x0080 | 0x0004)
            table.setItem(row_num,col,item)
            col = col + 1

    def update_table(self, row_list,header_list):
        table = self.get_table()
        #table = QTableWidget(len(row_list),len(header_list))
        table = QTableWidget(1,1)
        #table.setHorizontalHeaderLabels(header_list)
        #self.add_items(table,row_list)

        #1 = stretch to max string length
        #table.horizontalHeader().setSectionResizeMode(1)
        self.set_table(table)
        self.get_table().repaint()

    def get_table(self):
        return self.table

    def set_table(self,new_table):
        self.table = new_table

    def run(self,screen_width,screen_height):
        w = screen_width
        h = screen_height
        app = QApplication([])
        window = QWidget()

        #headers = ["Name", "Address"];
        #row =     [["Jimmy Qt-Designer","17 Elm St"],
        #           ["John Smith", "1175 Deerfield Rd"],
        #           ["Ulysses Cardenas","1105 Adams Ave"]]

        self.table = QTableWidget(1,5)
        layout = QGridLayout()
        layout.addWidget(self.table)
        window.resize(w,h)
        window.setLayout(layout)
        window.show()
        app.exec_()
