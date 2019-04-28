#This file  is used to take and inputed excel file,csv, or text
#file and import it into the database
#https://www.datacamp.com/community/tutorials/python-excel-tutorial
#http://zetcode.com/articles/openpyxl/
#https://www.geeksforgeeks.org/working-csv-files-python/

from Ingestor import Ingestor
import unittest

class IngestorTest(unittest.TestCase):
    def setUp(self):
        filename = 'Test_Files/DatabaseManagerTest_15.csv'
        self.ingestor = Ingestor(filename)
        self.ingestor.readCSV()


    def test_headers(self):
        headerList = ["Street Address","owner's first name","last_name","Long","email","phone Number","Loan Amount","Lat"]
        #self.assertEqual(self.ingestor.getCSVHeaders(),headerList)

    def test_search_headers(self):
        searchCritera = ["last_name","Long","phone Number"]
        expectedRetun = [["last_name",2],["Long",3],["phone_Number",5]]

        self.assertEqual(self.ingestor.getHeaderIndex(searchCritera,self.ingestor.getCSVHeaders()),expectedRetun)

    def test_get_row(self):
        expectedRetun = ["8 Hoard Court","Samuele","Gulliver","-64.1305924","sgulliver0@yahoo.co.jp","+54 (656) 804-6029","$14,895.21 ","-31.4325479"]
        self.assertEqual(self.ingestor.getRowAt(0),expectedRetun)

    def test_get_row_filtered(self):
        searchCritera = [["last_name",2],["Long",3],["phone_Number",5]]
        expectedRetun = ["Gulliver","-64.1305924","+54 (656) 804-6029"]
        self.ingestor.searchRows(searchCritera,self.ingestor.getRows())
        self.assertEqual(self.ingestor.getRowAt(0),expectedRetun)

        expectedRetun = ["Scoullar","121.5570313","+63 (634) 506-0432"]
        self.assertEqual(self.ingestor.getRowAt(4),expectedRetun)

    def test_number_of_headers(self):
        self.assertEqual(self.ingestor.getNumberOfHeaders(),8)

    def test_number_of_row(self):
        self.assertEqual(self.ingestor.getNumberOfRows(),15)


    def test_switch_files(self):
        self.assertFalse(self.ingestor.updateFileLoc(""))
        self.assertTrue(self.ingestor.updateFileLoc("Test_Files/DatabaseManagerTest_1000.csv"))

if __name__ == '__main__':
    unittest.main()
