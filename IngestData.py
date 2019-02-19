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

# def getHeaderIndex(headerDic,fieldsList):
#     for header in headerDic:
#         count = 0
#         for field in fieldsList:
#             if field.upper() == header.upper():
#                 headerDic[header] = count
#             else:
#                 count = count + 1
#
#     return headerDic
#
# def searchRow(headerDic, unfilteredRow):
#     filteredRow = []
#
#     for header in headerDic:
#         filteredRow.append(unfilteredRow[headerDic[header]])
#
#     return filteredRow
from Ingestor import Ingestor

def main():
    filename = "/home/anthonym/Documents/SchoolWork/SoftwareEngineering/Divorce_list_08.20.18_FIXED.csv"
    ingestor = Ingestor(filename)
    ingestor.readCSV()

    print(ingestor.getHeaders())
    tempHeaders = ingestor.getHeaders()
    searchCritera = [tempHeaders[2],tempHeaders[3],tempHeaders[5],tempHeaders[6],tempHeaders[22]]
    dict = ingestor.getHeaderIndex(ingestor.listToDict(searchCritera,-1),tempHeaders)
    print(dict)

    print(ingestor.getRow(1))
    ingestor.trimRows(dict,ingestor.getRows())
    print(ingestor.getRow(1))


#Run main method
main()
