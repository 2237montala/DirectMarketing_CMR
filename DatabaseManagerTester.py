# https://sebastianraschka.com/Articles/2014_sqlite_in_python_tutorial.html
    # https://www.dataquest.io/blog/python-pandas-databases/
# https://www.youtube.com/watch?v=pd-0G0MigUA
#https://stackoverflow.com/questions/17044259/python-how-to-check-if-table-exists
from DatabaseManager import DatabaseManager
from Ingestor import Ingestor
import unittest

class DatabaseManagerTester(unittest.TestCase):
    def setup(self):
        sqlite_file = 'test.db'
        self.db = DatabaseManager(sqlite_file,'__ADMIN__')

        filename = "Test_Files/DatabaseManagerTest_15.csv"
        ingestor = Ingestor(filename)
        self.ingestor.readCSV()

        tempHeaders = self.ingestor.getCSVHeaders()
        self.searchCritera = [tempHeaders[0],tempHeaders[1],tempHeaders[2],tempHeaders[4],tempHeaders[5],tempHeaders[6]]
        searchCriteraTwoD = self.ingestor.getHeaderIndex(self.searchCritera,tempHeaders)
        self.ingestor.searchRows(searchCriteraTwoD,self.ingestor.getRows())
        self.searchCritera = self.db.remove_spaces(searchCritera)
        self.new_table = 'Test_15'

    def test_create_new_table(self):
        self.assertTrue(self.db.create_table_list(self.new_table,self.searchCritera,'string'))

if __name__ == '__main__':
    unittest.main()
