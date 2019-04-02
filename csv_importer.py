#https://blog.manash.me/quick-pyqt5-1-signal-and-slot-example-in-pyqt5-bf502ccaf11d <- used for import done signal
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QCheckBox
from PyQt5.QtWidgets import QGroupBox, QVBoxLayout,QScrollArea, QPushButton
from PyQt5.QtWidgets import QRadioButton, QButtonGroup
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from Ingestor import Ingestor
from DatabaseManager import DatabaseManager
from re import search

# ABSENTEE_DEFAULT_LIST=['Site Address','Site City','Site Zip Code','County',"1st Owner's First Name","1st Owner's Last Name"]
ABSENTEE_DEFAULT_LIST=['Street Address','first_name','last name','County',"1st Owner's First Name","1st Owner's Last Name"]
# DIVORCE_DEFAULT_LIST=['Site Address','Site City','Site Zip Code','County',"1st Owner's First Name","1st Owner's Last Name"]
DIVORCE_DEFAULT_LIST=['Site Address','Site City','last_name','County',"1st Owner's First Name","1st Owner's Last Name"]
LISTPENDENT_DEFAULT_LIST=['Site Address','Site City','Site Zip Code','County',"1st Owner's First Name","1st Owner's Last Name"]
PROBATE_DEFAULT_LIST=['Site Address','Site City','Site Zip Code','County',"1st Owner's First Name","1st Owner's Last Name"]
DEFAULT_LISTS=[ABSENTEE_DEFAULT_LIST,DIVORCE_DEFAULT_LIST,LISTPENDENT_DEFAULT_LIST,PROBATE_DEFAULT_LIST]

class csv_importer_popup(QtWidgets.QDialog):
    importDoneSignal = QtCore.pyqtSignal('QString')

    def __init__(self,window_title):
        super().__init__()
        self.title = window_title
        self.setWindowTitle(self.title)
        self.commonFileTypes = ['Absentee', 'Divorce', 'Lis Pendents','Probate']

    def run_popup(self,file_loc,tables,db_file_loc):
        #Signal
        #self.testSignal.connect(closed_function)

        self.tablesInDB = tables

        #CSV file stuff
        self.ingestor = Ingestor(file_loc)
        self.ingestor.readCSV()

        #Database manager stuff
        self.db = DatabaseManager(db_file_loc)

        #Create the check box window
        #Create a group of buttons
        header_button_group = QButtonGroup()
        header_button_group.setExclusive(False)
        header_button_group_box = QGroupBox('Select which headers you want to import')
        #Make the layout display the buttons vertically
        header_button_group_layout = QVBoxLayout()
        for header in self.ingestor.getCSVHeaders():
            #Add each button to the layout from the csv file
            checkbox = QCheckBox(header)
            header_button_group.addButton(checkbox)
            header_button_group_layout.addWidget(header_button_group.buttons()[-1])

        #Make the window fit the longest word
        header_button_group_layout.addStretch(1)
        #set the button group's layout to the layout with the vertically
        #alligned button layout
        header_button_group_box.setLayout(header_button_group_layout)

        #Create a area that has a scroll bar
        scrollArea = QScrollArea()
        scrollArea.setWidget(header_button_group_box)
        scrollArea.horizontalScrollBar().setEnabled(False)

        commonHeaderGroup = QButtonGroup()
        #Create a group of common headers buttons
        commonHeaderGroupBox = QGroupBox('Select a default header setup')
        #Make the layout display the buttons vertically
        commonHeaderGroupLayout = QVBoxLayout()
        #For each common file types make a radio button
        count = 0
        for fileType in self.commonFileTypes:
            radioButton = QRadioButton(fileType)
            commonHeaderGroup.addButton(radioButton,count)
            commonHeaderGroupLayout.addWidget(commonHeaderGroup.buttons()[-1])
            count += 1
        #Allow window to stretch to longest word
        commonHeaderGroupLayout.addStretch(1)
        #Set the groups layout to the one with the added buttons
        commonHeaderGroupBox.setLayout(commonHeaderGroupLayout)

        #List of button groups
        self.buttonGroups = [commonHeaderGroup,header_button_group]

        #Create text field
        self.tableNameField = QtWidgets.QLineEdit('Custom Table Name')

        #Create buttons
        cancelButton = QPushButton('Cancel')
        importButton = QPushButton('Import')

        cancelButton.clicked.connect(self.closeWindow)
        importButton.clicked.connect(self.importCSV)

        #Create the master layout which is a grid
        layout = QGridLayout()
        #Add widgets
        #format of addWidget(widget,row,col,row span, col span)
        layout.addWidget(scrollArea,1,1,1,2)
        layout.addWidget(self.tableNameField,2,1,1,2)
        layout.addWidget(commonHeaderGroupBox,3,1,1,2)
        layout.addWidget(cancelButton,4,1)
        layout.addWidget(importButton,4,2)
        self.setLayout(layout)
        self.resize(self.sizeHint())

    def import_done(self,tableName):
        print("Emiting %s signal name" % tableName)
        self.importDoneSignal.emit(tableName)
        self.accept()

    def closeWindow(self):
        #Closes the window
        self.reject()

    def importCSV(self):
        #If any of the radio buttons are check it will return a number > -1
        if self.buttonGroups[0].checkedId() > -1:
            print("Radio button pressed")
            buttonID = self.buttonGroups[0].checkedId()
            print('Button %d' % buttonID)
            #Use a default list for importing
            searchCritera = self.ingestor.getHeaderIndex(DEFAULT_LISTS[buttonID],self.ingestor.getCSVHeaders())
#             print(searchCritera)
            buttonText = self.buttonGroups[0].buttons()[buttonID].text()
#             print(buttonText)
            #buttonText = self.buttonGroups[0].id(self.buttonGroups[0].checkedId()).text()

            #Check which table coresponds with the button pressed
            for tableName in self.tablesInDB:
                print('%s == %s' % (buttonText.replace(' ','_'), tableName))
                if buttonText.replace(' ','_') == tableName:
                    print(tableName)
                    #print(self.ingestor.getRowAt(0))
                    #Uses the ingestor to search the unfiltered rows using
                    #this search critera list
                    self.ingestor.searchRows(searchCritera,self.ingestor.getRows())
                    rows = self.ingestor.getRows()
                    #Check if tables exists already
                    if not self.db.doesTableExist(tableName):
                        #If not the create it with the table name
                        print("Table created")
                        self.db.create_table_list(tableName,self.db.remove_spaces(DEFAULT_LISTS[buttonID]),'string')
                    else:
                        print("Table not created")

                    #Add the searched rows to the table that was clicked
                    #The seach critera list has to have spaces removed so the db
                    #doesn't get confused
                    self.db.add_list_of_rows(tableName,self.db.remove_spaces(DEFAULT_LISTS[buttonID]),rows)
                    # progress bar (len(rows))
                    # for row in rows
                    #     add row to db
                    #     increment the progress bar 1
                    self.import_done(tableName)


        else:
            #default header option not choosen, so custom lists
            searchCritera = []
            for item in self.buttonGroups[1].buttons():
                if item.isChecked():
                    print(item.text())
                    searchCritera.append(item.text())
            print(searchCritera)
            DEFAULT_LISTS.append(searchCritera)
            newId = len(DEFAULT_LISTS) - 1
            try:
                self.ingestor.searchRows(DEFAULT_LISTS[newId],self.ingestor.getRows())
                rows = self.ingestor.getRows()
                print(rows)
                for tableName in self.tablesInDB:
                    new_table_name = self.db.is_valid_string(self.tableNameField.text().replace(' ','_'))
                    if new_table_name == tableName:
                            print("That table already exists")
                    else:
                        if not self.db.doesTableExist(new_table_name):
                            #If not the create it with the table name
                            print("Table created")
                            self.db.create_table_list(new_table_name,self.db.remove_spaces(DEFAULT_LISTS[newId]),'string')
                        else:
                            print("Table not created")
                    self.db.add_list_of_rows(new_table_name,self.db.remove_spaces(DEFAULT_LISTS[newId]),rows)
                    self.import_done(new_table_name)
            except Exception as e:
                print('Error message:', e.args[0])
            return False

            #What needs to happen after this
            #Get all the check boxes and give them to the csv Ingestor
            #Send the returned filtered data to the DatabaseManager and save
            #it to a new database that has a custom name


#Running this file with run this part of the code
#Makes a pop up window
if __name__ == '__main__':
#     file = "/home/anthonym/Documents/SchoolWork/SoftwareEngineering/Divorce_list_08.20.18_FIXED.csv"
    file = "Test_Files/DatabaseManagerTest_15.csv"
    tables = ['Absentee','Divorce','Lis_Pendents','Probate']
    app = QApplication([])
    csvTest = csv_importer_popup("Test Popup")
    csvTest.run_popup(file,tables,'test.db')
    csvTest.show()
    app.exec_()
