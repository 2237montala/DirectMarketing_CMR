# https://sebastianraschka.com/Articles/2014_sqlite_in_python_tutorial.html
# https://www.dataquest.io/blog/python-pandas-databases/
# https://www.youtube.com/watch?v=pd-0G0MigUA
import sqlite3
from Ingestor import Ingestor

# SETTING IT EQUAL TO ':memory:' WILL HAVE IT RUN ON RAM AND NO SQLITE FILE WILL BE MADE.
sqlite_file = 'test.db'

# Connecting to the database file
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

def create_table(table_name, column_name, column_type):
    with conn:
        c.execute("CREATE TABLE %s (%s %s PRIMARY KEY)" % (table_name, column_name, column_type))


def return_table(tablename):
    c.execute("SELECT * FROM %s" % tablename)
    return c.fetchall()

def add_column(tablename,column_name, column_type):
    c.execute("ALTER TABLE %s ADD COLUMN %s %s" % (tablename, column_name, column_type))
# STILL NEED TO FIGURE OUT HOW TO HAVE INGESTOR CLASS AUTOMATICALLY CREATE CORRECT AMOUNT OF COLUMNS

# AFTER THAT IS DONE, ADDING ROW COMMAND HAS TO CHNAGE DEPENDING ON HOW MANY COLUMNS TEHRE IS. THINKING OF PROBABLY DOING A FOR LOOP.
def add_row(tablename, column, row):
    with conn:
        if column == 'Name':
            c.execute("INSERT OR IGNORE INTO %s (%s) VALUES (?)" % (tablename, column), (row,) )
        elif column == 'Number':
            c.execute("INSERT OR IGNORE INTO %s (%s) VALUES (%d)" % (tablename, column, row))

# Creating a new SQLite table with 1 column
t = 'TEST_TABLE'
create_table(t, 'Name', 'string')
add_column(t,'Number', 'string')
add_column(t,'Equity', 'integer')
add_row(t, 'Name', 'John')
add_row(t, 'Number', 1)
add_row(t, 'Number', 2)
add_row(t, 'Number', 3)
# c.execute("DELETE FROM t")
# conn.commit()
# c.execute("DROP TABLE %s" % t)
# conn.commit()
# print(return_table(t))
# conn.close()
