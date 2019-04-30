#https://blog.manash.me/quick-pyqt5-1-signal-and-slot-example-in-pyqt5-bf502ccaf11d <- used for import done signal
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QCheckBox
from PyQt5.QtWidgets import QGroupBox, QVBoxLayout,QScrollArea, QPushButton
from PyQt5.QtWidgets import QRadioButton, QButtonGroup
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from Ingestor import Ingestor
from DatabaseManager import DatabaseManager
from re import search

#Phone number
#status
#interested

class csv_importer_popup(QtWidgets.QDialog):
    #Signals when csv_importer_popup closes
    importDoneSignal = QtCore.pyqtSignal('QString')

    def __init__(self,window_title,db_file_loc,tables,protected_table_prefix):
        super().__init__()
        #Creating the window
        self.title = window_title
        self.setWindowTitle(self.title)
        self.protected_table_prefix = protected_table_prefix
        self.tablesInDB = tables
        #Database manager stuff
        self.db = DatabaseManager(db_file_loc,protected_table_prefix)

        #Create array with tables already in the database to be
        #put in the common files radio button box
        self.default_lists = []
        for table in tables:
            tempList = []
            for columnName in self.db.get_headers(table):
                tempList.append(columnName)
            self.default_lists.append(tempList)

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

        #Create the buttons for tables that already exist in the database
        self.generate_radiobuttons(self.tablesInDB)

        #List of button groups
        self.buttonGroups = [self.commonFileTypesGroup,self.csvHeaderGroup]

        #Create label
        tableNameLabel = QtWidgets.QLabel("Table Name")

        #Create text field
        self.tableNameField = QtWidgets.QLineEdit()
        self.tableNameField.setPlaceholderText("Enter Custom Table Name")

        #Create buttons
        self.cancelButton = QPushButton('Cancel')
        self.importButton = QPushButton('Import')

        self.cancelButton.clicked.connect(self.closeWindow)
        self.importButton.clicked.connect(self.importCSV)

        #Create progress Bar
        self.progressBar = QtWidgets.QProgressBar()

        #Create the master layout which is a grid
        layout = QGridLayout()
        #Add widgets
        #format of addWidget(widget,row,col,row span, col span)
        layout.addWidget(scrollArea,1,1,1,2)
        layout.addWidget(tableNameLabel,2,1,1,2)
        layout.addWidget(self.tableNameField,3,1,1,2)
        layout.addWidget(self.commonFileTypesGroupBox,4,1,1,2)
        layout.addWidget(self.progressBar,5,1,1,2)
        layout.addWidget(self.cancelButton,6,1)
        layout.addWidget(self.importButton,6,2)
        self.setLayout(layout)
        self.resize(self.sizeHint())


    def generate_checkboxes(self, button_name_list):
        #Generate check_boxes
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
        #Generate Radio Buttons
        self.commonFileTypesGroup = QButtonGroup()
        self.commonFileTypesGroupLayout = QVBoxLayout()
        self.commonFileTypesGroupBox = QGroupBox('Select a pre-existing table')
        self.commonFileTypesGroupLayout.addStretch(1)
        count = 0
        for button_name in button_name_list:
            #Add each button from available lists in database
            radioButton = QRadioButton(button_name)
            self.commonFileTypesGroup.addButton(radioButton,count)
            self.commonFileTypesGroupLayout.addWidget(self.commonFileTypesGroup.buttons()[-1])
            count += 1

        self.commonFileTypesGroupBox.setLayout(self.commonFileTypesGroupLayout)


    def import_done(self,tableName):
        #Returns what table was created
        self.importDoneSignal.emit(tableName)
        self.accept()

    def closeWindow(self):
        #Closes the window
        self.reject()

    def importCSV(self):
        self.importButton.setEnabled(False)
        self.cancelButton.setEnabled(False)
        #Check if any radio buttons were pressed by checking if they were
        #checked and save the number in the button group
        radio_button_number = -1
        special_button_number = -1
        count = 0
        for radioButton in self.buttonGroups[0].buttons():
            if radioButton.isChecked():
                radio_button_number = count
                break;
            count += 1
        for specialButton in self.buttonGroups[1].buttons(): # Do the same for the special buttons
            if specialButton.isChecked():
                special_button_number = count
                break;
            count += 1

        if radio_button_number > -1:
            searchCritera = self.ingestor.getHeaderIndex(self.default_lists[radio_button_number]
                                                        ,self.ingestor.getCSVHeaders())
            buttonText = self.buttonGroups[0].buttons()[radio_button_number].text()
            #Check which table corresponds with the button pressed
            for tableName in self.tablesInDB:
                if buttonText.replace(' ','_') == tableName:
                    #Uses the ingestor to search the un-filtered rows using
                    #this search criteria list
                    self.ingestor.searchRows(searchCritera,self.ingestor.getRows())
                    #Check if tables exists already
                    if not self.db.doesTableExist(tableName):
                        #If not the create it with the table name
                        self.db.create_table_list(tableName,
                            self.db.remove_spaces(self.default_lists[radio_button_number]),'string')

                    self.import_with_progress_bar(tableName,self.ingestor.getRows()
                                                ,self.default_lists[radio_button_number])
                    self.import_done(tableName)
        else:
            try:
                if self.tableNameField.text() == '' or self.protected_table_prefix in self.tableNameField.text():
                    raise Exception()
                else:
                    customTableName = self.db.is_valid_string(self.tableNameField.text().replace(' ','_'))
                    if special_button_number > -1:
                        # Default header option not chosen, so custom lists
                        try:
                            requestedHeaders = []
                            for item in self.buttonGroups[1].buttons():
                                if item.isChecked():
                                    requestedHeaders.append(item.text())

                            does_exist = self.db.doesTableExist(customTableName)
                            has_same_cols = True
                            if not does_exist:
                                #If not the create it with the table name
                                self.db.create_table_list(customTableName,self.db.remove_spaces(requestedHeaders),'string')
                            else:
                                #Tables exists. Does it have the same columns?
                                if not(requestedHeaders == self.db.get_headers(customTableName)):
                                    has_same_cols = False
                                    #Find the different column names
                                    #This works by turning the lists into sets
                                    #A set is an unordered list with no duplicate elements
                                    #A set supports matrix operations so you can subtract the two sets
                                    #This returns the elements that are not shared
                                    different_cols = list(set(self.db.remove_spaces(requestedHeaders))
                                                            - set(self.db.get_headers(customTableName)))
                                    #Add the extra columns
                                    for col in different_cols:
                                        self.db.add_column(customTableName,col,'string')

                            if has_same_cols:
                                #New table is identical to existing one
                                searchCritera = self.ingestor.getHeaderIndex(requestedHeaders,self.ingestor.getCSVHeaders())
                                self.ingestor.searchRows(searchCritera,self.ingestor.getRows())
                                rows = self.ingestor.getRows()
                                self.import_with_progress_bar(customTableName, self.ingestor.getRows(),requestedHeaders)
                            else:
                                #New table has different columns
                                #Combine the headers in the lists
                                combinedHeaders = self.db.get_headers(customTableName) + requestedHeaders
                                #Have to re order them to match the csv file
                                newRequestedHeaders = []
                                for header in self.db.remove_spaces(self.ingestor.getCSVHeaders()):
                                    if header in combinedHeaders:
                                        newRequestedHeaders.append(header)
                                searchCritera = self.ingestor.getHeaderIndex(newRequestedHeaders,self.ingestor.getCSVHeaders())
                                self.ingestor.searchRows(searchCritera,self.ingestor.getRows())
                                rows = self.ingestor.getRows()
                                self.import_with_progress_bar(customTableName, self.ingestor.getRows(),newRequestedHeaders)

                            self.import_done(customTableName)
                        except Exception as er:
                            #General error message
                            print('Error message:', er.args[0])
                            return False
                    else:
                        raise Exception()

            except:
                ErrorBox = QtWidgets.QMessageBox()
                choice  = ErrorBox.critical(self, 'Table Name Error',
                                            "Table name can only have letters numbers, and underscores",
                                            ErrorBox.Ok)
                if choice == ErrorBox.Ok:
                    #User wants to try a new name
                    print("Closing")
                    ErrorBox.accept()
                    self.importButton.setEnabled(True)
                    self.cancelButton.setEnabled(True)



    def import_with_progress_bar(self,tableName,rows_to_be_added,column_headers):
        """
        Adds the ingestor rows to the db one row at a time so the progress
        bar will show the progress
        """
        #Set the max value of the progress bar to the number of rows to be add
        self.progressBar.setMaximum(len(rows_to_be_added))
        #self.db.add_list_of_rows(tableName,self.db.remove_spaces(self.default_lists[button_number]),rows)
        count = 0
        for row in rows_to_be_added:
            #For every row to be added add it to the db and increment the progress
            #bar value by 1
            count += 1
            self.db.add_row_list(tableName,self.db.remove_spaces(column_headers),row)
            self.progressBar.setValue(count)



#Running this file with run this part of the code
#Makes a pop up window
if __name__ == '__main__':
    file = "Test_Files/DatabaseManagerTest_15.csv"
    tables = ['Absentee','Divorce','Lis_Pendents','Probate']
    app = QApplication([])
    csvTest = csv_importer_popup("Test Popup",'test.db',tables,'__ADMIN__')
    csvTest.run_popup(file)
    csvTest.show()
    app.exec_()
