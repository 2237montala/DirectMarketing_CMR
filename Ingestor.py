import csv

class Ingestor:
    def __init__(self,fileLocation,srchCritera):
        self.filename = fileLocation
        self.searchCritera=self.listToDict(srchCritera,-1)
        self.rows = []


    def listToDict(self,list,defaultVal):
        dict = {}

        for item in list:
            dict[item] = -1

        return dict

    #Make opening the csv and reading the rows 3 different method
    def openCSVFile(self):
    def readInHeaders(self):
    def readInRowData(self):

    def readCSV(self):
        with open(self.filename, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            fields = next(csvreader)
            self.searchCritera = self.getHeaderIndex(self.searchCritera,fields)
            for row in csvreader:
                self.rows.append(self.searchRow(self.searchCritera,row))

    def getHeaderIndex(self,headerDic,fieldsList):
        for header in headerDic:
            count = 0
            for field in fieldsList:
                if field.upper() == header.upper():
                    headerDic[header] = count
                else:
                    count = count + 1

        return headerDic

    def searchRow(self,headerDic, unfilteredRow):
        filteredRow = []

        for header in headerDic:
            filteredRow.append(unfilteredRow[headerDic[header]])

        return filteredRow

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
