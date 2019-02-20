#https://sebastianraschka.com/Articles/2014_sqlite_in_python_tutorial.html
#https://www.dataquest.io/blog/python-pandas-databases/
import sqlite3
from Ingestor import Ingestor

sqlite_file = 'my_first_db.sqlite'

# Connecting to the database file
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

def create_columns(data, tablename):
    Ingestor.getheader()
    cur.execute("create table %s (% integer, departure date, arrival date, number text, route_id integer)"% tablename)    
    conn.commit()
    
# Creating a new SQLite table with 1 column
#cur.execute("create table daily_flights (id integer, departure date, arrival date, number text, route_id integer)")

<<<<<<< HEAD
# Creating a second table with 1 column and set it as PRIMARY KEY
# note that PRIMARY KEY column must consist of unique values!
c.execute('CREATE TABLE {tn} ({nf} {ft} PRIMARY KEY)'\
        .format(tn=table_name2, nf=new_field, ft=field_type))

# Committing changes and closing the connection to the database file
conn.commit()
conn.close()
=======
#c.execute('CREATE TABLE {tn} ({nf} {ft})'\
#       .format(tn=table_name1, nf=new_field, ft=field_type))
#conn.commit()
conn.close()
>>>>>>> d78b097d82dbdb559382e312bd6f2557af0fe47e
