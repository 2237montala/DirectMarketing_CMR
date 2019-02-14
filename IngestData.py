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

def getHeaderIndex(headerDic,fieldsList):
    for header in headerDic:
        count = 0
        for field in fieldsList:
            if field.upper() == header.upper():
                headerDic[header] = count
            else:
                count = count + 1

    return headerDic

def main():
    filename = "/home/anthonym/Documents/SchoolWork/SoftwareEngineering/Divorce_list_08.20.18_FIXED.csv"
    rows = []
    fields = []
    reqHeaders={"Site Address":-1,"Site City":-1,"Site Zip Code":-1}

    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        fields = next(csvreader)

        # for header in reqHeaders:
        #     count = 0
        #     for field in fields:
        #         if field.upper() == header.upper():
        #             reqHeaders[header] = count
        #         else:
        #             count = count + 1

        reqHeaders = getHeaderIndex(reqHeaders,fields)

        print("Number of headers: %d" % len(fields))

        for name, value in reqHeaders.items():
            print(name,value)

        for row in csvreader:
            rows.append(row)

        print("Total no. of rows: %d"%(csvreader.line_num))
