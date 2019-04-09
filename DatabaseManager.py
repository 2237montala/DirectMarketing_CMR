#https://stackoverflow.com/questions/16856647/sqlite3-programmingerror-incorrect-number-of-bindings-supplied-the-current-sta
#https://stackoverflow.com/questions/39196462/how-to-use-variable-for-sqlite-table-name?rq=1 <- finds if a table exists
#https://www.sqlite.org/faq.html Remove table at row id example

import sqlite3
import re
from _sqlite3 import Cursor
from Ingestor import Ingestor

#This means All characters that are A to Z or a to z or 0 to 9 or _ that
#exist anywhere in the string
VALID_CHARS = '^[A-Za-z0-9_]*$'


class DatabaseManager:
    def __init__ (self, file_loc):
        self.conn = sqlite3.connect(file_loc)
        self.cursor = self.conn.cursor()

    def create_table(self, table_name, column_name, column_type):
        """
        Creates a new table with a name and the first column
        """
        try:
            with self.conn:
              if not self.doesTableExist(table_name):
                  column_name = column_name.replace("'","\'")
                  self.cursor.execute("CREATE TABLE %s (%s %s PRIMARY KEY)" % (table_name, column_name, column_type))
                  self.conn.commit()
                  return True
              else:
                  return False
        except Exception as er:
            print('Error message:', er.args[0])
            return False

    def doesTableExist(self, table_name):
        """
        Checks if the table exists by checking the database file for a table
        with the same name
        """
        try:
            self.cursor.execute("SELECT 1 FROM sqlite_master WHERE name = ? AND type = 'table'",(table_name,))
            if self.cursor.fetchone() is not None:
                #If it doesn't return none then the table exists
                return True
            else:
                #print("Table already exists")
                return False
        except sqlite3.Error as er:
            #Catches sql errors
            print('Error message:', er.args[0])
            return False
        except Exception as er:
            #General error message
            print('Error message:', er.args[0])
            return False

    def create_table_list(self,table_name,column_name_list,column_type):
        """
        Creates a table with a name but takes in a list of column header
        Uses the create_table and add column method but with a loop
        """
        self.create_table(table_name,column_name_list[0],column_type)
        for i in range(1,len(column_name_list)):
            #column_name = column_name.replace("'","\'")
            self.add_column(table_name,column_name_list[i],'string')


    def add_column(self, table_name,column_name, column_type):
        """
        Adds a column to the table requested with a specified datatype
        """
        try:
            #.format is used to turn certain inputs into a string so SQL doesn't
            #get mad for special characters
            #column_name = column_name.replace("'","\'")
            self.cursor.execute("ALTER TABLE %s ADD COLUMN %s %s" % (table_name,'"{}"'.format(column_name) ,column_type))
            return True
        except Exception as er:
            #General error message
            print('Error message:', er.args[0])
            return False

    def add_list_of_rows(self,table_name,column_list,rows):
        try:
            for row in rows:
                self.add_row_list(table_name,column_list,row)
            return True
        except Exception as er:
            #General error message
            print('Error message:', er.args[0])
            return False


    def add_row_list(self, table_name, column_arr, row_arr):
        """
        Adds a rows to the table with specified data. It first adds the value
        related to the first column, then adds the rest by appending to it
        """

        #Crashes if there is a comma in the field
        with self.conn:
            self.cursor.execute("INSERT OR IGNORE INTO %s (%s) VALUES(?)" % (table_name,'"{}"'.format(column_arr[0])), (row_arr[0],))
            for i in range(1,len(column_arr)):
                self.cursor.execute("UPDATE %s SET %s=? WHERE %s=?" % (table_name, '"{}"'.format(column_arr[i]),column_arr[0]) , (row_arr[i], row_arr[0],))
                #self.cursor.execute("UPDATE %s SET ?=? WHERE ?=?" % (table_name) , (column_arr[i],row_arr[i], column_arr[0],row_arr[0],))


    def clear_table(self, table_name):
        """
        Clears all the values in the table. I don't know if it keeps the column
        headers or not   ------- "YES IT DOES KEEP THE COLUMN HEADERS" - ULY 4/8/2019
        """
        with self.conn:
                self.cursor.execute("DELETE FROM %s" % table_name)

    def get_table(self, table_name):
        """
        Returns the table as an 2d list
        """
        try:
            self.cursor.execute("SELECT * FROM %s" % table_name)
            return self.cursor.fetchall()
        except Exception as er:
            #General error message
            print('Error message:', er.args[0])
            return None

    def get_table_names(self):
        """
        Returns a list of the table names in the database
        """
        try:
            self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
            names = self.cursor.fetchall()
            formatedNames = []
            for name in names:
                formatedNames.append(name[0])
            return formatedNames
        except Exception as er:
            #General error message
            print('Error message:', er.args[0])
            return None

    def get_headers(self,table_name):
        """
        Return the column headers for the table
        """
        try:
            #self.cursor.execute('PRAGMA TABLE_INFO({})'.format(table_name))
            self.cursor.execute('PRAGMA TABLE_INFO(%s)' % table_name)
            headers = [tup[1] for tup in self.cursor.fetchall()]
            return headers
        except Exception as er:
            #General error message
            print('Error message:', er.args[0])
            return False

    def get_header_index(self, table_name, header):
        i = 0
        headers = self.get_headers(table_name)
        for head in headers:
            if head == header:
                return i
            i += 1
        return False
    def get_row_at(self,table_name,column_name = None, column_value = None, row_id = -1):
        try:
            if row_id != -1:
                #The user wants to use row id to get row
                print("Get PK")
                self.cursor.execute('SELECT * FROM %s WHERE _rowid_ = ?' % (table_name,), (row_id,))
            else:
                #The user wants to use a specific column to get row
                print("Get row w/ column")
#                 self.cursor.execute('SELECT * FROM %s WHERE %s = ?' % (table_name,column_name), (column_value,))
                column_name = column_name.replace("'","\'")
                self.cursor.execute('SELECT * FROM %s WHERE %s = ?' % (table_name,column_name,), (column_value,))
#                 return self.cursor.fetchall()
            for row in self.cursor:
                return row
        except Exception as er:
            #General error message
            print('Error message:', er.args[0])
            return None

    def delete_row_at(self,table_name, row_id = -1):
        try:
            with self.conn:
                #Create a temporary table names temp with the data from
                #the original table but skips the row at the row id
                self.cursor.execute('CREATE TEMPORARY TABLE temp AS SELECT * FROM %s WHERE _rowid_ != ?' % table_name ,(row_id,))
                #Delete the old table
                self.cursor.execute('DROP TABLE %s' % table_name)
                #Create a new table with the same name as the old table
                #and copies all the data from temp
                self.cursor.execute('CREATE TABLE %s AS SELECT * FROM temp' % table_name)
                #Deletes the temp table
                self.cursor.execute('DROP TABLE temp')
                return True
        except Exception as er:
            #General error message
            print('Error message:', er.args[0])
            return False

    def remove_spaces(self,old_list):
        for i in range(len(old_list)):
            old_list[i] = old_list[i].replace(' ','_')
        return old_list

    def is_valid_string(self,input_str):
        if re.match(VALID_CHARS,input_str):
            #Checks if the string is only letters and numbers
            return input_str
        else:
            raise Exception('Illegally formatted string')

    def update_row_at(self, table_name, column_name = None, column_value = None, primary_key = None, new_row = None):
        column_arr =  self.get_headers(table_name)
        if (primary_key != None):
            print("PK found")
            old_row = self.get_row_at(table_name, row_id = primary_key)
            if (len(old_row) == len(new_row)):
                try:
                    with self.conn:
                        for i in range(0, len(new_row)):
                            self.cursor.execute("UPDATE %s SET %s='%s' WHERE _rowid_ = ?" % (table_name, column_arr[i], new_row[i]), (primary_key,))
                        return True
                except Exception as er:
                    #General error message
                    print('Error message:', er.args[0])
                    return False
            else:
                print('# of items in row doesn\'t match the # of items in current row' )
                return False
        else:
            print("using column method")
            column_name = column_name.replace("'","\'")
            old_row = self.get_row_at(table_name, column_name, column_value)
            if (len(old_row) == len(new_row)):
                try:
                    with self.conn:
                        self.cursor.execute("SELECT _rowid_, * FROM %s WHERE %s = ?" % (table_name, column_name), (column_value,))
                        rowid = self.cursor.fetchone()
                        print(rowid[0])
                        for i in range(0, len(new_row)):
    #                         print(column_arr[i])
    #                         print(new_row[i])
                            self.cursor.execute("UPDATE %s SET %s='%s' WHERE _rowid_ = ?" % (table_name, column_arr[i], new_row[i]), (rowid[0],))
                        return True
                except Exception as er:
                    #General error message
                    print('Error message:', er.args[0])
                    return False
            else:
                print('# of items in row doesn\'t match the # of items in current row' )
                return False

    def search_table(self, searchCriteria, table_name):
        columns = self.get_headers(table_name)
        print(columns)
        print(searchCriteria)
        searchCriteria = ("%" + searchCriteria + "%")
        try:
            with self.conn:
                rows = []
                for header in columns:
                    #print(header)
                    #Use '"{}"'.format() to allow for special characters in column names
                    self.cursor.execute("SELECT * FROM %s WHERE %s LIKE ?" % (table_name, '"{}"'.format(header)), (searchCriteria,))
                    row = self.cursor.fetchall()
                    if row == [] :
                        print("No Row Found at %s" % (header))
                    else:
                        for r in row:
                            rows.append(r)
                        print(rows)
                return rows
        except Exception as e:
            print("Error Message:", e.args[0])
            return None
