import csv
import os

class Ingestor:
    def __init__(self,fileLocation):
        self.filename = fileLocation
        self.rows = []
        self.headers = []


    def listToDict(self,list,defaultVal):
        dict = {}
        for item in list:
            dict[item] = -1
        return dict

    def readCSV(self):
        with open(self.filename, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            self.headers = next(csvreader)
            #self.searchCritera = self.getHeaderIndex(self.searchCritera,fields)
            for row in csvreader:
                #self.rows.append(self.searchRow(self.searchCritera,row))
                self.rows.append(row)

    def getHeaderIndex(self,headerDic,fieldsList):
        for header in headerDic:
            count = 0
            for field in fieldsList:
                if field.upper() == header.upper():
                    headerDic[header] = count
                    break
                else:
                    count = count + 1
        return headerDic

    def searchRow(self,headerDic, unfilteredRow):
        filteredRow = []
        for header in headerDic:
            filteredRow.append(unfilteredRow[headerDic[header]])

        return filteredRow

    def trimRows(self,headerDic,oldRows):
        newRows = []
        for row in oldRows:
            newRows.append(self.searchRow(headerDic,row))
        self.rows = newRows

    def getCritera(self):
        return self.searchCritera

    def getRows(self):
        return self.rows

    def getRow(self, index):
        return self.rows[index]

    def getNumberOfRow(self):
        return len(self.rows)

    def getNumberOfCritera(self):
        return len(self.searchCritera)

    def getHeaders(self):
        return self.headers

#THIS CODE DOESNT WORK
#Python doesn't keep file open after exiting with open line
# #Make opening the csv and reading the rows 3 different method
# def openCSVFile(self,fName):
#     if os.path.exists(fName):
#         try:
#             with open(fName, 'r') as csvfile:
#                 self.csvReader = csv.reader(csvfile)
#         except IOERROR:
#             return False
#         return True
#     else:
#         return False
#
# def readInHeaders(self):
#     headers = next(self.csvReader)
#     return headers
#
# def readInRowData(self,searchCritera):
#     self.searchCritera = self.getHeaderIndex(searchCritera,fields)
#     for row in self.csvreader:
#         self.rows.append(self.searchRow(self.searchCritera,row))
