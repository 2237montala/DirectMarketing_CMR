#from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout
#from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem

from PyQt5.QtWidgets import *


def add_items(table,row_list):
    row_count = 0
    for row in row_list:
        add_item(table,row_count,row)
        row_count += 1

def add_item(table,row_num,row):
    col = 0
    for str in row:
        item = QTableWidgetItem(str)
        #0x0080 align vertical centered
        #0x0004 align horizontally centered
        item.setTextAlignment(0x0080 | 0x0004)
        table.setItem(row_num,col,item)
        col = col + 1

def create_table(header_list, row_list):
    new_table = QTableWidget(len(row_list),len(header_list))
    new_table.setHorizontalHeaderLabels(header_list)
    add_items(new_table,row_list)

    #1 = stretch to max string length
    new_table.horizontalHeader().setSectionResizeMode(1)

    return new_table

def main():
    app = QApplication([])
    window = QWidget()

    headers = ["Name", "Address"];
    row =     [["Jimmy Qt-Designer","17 Elm St"],
               ["John Smith", "1175 Deerfield Rd"],
               ["Ulysses Cardenas","1105 Adams Ave"]]

    table = create_table(headers,row)
    layout = QGridLayout()
    layout.addWidget(table)
    window.setLayout(layout)
    window.show()
    app.exec_()


main()
