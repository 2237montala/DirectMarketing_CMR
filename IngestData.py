#This file  is used to take and inputed excel file,csv, or text
#file and import it into the database
#https://www.datacamp.com/community/tutorials/python-excel-tutorial
#http://zetcode.com/articles/openpyxl/
#import openpyxl ## library for excel sheet

#FilePath = "/home/anthonym/Documents/SchoolWork/SoftwareEngineering/CMR_TestData.xlsx"

#Open the work book at the file path
#workBook = openpyxl.load_workbook(filename = FilePath)
#Open the fist sheet
#currSheet = workBook.active
#currSheetDims = currSheet.dimensions

#print(currSheet['A1'].value)

#for row in range(0,currSheet.max_row):
#    print(row.value)

#print(currSheetDims)
#https://www.geeksforgeeks.org/working-csv-files-python/
from Ingestor import Ingestor

def main():
    filename = "/home/anthonym/Documents/SchoolWork/SoftwareEngineering/Divorce_list_08.20.18_FIXED.csv"
    ingestor = Ingestor(filename)
    ingestor.readCSV()

    print("Header of csv file")
    print(ingestor.getCSVHeaders())
    tempHeaders = ingestor.getCSVHeaders()
    searchCritera = [tempHeaders[2],tempHeaders[3],tempHeaders[5],tempHeaders[6],tempHeaders[22]]

    dict = ingestor.getHeaderIndex(ingestor.listToDict(searchCritera,-1),tempHeaders)
    print("\nDictionary of search critera and their indexes in the csv")
    print(dict)

    print("\nPrint raw list from csv")
    print(ingestor.getRowAt(1))
    ingestor.trimRows(dict,ingestor.getRows())
    print("\nPrint filtered list from unfiltered row")
    print(ingestor.getRowAt(1))

    print("\nNumber of columns")
    print(ingestor.getNumberOfHeaders())

    print("\nNumber of rows")
    print(ingestor.getNumberOfRows())

    print("\nUpdating file to a csv in project folder names newList.csv. Expected:False")
    print(ingestor.updateFileLoc("/home/anthonym/Documents/SchoolWork/SoftwareEngineering/newList.csv"))

    print("\nUpdating file to a csv with no name. Expected:false")
    print(ingestor.updateFileLoc(""))
#Run main method
main()
