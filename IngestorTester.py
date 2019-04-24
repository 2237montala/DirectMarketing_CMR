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
        expectedRetun = ["8 Hoard Court","Samuele","Gulliver","-64.1305924","sgulliver0@yahoo.co.jp","+54 (656) 804-6029","$14895.21","-31.4325479"]
        self.assertEqual(self.ingestor.getRowAt(0),expectedRetun)

    def test_switch_files(self):
        self.assertFalse(self.ingestor.updateFileLoc(""))
        self.assertTrue(self.ingestor.updateFileLoc("Test_Files/DatabaseManagerTest_1000.csv"))


def main():
    filename = 'Test_Files/DatabaseManagerTest_15.csv'
    ingestor = Ingestor(filename)
    ingestor.readCSV()

    print("Header of csv file")
    print(ingestor.getCSVHeaders())
    tempHeaders = ingestor.getCSVHeaders()
    searchCritera = [tempHeaders[2],tempHeaders[3],tempHeaders[5]]

    searchCritera = ingestor.getHeaderIndex(searchCritera,tempHeaders)
    print("\nDictionary of search critera and their indexes in the csv")
    print(searchCritera)

    print("\nPrint raw list from csv")
    print(ingestor.getRowAt(1))
    ingestor.searchRows(searchCritera,ingestor.getRows())
    print("\nPrint filtered list from unfiltered row")
    print(ingestor.getRowAt(1))

    print(ingestor.getRowAt(2))
    print(ingestor.getRowAt(3))
    print(ingestor.getRowAt(4))

    print("\nNumber of columns")
    print(ingestor.getNumberOfHeaders())

    print("\nNumber of rows")
    print(ingestor.getNumberOfRows())

    print("\nUpdating file to a csv in project folder names newList.csv. Expected:False")
    print(ingestor.updateFileLoc("/home/anthonym/Documents/SchoolWork/SoftwareEngineering/newList.csv"))

    print("\nUpdating file to a csv with no name. Expected:false")
    print(ingestor.updateFileLoc(""))

    print("\nUpdating file to a csv with location Test_Files/DatabaseManagerTest_1000.csv. Expected:true")
    print(ingestor.updateFileLoc("Test_Files/DatabaseManagerTest_1000.csv"))


if __name__ == '__main__':
    unittest.main()
