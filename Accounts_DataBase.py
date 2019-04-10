'''
Created on Mar 27, 2019

@author: Alberto Fernandez
'''

import sqlite3
import re
from _sqlite3 import Cursor
from Ingestor import Ingestor

class MyClass(object):
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
        """z
        Creates a table with a name but takes in a list of column header
        Uses the create_table and add column method but with a loop
        """
        self.create_table(table_name,column_name_list[0],column_type)
        for i in range(1,len(column_name_list)):
            self.add_column(table_name,column_name_list[i],'string')
            
    def add_row_list(self, table_name, column_arr, row_arr):
        """
        Adds a rows to the table with specified data. It first adds the value
        related to the first column, then adds the rest by appending to it
        """
        with self.conn:
            self.cursor.execute("INSERT OR IGNORE INTO %s (%s) VALUES(?)" % (table_name,'"{}"'.format(column_arr[0])), (row_arr[0],))
            for i in range(1,len(column_arr)):
                self.cursor.execute("UPDATE %s SET %s='%s' WHERE %s='%s'" % (table_name, '"{}"'.format(column_arr[i]), row_arr[i], column_arr[0], row_arr[0]))

    