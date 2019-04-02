#https://blog.manash.me/quick-pyqt5-1-signal-and-slot-example-in-pyqt5-bf502ccaf11d <- used for import done signal
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QCheckBox
from PyQt5.QtWidgets import QGroupBox, QVBoxLayout,QScrollArea, QPushButton
from PyQt5.QtWidgets import QRadioButton, QButtonGroup
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from Ingestor import Ingestor
from DatabaseManager import DatabaseManager
from re import search

ABSENTEE_DEFAULT_LIST=   ['Site Address','Site City','Site Zip Code','County',"1st Owner's First Name","1st Owner's Last Name"]
DIVORCE_DEFAULT_LIST=    ['Site Address','Site City','Site Zip Code','County',"1st Owner's First Name","1st Owner's Last Name"]
LISTPENDENT_DEFAULT_LIST=['Site Address','Site City','Site Zip Code','County',"1st Owner's First Name","1st Owner's Last Name"]
PROBATE_DEFAULT_LIST=    ['Site Address','Site City','Site Zip Code','County',"1st Owner's First Name","1st Owner's Last Name"]
DEFAULT_LISTS = []

class csv_importer_popup(QtWidgets.QDialog):
    importDoneSignal = QtCore.pyqtSignal('QString')

    def __init__(self,window_title,db_file_loc,tables):
        super().__init__()
        self.title = window_title
        self.setWindowTitle(self.title)

        self.tablesInDB = tables
        #Database manager stuff
        self.db = DatabaseManager(db_file_loc)

        #Create array with tables already in the db to be
        #put in the common files radio button box
        self.default_lists = []
        for table in tables:
            tempList = []
            for columnName in self.db.get_headers(table):
                tempList.append(columnName)
            self.default_lists.append(tempList)

        print(self.default_lists)


        self.layout = QGridLayout()

    def run_popup(self,file_loc):
        #CSV file stuff
        self.ingestor = Ingestor(file_loc)
        self.ingestor.readCSV()

        self.rows = self.ingestor.getCSVHeaders()

        #Create buttons from the csv file headers that was just selected
        self.generate_checkboxes(self.rows)

        #Create a area that has a scroll bar
        scrollArea = QScrollArea()
        scrollArea.setWidget(self.csvHeaderGroup_box)
        scrollArea.horizontalScrollBar().setEnabled(False)

        #Create the buttson for tables that already exist in the db
        self.generate_radiobuttons(self.tablesInDB)

        #List of button groups
        self.buttonGroups = [self.commonFileTypesGroup,self.csvHeaderGroup]

        #Create text field
        self.tableNameField = QtWidgets.QLineEdit('Custom Table Name')

        #Create buttons
        self.cancelButton = QPushButton('Cancel')
        self.importButton = QPushButton('Import')

        self.cancelButton.clicked.connect(self.closeWindow)
        self.importButton.clicked.connect(self.importCSV)

        #Create the master layout which is a grid
        layout = QGridLayout()
        #Add widgets
        #format of addWidget(widget,row,col,row span, col span)
        layout.addWidget(scrollArea,1,1,1,2)
        layout.addWidget(self.tableNameField,2,1,1,2)
        layout.addWidget(self.commonFileTypesGroupBox,3,1,1,2)
        layout.addWidget(self.cancelButton,4,1)
        layout.addWidget(self.importButton,4,2)
        self.setLayout(layout)
        self.resize(self.sizeHint())


    def generate_checkboxes(self, button_name_list):
        print(button_name_list)
        self.csvHeaderGroup = QButtonGroup()
        self.csvHeaderGroup_layout = QVBoxLayout()
        self.csvHeaderGroup.setExclusive(False)
        self.csvHeaderGroup_box = QGroupBox('Select which headers')
        self.csvHeaderGroup_layout.addStretch(1)
        for button_name in button_name_list:
            #Add each button to the layout from the csv file
            checkbox = QCheckBox(button_name)
            self.csvHeaderGroup.addButton(checkbox)
            self.csvHeaderGroup_layout.addWidget(self.csvHeaderGroup.buttons()[-1])

        self.csvHeaderGroup_box.setLayout(self.csvHeaderGroup_layout)

    def generate_radiobuttons(self,button_name_list):
        self.commonFileTypesGroup = QButtonGroup()
        self.commonFileTypesGroupLayout = QVBoxLayout()
        self.commonFileTypesGroupBox = QGroupBox('Select a default header setup')
        self.commonFileTypesGroupLayout.addStretch(1)
        count = 0
        for button_name in button_name_list:
            radioButton = QRadioButton(button_name)
            self.commonFileTypesGroup.addButton(radioButton,count)
            self.commonFileTypesGroupLayout.addWidget(self.commonFileTypesGroup.buttons()[-1])
            count += 1

        self.commonFileTypesGroupBox.setLayout(self.commonFileTypesGroupLayout)


    def import_done(self,tableName):
        print("Emiting %s signal name" % tableName)
        self.importDoneSignal.emit(tableName)
        self.accept()

    def closeWindow(self):
        #Closes the window
        self.reject()

    def importCSV(self):
        self.importButton.setEnabled(False)
        self.cancelButton.setEnabled(False)
        #Check if any radio buttons were presssed by checking if they were
        #checked and save the number in the button group
        button_number = -1
        count = 0
        for radioButton in self.buttonGroups[0].buttons():
            print(count)
            if radioButton.isChecked():
                print(radioButton.text())
                button_number = count
                break;
            count += 1

        if button_number > -1:
            searchCritera = self.ingestor.getHeaderIndex(self.default_lists[button_number],self.ingestor.getCSVHeaders())
            print(searchCritera)

            buttonText = self.buttonGroups[0].buttons()[button_number].text()
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
                        self.db.create_table_list(tableName,self.db.remove_spaces(self.default_lists[button_number]),'string')

                    #Add the searched rows to the table that was clicked
                    #The seach critera list has to have spaces removed so the db
                    #doesn't get confused
                    self.db.add_list_of_rows(tableName,self.db.remove_spaces(self.default_lists[button_number]),rows)
                    # progress bar (len(rows))
                    # for row in rows
                    #     add row to db
                    #     increment the progress bar 1
                    self.import_done(tableName)


        else:
            #default header option not choosen, so custom lists
            requestedHeaders = []
            for item in self.buttonGroups[1].buttons():
                if item.isChecked():
                    #print(item.text())
                    requestedHeaders.append(item.text())

            searchCritera = self.ingestor.getHeaderIndex(requestedHeaders,self.ingestor.getCSVHeaders())
            print(searchCritera)

            customTableName = self.db.is_valid_string(self.tableNameField.text().replace(' ','_'))
            print(customTableName)

            self.ingestor.searchRows(searchCritera,self.ingestor.getRows())
            rows = self.ingestor.getRows()
            #print(rows)

            if not self.db.doesTableExist(customTableName):
                #If not the create it with the table name
                print('%s doesn\'t exist. Creating' % customTableName)
                self.db.create_table_list(customTableName,self.db.remove_spaces(requestedHeaders),'string')

            self.db.add_list_of_rows(customTableName,self.db.remove_spaces(requestedHeaders),rows)
            self.import_done(customTableName)
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
    csvTest = csv_importer_popup("Test Popup",'test.db',tables)
    csvTest.run_popup(file)
    csvTest.show()
    app.exec_()
