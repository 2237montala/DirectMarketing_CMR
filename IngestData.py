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
import csv

filename = "/home/anthonym/Documents/SchoolWork/SoftwareEngineering/Divorce_list_08.20.18_FIXED.csv"
row = []
fields = []

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = csvreader.next()

    for row in csvreader:
        rows.append(row)

    print("Total no. of rows: %d"%(csvreader.line_num))
