#https://blog.manash.me/quick-pyqt5-1-signal-and-slot-example-in-pyqt5-bf502ccaf11d <- used for import done signal
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QCheckBox
from PyQt5.QtWidgets import QGroupBox, QVBoxLayout,QScrollArea, QPushButton
from PyQt5.QtWidgets import QRadioButton, QButtonGroup
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from Ingestor import Ingestor
from DatabaseManager import DatabaseManager

ABSENTEE_DEFAULT_LIST=   ['Site Address','Site City','Site Zip Code','County',"1st Owner's First Name","1st Owner's Last Name"]
DIVORCE_DEFAULT_LIST=    ['Site Address','Site City','Site Zip Code','County',"1st Owner's First Name","1st Owner's Last Name"]
LISTPENDENT_DEFAULT_LIST=['Site Address','Site City','Site Zip Code','County',"1st Owner's First Name","1st Owner's Last Name"]
PROBATE_DEFAULT_LIST=    ['Site Address','Site City','Site Zip Code','County',"1st Owner's First Name","1st Owner's Last Name"]
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
        self.header_button_group = QButtonGroup()
        self.header_button_group.setExclusive(False)
        self.header_button_group_box = QGroupBox('Select which headers you want to import')
        #Make the layout display the buttons vertically
        self.header_button_group_layout = QVBoxLayout()
        self.generate_checkboxes(self.ingestor.getCSVHeaders())
        #Make the window fit the longest word
        self.header_button_group_layout.addStretch(1)
        #set the button group's layout to the layout with the vertically
        #alligned button layout
        self.header_button_group_box.setLayout(self.header_button_group_layout)

        #Create a area that has a scroll bar
        scrollArea = QScrollArea()
        scrollArea.setWidget(self.header_button_group_box)
        scrollArea.horizontalScrollBar().setEnabled(False)

        self.commonHeaderGroup = QButtonGroup()
        #Create a group of common headers buttons
        self.commonHeaderGroupBox = QGroupBox('Select a default header setup')
        #Make the layout display the buttons vertically
        self.commonHeaderGroupLayout = QVBoxLayout()
        #For each common file types make a radio button
        self.generate_radiobuttons(self.commonFileTypes)
        #Allow window to stretch to longest word
        self.commonHeaderGroupLayout.addStretch(1)
        #Set the groups layout to the one with the added buttons
        self.commonHeaderGroupBox.setLayout(self.commonHeaderGroupLayout)

        #List of button groups
        self.buttonGroups = [self.commonHeaderGroup,self.header_button_group]

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
        layout.addWidget(self.commonHeaderGroupBox,3,1,1,2)
        layout.addWidget(cancelButton,4,1)
        layout.addWidget(importButton,4,2)
        self.setLayout(layout)
        self.resize(self.sizeHint())

    def generate_checkboxes(self, button_name_list):
        for button_name in button_name_list:
            #Add each button to the layout from the csv file
            checkbox = QCheckBox(button_name)
            self.header_button_group.addButton(checkbox)
            self.header_button_group_layout.addWidget(self.header_button_group.buttons()[-1])

    def generate_radiobuttons(self,button_name_list):
        count = 0
        for button_name in button_name_list:
            radioButton = QRadioButton(button_name)
            self.commonHeaderGroup.addButton(radioButton,count)
            self.commonHeaderGroupLayout.addWidget(self.commonHeaderGroup.buttons()[-1])
            count += 1


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
            print(searchCritera)

            buttonText = self.buttonGroups[0].buttons()[buttonID].text()
            print(buttonText)
            #buttonText = self.buttonGroups[0].id(self.buttonGroups[0].checkedId()).text()

            #Check which table coresponds with the button pressed
            for tableName in self.tablesInDB:
                #print('%s == %s' % (buttonText.replace(' ','_'), tableName))
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
                        self.db.create_table_list(tableName,self.db.remove_spaces(DEFAULT_LISTS[buttonID]),'string')

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
            for item in self.buttonGroups[1].buttons():
                if item.isChecked():
                    print(item.text())

            print(self.db.is_valid_string(self.tableNameField.text().replace(' ','_')))
            #self.import_done()

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
