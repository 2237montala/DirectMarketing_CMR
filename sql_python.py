#https://sebastianraschka.com/Articles/2014_sqlite_in_python_tutorial.html
#https://www.dataquest.io/blog/python-pandas-databases/
import sqlite3
from Ingestor import Ingestor

sqlite_file = 'my_first_db.sqlite'

# Connecting to the database file
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

def create_columns(data, tablename, headerList):
    Ingestor.getheader()
    cur.execute("create table %s (integer, departure date, arrival date, number text, route_id integer)"% tablename)
    conn.commit()

# Creating a new SQLite table with 1 column
#cur.execute("create table daily_flights (id integer, departure date, arrival date, number text, route_id integer)")

#c.execute('CREATE TABLE {tn} ({nf} {ft})'\
#       .format(tn=table_name1, nf=new_field, ft=field_type))
#conn.commit()
conn.close()
