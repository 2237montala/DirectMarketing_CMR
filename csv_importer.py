from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QCheckBox, QGroupBox, QVBoxLayout,QScrollArea
from Ingestor import Ingestor

class csv_importer_popup(QWidget):
    def __init__(self,window_title,file_loc):
        super().__init__()
        self.title = window_title
        #self.setWindowTitle(self.title)

        #CSV file stuff
        ingestor = Ingestor(file_loc)
        ingestor.readCSV()

        #Create the check box window
        #Create a group of buttons
        button_group = QGroupBox('Select which headers you want to import')
        #Make the layout display the buttons vertically
        button_group_layout = QVBoxLayout()
        for header in ingestor.getCSVHeaders():
            #Add each button to the layout from the csv file
            button_group_layout.addWidget(QCheckBox(header))

        #Make the window fit the longest word
        button_group_layout.addStretch(1)
        #set the button group's layout to the layout with the vertically
        #alligned button layout
        button_group.setLayout(button_group_layout)

        #Create a area that has a scroll bar
        scrollArea = QScrollArea()
        scrollArea.setWidget(button_group)
        scrollArea.horizontalScrollBar().setEnabled(False)

        #Create the master layout which is a grid
        layout = QGridLayout()

        #Add widgets
        #format of addWidget(widget,row,col,row span, col span)
        layout.addWidget(scrollArea,1,1)
        self.setLayout(layout)

        print('displaying')

        #Only here so if you run this class something shows up
        self.show()


#Running this file with run this part of the code
#Makes a pop up window
if __name__ == '__main__':
    file = "/home/anthonym/Documents/SchoolWork/SoftwareEngineering/Divorce_list_08.20.18_FIXED.csv"
    app = QApplication([])
    ex = csv_importer_popup('Test',file)
    app.exec_()
