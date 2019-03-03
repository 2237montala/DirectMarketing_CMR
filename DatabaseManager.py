#https://stackoverflow.com/questions/16856647/sqlite3-programmingerror-incorrect-number-of-bindings-supplied-the-current-sta

import sqlite3

class DatabaseManager:
    def __init__ (self, file_loc):
        self.conn = sqlite3.connect(file_loc)
        self.cursor = self.conn.cursor()

    def create_table(self, table_name, column_name, column_type):
        """
        Creates a new table with a name and the first column
        """
        with self.conn:
          if not self.doesTableExist(table_name):
              self.cursor.execute("CREATE TABLE %s (%s %s PRIMARY KEY)" % (table_name, column_name, column_type))
              self.conn.commit()
              return True
          else:
                return False

    def doesTableExist(self, table_name):
        """
        Checks if the table exists by checking the database file for a table
        with the same name
        """
        try:
            self.cursor.execute("SELECT * FROM sqlite_master WHERE name = '%s' AND type = 'table'" % table_name)
            if self.cursor.fetchone()[1] == table_name:
                #If it returns a 1 that means a table with the same names exists
                return True
            else:
                #print("Table already exists")
                return False
        except sqlite3.Error as er:
            #If another error is throws print it
            print('Error message:', er.args[0])
            return False

    def create_table_list(self,table_name,column_name_list,column_type):
        """
        Creates a table with a name but takes in a list of column header
        Uses the create_table and add column method but with a loop
        """
        self.create_table(table_name,column_name_list[0],column_type)
        for i in range(1,len(column_name_list)):
            self.add_column(table_name,column_name_list[i],'string')


    def add_column(self, table_name,column_name, column_type):
        """
        Adds a column to the table requested with a specified datatype
        """
        try:
            #.format is used to turn certain inputs into a string so SQL doesn't
            #get mad for special characters
            self.cursor.execute("ALTER TABLE %s ADD COLUMN %s %s" % (table_name,'"{}"'.format(column_name) ,column_type))
            return True
        except sqlite3.Error as er:
            print('Error message:', er.args[0])
            return False

    def add_row_list(self, table_name, column_arr, row_arr):
        """
        Adds a rows to the table with specified data. If first adds the value
        related to the first column, then adds the rest by appending to it
        """
        with self.conn:
            self.cursor.execute("INSERT OR IGNORE INTO %s (%s) VALUES(?)" % (table_name,'"{}"'.format(column_arr[0])), (row_arr[0],))
            for i in range(1,len(column_arr)):
                self.cursor.execute("UPDATE %s SET %s='%s' WHERE %s='%s'" % (table_name, '"{}"'.format(column_arr[i]), row_arr[i], column_arr[0], row_arr[0]))

    def clear_table(self, table_name):
        """
        Clears all the values in the table. I don't know if it keeps the column
        headers or not
        """
        with self.conn:
                self.cursor.execute("DELETE FROM %s" % table_name)

    def return_table(self, table_name):
        """
        Returns the table as an 2d list
        """
        try:
            self.cursor.execute("SELECT * FROM %s" % table_name)
            return self.cursor.fetchall()
        except sqlite3.Error as er:
            print('Error message:', er.args[0])
            return False
