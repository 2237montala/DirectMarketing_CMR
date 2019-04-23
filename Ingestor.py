import csv
import os

class Ingestor:
    def __init__(self,fileLocation):
        self.filename = fileLocation
        self.rows = []
        self.headers = []


    def listToTwoD(self,list,defaultVal):
        """
        Takes and array and makes it a 2d array with a default value
        """
        newArray = []
        for item in list:
            newArray.append([item,-1])
        return newArray

    def readCSV(self):
        """
        Reads the csv from the file specified in the constructor. It reads in
        the first row as the row if column headers. Then it reads in the
        reamining rows into a 2d array
        """

        try:
            if os.path.exists(self.filename):
                with open(self.filename, 'r') as csvfile:
                    #Created csv reader object
                    csvreader = csv.reader(csvfile)
                    #Reads in first row
                    #next(csvreader) reads in the next row
                    self.headers = next(csvreader)
                    for row in csvreader:
                        #Loops through all rows in csvreader adding it to and array
                        self.rows.append(row)
                return True
        except Exception as er:
            print('Error message:', er.args[0])
            return False
            #If there is an io error return a false
        else:
            return False


    def getHeaderIndex(self,headerList,fieldsList):
        """
        Takes the header dictionary and finds each element in the column
        headers from the fields list. It then updates the integer values
        for each element to match what column it is. All spaces will be replaced
        with underscores
        """
        headerListWithIndex = self.listToTwoD(headerList,-1)

        for i in range(len(headerListWithIndex)):
            count = 0
            for field in fieldsList:
                if field.upper().replace(' ','_') == headerListWithIndex[i][0].upper().replace(' ','_'):
                    headerListWithIndex[i][1] = count
                    headerListWithIndex[i][0] = headerListWithIndex[i][0].replace(' ','_')

                    break
                else:
                    count = count + 1
        return headerListWithIndex

    def searchRow(self,headerListWithIndex, unfilteredRow):
        """
        Takes the header 2d list and an unfiltered row of data and sorts
        it. Using the int value in the 2d list for each element it take
        it from the unfiltered row. The values from the unfiltered row are saved
        in a new array and returned
        """
        filteredRow = []
        for i in range(len(headerListWithIndex)):
            filteredRow.append(unfilteredRow[headerListWithIndex[i][1]])
        return filteredRow

    def searchRows(self,headerDic,unfilteredRows):
        """
        Iderates over all the rows in unfiltered rows and sorts them using
        the dictionary
        """
        newRows = []
        for row in unfilteredRows:
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
