# https://sebastianraschka.com/Articles/2014_sqlite_in_python_tutorial.html
# https://www.dataquest.io/blog/python-pandas-databases/
# https://www.youtube.com/watch?v=pd-0G0MigUA
#https://stackoverflow.com/questions/17044259/python-how-to-check-if-table-exists
from DatabaseManager import DatabaseManager
from Ingestor import Ingestor
from _hashlib import new

# SETTING IT EQUAL TO ':memory:' WILL HAVE IT RUN ON RAM AND NO SQLITE FILE WILL BE MADE.
sqlite_file = 'test.db'
db = DatabaseManager(sqlite_file)
new_table = 'Students'
db.create_table(new_table, 'Name', 'string')
db.add_column(new_table, 'Age', 'integer')
db.add_column(new_table, 'Year', 'string')
db.add_row(new_table, ['Name', 'Age','Year'], ['Anthony', '12', '2021'])
db.add_row(new_table, ['Name', 'Age','Year'], ['Mike', '18', '2022'])
db.add_row(new_table, ['Name', 'Age','Year'], ['Tyler', '45', '2045'])
# db.clear_table(new_table)
print(db.return_table(new_table))
# Connecting to the database file
<<<<<<< HEAD


# Creating a new SQLite table with 1 column
# doesTableExist("%s" % t)
# add_column(t,'Number', 'string')
# add_column(t,'Equity', 'integer')
# add_row(t, 'Name', 'Jane')
# add_row(t, 'Number', 1)
# add_row(t, 'Number', 2)
# add_row(t, 'Number', 3)
# c.execute("DELETE FROM %s" % t)
=======
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

def create_table(table_name, column_name, column_type):
    with conn:
<<<<<<< HEAD
        if not doesTableExist(table_name):
            #c.execute("CREATE TABLE %s (%s %s PRIMARY KEY)" % (table_name, column_name, column_type))
            c.execute("CREATE TABLE %s (%s %s)" % (table_name, column_name, column_type))
            conn.commit()
=======
<<<<<<< HEAD
      #  if  not doesTableExist(table_name):
      c.execute("CREATE TABLE %s (%s %s PRIMARY KEY)" % (table_name, column_name, column_type))
=======
        if  not doesTableExist(table_name):
            c.execute("CREATE TABLE %s (%s %s PRIMARY KEY)" % (table_name, column_name, column_type))
>>>>>>> cdb49ea9132ab71d6413e4ec4578a6c59e9815d1
            return True
        else:
            #Returns false if tabel already exists
            return False
<<<<<<< HEAD
>>>>>>> ed456d4f357c54e01ac5b27bb27ae549a03cb037
=======
>>>>>>> ed456d4f357c54e01ac5b27bb27ae549a03cb037

def doesTableExist(table_name):
    #c.execute("""SELECT COUNT(*) FROM %s WHERE %s """ % (table_name,table_name))
    #c.execute("""SELECT COUNT(*) FROM 'TEST_TABLE.tables' WHERE table_name = %s """ % (table_name))
    c.execute("SELECT * FROM sqlite_master WHERE name = '%s' and type='table'" % table_name)
    temp = c.fetchone()[1]
    print(temp)
    if temp == table_name:
        print("Table exsists")
        return True
    else:
        print("Table doesn't exist")
        return False


def return_table(tablename):
    try:
        c.execute("SELECT * FROM %s" % tablename)
        return c.fetchall()
    except:
        return "Table doesn't exist"

def add_column(tablename,column_name, column_type):
    try:
        c.execute("ALTER TABLE %s ADD COLUMN %s %s" % (tablename, column_name, column_type))
        return True
    except:
        return False
        # STILL NEED TO FIGURE OUT HOW TO HAVE INGESTOR CLASS AUTOMATICALLY CREATE CORRECT AMOUNT OF COLUMNS

# AFTER THAT IS DONE, ADDING ROW COMMAND HAS TO CHNAGE DEPENDING ON HOW MANY COLUMNS TEHRE IS. THINKING OF PROBABLY DOING A FOR LOOP.
def add_row(tablename, column, row, dataType):
    with conn:
        if dataType == 's':
            c.execute("INSERT OR IGNORE INTO %s (%s) VALUES (?)" % (tablename, column), (row,))
        #if column == 'Name':
        #    c.execute("INSERT OR IGNORE INTO %s (%s) VALUES (?)" % (tablename, column), (row,) )
        #elif column == 'Number':
        #    c.execute("INSERT OR IGNORE INTO %s (%s) VALUES (%d)" % (tablename, column, row))

# Creating a new SQLite table with 1 column
t = 'TEST_TABLE'
create_table(t, 'Name', 'string')
<<<<<<< HEAD
add_column(t,'Number', 'string')
add_column(t,'Equity', 'integer')
add_row(t,'Name','John','s')
=======
<<<<<<< HEAD
<<<<<<< HEAD
add_column(t,'Number', 'string')
add_column(t,'Equity', 'integer')
add_row(t, 'Name', 'John')
add_row(t, 'Number', 1)
add_row(t, 'Number', 2)
add_row(t, 'Number', 3)
# c.execute("DELETE FROM t")
>>>>>>> a0907bc050325e620906a2ce3df37d9d29acb23f
# conn.commit()
# c.execute("DROP TABLE %s" % t)
# conn.commit()
# print(return_table(t))
# conn.close()
#add_column(t,'Number', 'string')
#add_column(t,'Equity', 'integer')
#add_row(t,'Name','John','s')
>>>>>>> cdb49ea9132ab71d6413e4ec4578a6c59e9815d1
#add_row(t, 'Name', 'John')
# add_row(t, 'Number', 1)
# add_row(t, 'Number', 2)
# add_row(t, 'Number', 3)
#c.execute("DELETE FROM %s" % t)
#conn.commit()
# c.execute("DROP TABLE %s" % t)
<<<<<<< HEAD
# conn.commit()
=======
#conn.commit()
print(return_table(t))
conn.close()
<<<<<<< HEAD
>>>>>>> ed456d4f357c54e01ac5b27bb27ae549a03cb037
=======
>>>>>>> ed456d4f357c54e01ac5b27bb27ae549a03cb037
>>>>>>> a0907bc050325e620906a2ce3df37d9d29acb23f
