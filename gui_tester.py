from gui import GUI
from DatabaseManager import DatabaseManager

def main():
    #print(rows)
    data_base_file = 'test.db'

    app = GUI(data_base_file)
    app.run(1650,900)
    #app.update_table([],rows)


main()
