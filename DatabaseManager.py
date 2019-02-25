import sqlite3

class DatabaseManager:
    def __init__ (self, file_loc):
        self.conn = sqlite3.connect(file_loc)
        self.cursor = self.conn.cursor()

    def create_table(self, table_name, column_name, column_type):
        with self.conn:
          #  if  not doesTableExist(table_name):
          if not self.doesTableExist(table_name):
              self.cursor.execute("CREATE TABLE %s (%s %s PRIMARY KEY)" % (table_name, column_name, column_type))
              self.conn.commit()
              return True
          else:
                #Returns false if table already exists
                return False

    def doesTableExist(self, table_name):
#         c.execute("""SELECT COUNT(*) FROM %s WHERE 'TEST_TABLE_1' """ % (table_name))
        try:
            self.cursor.execute("SELECT * FROM sqlite_master WHERE name = '%s' AND type = 'table'" % table_name)
            if self.cursor.fetchone()[1] == table_name:
#                 print("Table exists")
                return True
            else:
#                 print("Table doesn't exist")
                return False
        except:
            return False

    def return_table(self, table_name):
        try:
            self.cursor.execute("SELECT * FROM %s" % table_name)
            return self.cursor.fetchall()
        except:
            return "Table doesn't exist"

    def add_column(self, table_name,column_name, column_type):
        #self.cursor.execute("ALTER TABLE %s ADD COLUMN %s %s" % (table_name,'"{}"'.format(column_name) ,column_type))
        try:
            self.cursor.execute("ALTER TABLE %s ADD COLUMN %s %s" % (table_name,'"{}"'.format(column_name) ,column_type))
            return True
        except sqlite3.Error as er:
            print 'er:', er.message
            return False

    # def add_row(self, table_name, column, row):
    #     with self.conn:
    #         self.cursor.execute("INSERT OR IGNORE INTO %s (%s) VALUES(?)" % (table_name,'"{}"'.format(column)), ('"{}"'.format(row_arr[0])))
    #         for i in range(1,len(column_arr)):
    #             self.cursor.execute("UPDATE %s SET %s='%s' WHERE %s='%s' " % (table_name, column_arr, row_arr[i], column_arr[0], row_arr[0]))

    def add_row_list(self, table_name, column_arr, row_arr):
        with self.conn:
            print('"{}"'.format(row_arr[0]))
            self.cursor.execute("INSERT OR IGNORE INTO %s (%s) VALUES(?)" % (table_name,'"{}"'.format(column_arr[0])), (row_arr[0],))
            for i in range(1,len(column_arr)):
                self.cursor.execute("UPDATE %s SET %s='%s' WHERE %s='%s'" % (table_name, '"{}"'.format(column_arr[i]), row_arr[i], column_arr[0], row_arr[0]))

    def clear_table(self, table_name):
        with self.conn:
                self.cursor.execute("DELETE FROM %s" % table_name)
