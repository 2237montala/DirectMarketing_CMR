from gui import GUI
from DatabaseManager import DatabaseManager

def main():
    sqlite_file = 'test.db'
    db = DatabaseManager(sqlite_file)

    new_table = "Probate"
    rows = db.return_table(new_table)

    print(rows)

    app = GUI()
    app.run(1650,900)
    app.update_table([],rows)


main()
