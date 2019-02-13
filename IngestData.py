#This file  is used to take and inputed excel file,csv, or text
#file and import it into the database
#https://www.datacamp.com/community/tutorials/python-excel-tutorial
#http://zetcode.com/articles/openpyxl/
import openpyxl ## library for excel sheet

FilePath = "/home/anthonym/Documents/SchoolWork/SoftwareEngineering/CMR_TestData.xlsx"

#Open the work book at the file path
workBook = openpyxl.load_workbook(filename = FilePath)
#Open the fist sheet
currSheet = workBook.active
currSheetDims = currSheet.dimensions

print(currSheet['A1'].value)

for row in currSheetDims:
    for cell in row:
        print(cell.value)

print(currSheetDims)
