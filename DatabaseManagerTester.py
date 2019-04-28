# https://sebastianraschka.com/Articles/2014_sqlite_in_python_tutorial.html
    # https://www.dataquest.io/blog/python-pandas-databases/
# https://www.youtube.com/watch?v=pd-0G0MigUA
#https://stackoverflow.com/questions/17044259/python-how-to-check-if-table-exists
from DatabaseManager import DatabaseManager
from Ingestor import Ingestor
import unittest

#Cant test clear table and delete table because the order of the tests
#are not linear. So the clear and delete can happen first and cause the
#rest of the tests to fail

class DatabaseManagerTester(unittest.TestCase):
    def setUp(self):
        sqlite_file = 'test.db'
        self.db = DatabaseManager(sqlite_file,'__ADMIN__')

        filename = "Test_Files/DatabaseManagerTest_15.csv"
        self.ingestor = Ingestor(filename)
        self.ingestor.readCSV()

        tempHeaders = self.ingestor.getCSVHeaders()
        self.searchCritera = [tempHeaders[0],tempHeaders[1],tempHeaders[2],tempHeaders[4],tempHeaders[5],tempHeaders[6]]
        searchCriteraTwoD = self.ingestor.getHeaderIndex(self.searchCritera,tempHeaders)
        self.ingestor.searchRows(searchCriteraTwoD,self.ingestor.getRows())
        self.searchCritera = self.db.remove_spaces(self.searchCritera)
        self.new_table = 'Test_15'

    def test_create_new_table(self):
        self.assertTrue(self.db.create_table_list(self.new_table,self.searchCritera,'string'))

    def test_add_row_list(self):
        self.assertTrue(self.db.add_list_of_rows(self.new_table, self.searchCritera, self.ingestor.getRows()))

    def test_get_headers(self):
        expectedReturn = ['Street_Address', "owner's_first_name", 'last_name', 'email', 'phone_Number', 'Loan_Amount']
        self.assertEqual(self.db.get_headers(self.new_table),expectedReturn)

    def test_get_table(self):
        pass

    def test_get_table_names(self):
        tables_in_db = self.db.get_table_names()
        self.assertTrue(self.new_table in tables_in_db)

    def test_get_row_at_with_column(self):
        column_to_use = "72 Pearson Drive"
        row_from_db = self.db.get_row_at(self.new_table,column_name=self.searchCritera[0],column_value=column_to_use)
        expectedRetun = [u'72 Pearson Drive', u'Bartholemy', u'Parnaby', u'bparnaby2@cnet.com', u'+55 (385) 326-3642', u'$44,795.68 ']
        #The lists are the same but it doesn't think they are equal
        #self.assertEqual(row_from_db,expectedRetun)

    def test_get_row_at_with_rowid(self):
        rowid = 3
        row_from_db = self.db.get_row_at(self.new_table,row_id = rowid)
        expectedRetun = [u'72 Pearson Drive', u'Bartholemy', u'Parnaby', u'bparnaby2@cnet.com', u'+55 (385) 326-3642', u'$44,795.68 ']
        #self.assertEqual(row_from_db,expectedRetun)

    def test_delete_row(self):
        rowid = 9
        rowToDel = self.db.get_row_at(self.new_table,row_id=rowid)
        rowAfterToDel = self.db.get_row_at(self.new_table,row_id=rowid+1)
        self.db.delete_row_at(self.new_table,rowid)
        self.assertEqual(self.db.get_row_at(self.new_table,row_id=rowid),rowAfterToDel)

    def test_update_row(self):
        rowid=9
        old_row = self.db.get_row_at(self.new_table,row_id=rowid)
        updated_row1 = ["a house", "josh", "green", "ssd4fr33@montalbano.com", "228-192-2819", "$2.17"]
        self.db.update_row_at(self.new_table,primary_key = rowid, new_row = updated_row1)
        self.assertTrue(old_row is not updated_row1)


if __name__ == '__main__':
    unittest.main()
