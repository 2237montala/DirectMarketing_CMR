#https://sebastianraschka.com/Articles/2014_sqlite_in_python_tutorial.html
import sqlite3

sqlite_file = 'my_first_db.sqlite'
table_name1 = 'my_table_1'
table_name2 = 'my_table_2'
new_field = 'my_1st_column'
field_type =  'INTEGER'

conn = sqlite3.connect()
c = conn.cursor()

c.execute('CREATE TABLE {tn} ({nf} {ft})'\
          .format(tn = table_name1, nf = new_field, ft = field_type))

c.execute('CREATE TABLE {tn} ({nf} {ft} PRIMARY KEY)'\
        .format(tn=table_name2, nf=new_field, ft=field_type))

conn.commit()
conn.close()
