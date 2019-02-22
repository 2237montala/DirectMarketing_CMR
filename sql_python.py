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


# Creating a new SQLite table with 1 column
# doesTableExist("%s" % t)
# add_column(t,'Number', 'string')
# add_column(t,'Equity', 'integer')
# add_row(t, 'Name', 'Jane')
# add_row(t, 'Number', 1)
# add_row(t, 'Number', 2)
# add_row(t, 'Number', 3)
# c.execute("DELETE FROM %s" % t)
# conn.commit()
# c.execute("DROP TABLE %s" % t)
# conn.commit()
# print(return_table(t))
# conn.close()
#add_column(t,'Number', 'string')
#add_column(t,'Equity', 'integer')
#add_row(t,'Name','John','s')
#add_row(t, 'Name', 'John')
# add_row(t, 'Number', 1)
# add_row(t, 'Number', 2)
# add_row(t, 'Number', 3)
#c.execute("DELETE FROM %s" % t)
#conn.commit()
# c.execute("DROP TABLE %s" % t)
# conn.commit()
