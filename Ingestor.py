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
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as csvfile:
                    csvreader = csv.reader(csvfile)
                    self.headers = next(csvreader)
                    for row in csvreader:
                        self.rows.append(row)
            except IOERROR:
                return False
                return True
            else:
                return False


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

    def getRowAt(self, index):
        return self.rows[index]

    def getNumberOfRows(self):
        return len(self.rows)

    def getNumberOfHeaders(self):
        return len(self.headers)

    def getCSVHeaders(self):
        return self.headers

    def getFileLoc(self):
        return self.filename

    def updateFileLoc(self,newLocation):
        if newLocation and os.path.exists(newLocation):
            self.filename = newLocation
            return True
        else:
            return False
