#This file  is used to take and inputed excel file,csv, or text
#file and import it into the database
#https://www.datacamp.com/community/tutorials/python-excel-tutorial
#http://zetcode.com/articles/openpyxl/
#https://www.geeksforgeeks.org/working-csv-files-python/

from Ingestor import Ingestor

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
#Run main method
main()
