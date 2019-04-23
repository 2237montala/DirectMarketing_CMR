# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Property_Profile.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from distutils.log import info
from PyQt5.Qt import QWidget, QApplication, QAbstractItemView, QTableWidgetItem
from _sqlite3 import Row

import webbrowser
#from ShowList import ShowList

class UI_ProfilePage(QWidget):

    CheckEdit = True
    header = ["Adress:", "City:", "Zip Code:", "State:","Status","Baths:","Comments of Property"]
    information = ["517 Madison Ave", "Glencoe", "60022","Illinois","0",'10',"comments"]

    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setObjectName("Form")
        self.resize(1122, 847)
        self.label_13 = QtWidgets.QLabel(self)
        self.label_13.setGeometry(QtCore.QRect(720, 60, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_7 = QtWidgets.QLabel(self)
        self.label_7.setGeometry(QtCore.QRect(190, 60, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_11 = QtWidgets.QLabel(self)
        self.label_11.setGeometry(QtCore.QRect(0, 0, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.line = QtWidgets.QFrame(self)
        self.line.setGeometry(QtCore.QRect(0, 30, 1121, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.clicked.connect(self.Handle_edit)
        self.pushButton.setGeometry(QtCore.QRect(990, 0, 121, 28))
        self.pushButton.setObjectName("pushButton")
        self.house_info = QtWidgets.QTableWidget(self)
        self.house_info.setGeometry(QtCore.QRect(40, 80, 491, 441))
        self.house_info.setObjectName("house_info")

        self.house_info.setColumnCount(1)
        self.house_info.setRowCount(13)
        item = QtWidgets.QTableWidgetItem()
        self.house_info.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        #item.setFlags(item.flags() != QtCore.Qt.ItemIsEditable)
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.house_info.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.house_info.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.house_info.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.house_info.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.house_info.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.house_info.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.house_info.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.house_info.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.house_info.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.house_info.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.house_info.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.house_info.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.house_info.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.house_info.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.house_info.setHorizontalHeaderItem(0, item)
        self.house_info.horizontalHeader().setDefaultSectionSize(300)
        self.owner_info = QtWidgets.QTableWidget(self)
        self.owner_info.setGeometry(QtCore.QRect(560, 80, 521, 441))
        self.owner_info.setObjectName("owner_info")
        self.owner_info.setColumnCount(1)
        self.owner_info.setRowCount(11)
        item = QtWidgets.QTableWidgetItem()
        self.house_info.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.house_info.setHorizontalHeaderItem(0, item)
        # item = QtWidgets.QTableWidgetItem()
        # brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        # brush.setStyle(QtCore.Qt.NoBrush)
        # item.setForeground(brush)
        # self.house_info.setItem(0, 0, item)
        self.house_info.horizontalHeader().setDefaultSectionSize(300)
        self.owner_info = QtWidgets.QTableWidget(self)
        self.owner_info.setGeometry(QtCore.QRect(560, 80, 521, 441))
        self.owner_info.setObjectName("owner_info")
        self.owner_info.setColumnCount(1)
        self.owner_info.setRowCount(11)
        item = QtWidgets.QTableWidgetItem()
        self.owner_info.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.owner_info.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.owner_info.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.owner_info.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.owner_info.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.owner_info.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.owner_info.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.owner_info.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.owner_info.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.owner_info.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.owner_info.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()

        self.owner_info.setHorizontalHeaderItem(0, item)


        item = QtWidgets.QTableWidgetItem()

        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.HorPattern)
        item.setForeground(brush)
        self.owner_info.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)

        self.owner_info.horizontalHeader().setDefaultSectionSize(300)
        self.label_8 = QtWidgets.QLabel(self)
        self.label_8.setGeometry(QtCore.QRect(40, 540, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.AdditionalInfo_txt = QtWidgets.QPlainTextEdit(self)
        self.AdditionalInfo_txt.setReadOnly(True)
        self.AdditionalInfo_txt.setGeometry(QtCore.QRect(40, 570, 431, 261))
        self.AdditionalInfo_txt.setObjectName("AdditionalInfo_txt")
        self.AdditionalInfo_txt.setPlainText("Comments of Property")
        self.label_9 = QtWidgets.QLabel(self)
        self.label_9.setGeometry(QtCore.QRect(490, 540, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.Button_NOresponse = QtWidgets.QCheckBox(self)
        self.Button_NOresponse.setGeometry(QtCore.QRect(740, 590, 131, 20))
        self.Button_NOresponse.setObjectName("Button_NOresponse")
        self.Respond_person = QtWidgets.QCheckBox(self)
        self.Respond_person.setGeometry(QtCore.QRect(890, 590, 141, 20))
        self.Respond_person.setObjectName("Respond_person")
        self.Button_responded = QtWidgets.QCheckBox(self)
        self.Button_responded.setGeometry(QtCore.QRect(630, 590, 95, 20))
        self.Button_responded.setObjectName("Button_responded")
        self.Very_interested = QtWidgets.QCheckBox(self)
        self.Very_interested.setGeometry(QtCore.QRect(630, 640, 111, 20))
        self.Very_interested.setObjectName("Very_interested")
        self.Interested = QtWidgets.QCheckBox(self)
        self.Interested.setGeometry(QtCore.QRect(770, 640, 95, 20))
        self.Interested.setObjectName("Interested")
        self.Not_interested = QtWidgets.QCheckBox(self)
        self.Not_interested.setGeometry(QtCore.QRect(890, 640, 111, 20))
        self.Not_interested.setObjectName("Not_interested")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(550, 590, 41, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(530, 640, 71, 16))
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(880, 0, 93, 28))
        self.pushButton_2.setObjectName("Save")
        self.pushButton_2.clicked.connect(self.Handle_Save)
        self.pushButton_3 = QtWidgets.QPushButton(self)
        self.pushButton_3.setGeometry(QtCore.QRect(770, 0, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_Zillow = QtWidgets.QPushButton(self)
        self.pushButton_Zillow.setGeometry(QtCore.QRect(500, 700,  300, 80))
        self.pushButton_Zillow.setObjectName("Save")
        self.pushButton_Zillow.clicked.connect(self.searchAdressZillow)
        self.pushButton_Redfin = QtWidgets.QPushButton(self)
        self.pushButton_Redfin.setGeometry(QtCore.QRect(810, 700, 300, 80))
        self.pushButton_Redfin.setObjectName("pushButton_3")

        self.Very_interested.setEnabled(False)
        self.Interested.setEnabled(False)
        self.Not_interested.setEnabled(False)
        self.Respond_person.setEnabled(False)
        self.Button_NOresponse.setEnabled(False)
        self.Button_responded.setEnabled(False)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.label_13.setText(_translate("Form", "Owner Information:"))
        self.label_7.setText(_translate("Form", "House Information:"))
        self.label_11.setText(_translate("Form", "Property Information"))
        self.pushButton.setText(_translate("Form", "Edit Information"))
        item = self.house_info.verticalHeaderItem(0)
        item.setText(_translate("Form", "Adress:"))
        item = self.house_info.verticalHeaderItem(1)
        item.setText(_translate("Form", "City:"))
        item = self.house_info.verticalHeaderItem(2)
        item.setText(_translate("Form", "Zip Code:"))
        item = self.house_info.verticalHeaderItem(3)
        item.setText(_translate("Form", "State:"))
        item = self.house_info.verticalHeaderItem(4)
        item.setText(_translate("Form", "Property Type:"))
        item = self.house_info.verticalHeaderItem(5)
        item.setText(_translate("Form", "Building Size:"))
        item = self.house_info.verticalHeaderItem(6)
        item.setText(_translate("Form", "Lot Size(SqFt):"))
        item = self.house_info.verticalHeaderItem(7)
        item.setText(_translate("Form", "Baths:"))
        item = self.house_info.verticalHeaderItem(8)
        item.setText(_translate("Form", "Bedrooms:"))
        item = self.house_info.verticalHeaderItem(9)
        item.setText(_translate("Form", "APN:"))
        item = self.house_info.verticalHeaderItem(10)
        item.setText(_translate("Form", "Year Built:"))
        item = self.house_info.verticalHeaderItem(11)
        item.setText(_translate("Form", "Number of Units:"))
        item = self.house_info.verticalHeaderItem(12)
        item.setText(_translate("Form", "Primary Garage Type:"))
        item = self.house_info.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Information", "Hello"))
        item = self.owner_info.verticalHeaderItem(0)
        item.setText(_translate("Form", "First Name:"))
        item = self.owner_info.verticalHeaderItem(1)
        item.setText(_translate("Form", "Last Name:"))
        item = self.owner_info.verticalHeaderItem(2)
        item.setText(_translate("Form", "Mailing Adress:"))
        item = self.owner_info.verticalHeaderItem(3)
        item.setText(_translate("Form", "Mailing City:"))
        item = self.owner_info.verticalHeaderItem(4)
        item.setText(_translate("Form", "Mailing Zip Code:"))
        item = self.owner_info.verticalHeaderItem(5)
        item.setText(_translate("Form", "Mailing State:"))
        item = self.owner_info.verticalHeaderItem(6)
        item.setText(_translate("Form", "Loan to Value Ratio:"))
        item = self.owner_info.verticalHeaderItem(7)
        item.setText(_translate("Form", "Total Outstanding Loans:"))
        item = self.owner_info.verticalHeaderItem(8)
        item.setText(_translate("Form", "Amount of Delinquent Taxes:"))
        item = self.owner_info.verticalHeaderItem(9)
        item.setText(_translate("Form", "Owner Occuppied:"))
        item = self.owner_info.verticalHeaderItem(10)
        item.setText(_translate("Form", "Purchased Prise:"))
        item = self.owner_info.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Information"))
        __sortingEnabled = self.owner_info.isSortingEnabled()
        self.owner_info.setSortingEnabled(True)
        self.owner_info.setSortingEnabled(__sortingEnabled)
        self.label_8.setText(_translate("Form", "Additional Comments:"))
        self.label_9.setText(_translate("Form", "Status:"))
        self.Button_NOresponse.setText(_translate("Form", "Hasn\'t Responded "))
        self.Respond_person.setText(_translate("Form", "Respomd Personally"))
        self.Button_responded.setText(_translate("Form", "Responded"))
        self.Very_interested.setText(_translate("Form", "Very Interested"))
        self.Interested.setText(_translate("Form", "Interested "))
        self.Not_interested.setText(_translate("Form", "Not Interested"))
        self.label.setText(_translate("Form", "Status: "))
        self.label_2.setText(_translate("Form", "Interested:"))
        self.pushButton_2.setText(_translate("Form", "Save Edit"))
        self.pushButton_3.setText(_translate("Form", "PushButton"))
        self.pushButton_Zillow.setText(_translate("Form", "Search Property In Zillow"))
        self.pushButton_Redfin.setText(_translate("Form", "Search Property In Red Fin"))
        self.filltable(self.header, self.information)

    def filltable(self, headers, info):
        #Parameters: header, information, nameOfList
        #Selected_info = self.sl.table_item_clicked().selectedRow
        #Table_Headers = self.sl.table_item_clicked().columHeaders

        count =0
        self.header = headers
        self.information = info

        while count != self.house_info.rowCount()-1:
            count2 = len(headers)
            for x in range(0, count2):

                if headers[x] == self.house_info.verticalHeaderItem(count).text():
                   item = QtWidgets.QTableWidgetItem(info[x])
                   print(x)
                   if self.CheckEdit:
                       item.setFlags(QtCore.Qt.ItemIsEditable)

                   self.house_info.setItem(count,0, item)
                   count=count+1
<<<<<<< HEAD:UI_ProfilePage.py
                   print("table")
                   print(count)

=======

                
>>>>>>> a51b5d2b03ada0ade0214a4949b61813cec27daa:ui_ProfilePage.py
                   break

                elif headers[x]=="Interested":

                    if info[x] == "0":
                        self.Very_interested.setChecked(True)
                    elif info[x] == "1":
                        self.Interested.setChecked(True)
                    elif info[x] == "2":
                        self.Not_interested.setChecked(True)
                    count =count+1

                elif headers[x] == "Status":

                    if info[x] == "0":
                        self.Respond_person.setChecked(True)
                    elif info[x] == "1":
                        self.Button_NOresponse.setChecked(True)
                    elif info[x] == "2":
                        self.Button_responded.setChecked(True)
                    count =count+1

                elif headers[x]== self.AdditionalInfo_txt.toPlainText():
                    self.AdditionalInfo_txt.setPlainText(info[x])
                #elif x+1 == count2:
                 #   count = count+1
                  #  print("lastif")
                   # print(count)
                    #break







            '''
            count=count+1

            item= QtWidgets.QTableWidgetItem()
            item.setText("You did it")
            self.house_info.setItem(count,0, item)
            count=count+1
            '''
        count =0
        while count != self.owner_info.rowCount()-1:
            count2 = len(headers)
            for x in range(0, count2):
                if headers[x] == self.owner_info.verticalHeaderItem(count).text():
                   item = QtWidgets.QTableWidgetItem(info[x])

                   if self.CheckEdit:
                    item.setFlags(QtCore.Qt.ItemIsEditable)

                   self.owner_info.setItem(count,0, item)
                   count=count+1
                   break
                elif x+1 == count2:
                    count = count+1
                    break
            '''
            item= QtWidgets.QTableWidgetItem()
            item.setText("You did it")
            self.owner_info.setItem(count,0,item)
            count=count+1
            '''



    def Handle_edit (self):
        self.CheckEdit = False
        print("hello")
        self.filltable(self.header, self.information)
        #for x in range(0, )
        self.Very_interested.setEnabled(True)
        self.Interested.setEnabled(True)
        self.Not_interested.setEnabled(True)
        self.Respond_person.setEnabled(True)
        self.Button_NOresponse.setEnabled(True)
        self.Button_responded.setEnabled(True)
        self.AdditionalInfo_txt.setReadOnly(False)


    def Handle_Save (self):
        self.CheckEdit = True
        print("hello")

        count =0
        while count != self.house_info.rowCount()-1:
            print("this worked lol22222")
            print(count)
            count2 = len(self.header)
            for x in range(0, count2):
                print("this is count")
                print(count)
                print(x)
                print("this worked lol11111111")
                if self.header[x] == self.house_info.verticalHeaderItem(count).text():
                   self.information[x] = self.house_info.item(count,0).text()
                   count=count+1
                   print("this worked lol333333")
                   break
                
               

                elif headers[x]=="Interested":
                    if self.Very_interested.isChecked:
                        info[x] = "0"
                        count =count+1
                        print("this worked lol11111911")
                        break
                    elif self.Interested.isChecked:
                        info[x] = "1"
                        count =count+1
                        break                        
                    elif self.Not_interested.sisChecked:
                        info[x] = "2"
                        count =count+1
                        break


                elif headers[x] == "Status":
                    print("this worked lol444444444")
                    if self.Respond_person.isChecked:
                        print("this worked lol")
                        info[x] = "0"
                        count =count+1
                                   
                    elif self.Button_NOresponse.isChecked:
                        info[x] = "1"    
                        count =count+1
                                           
                    elif self.Button_responded.isChecked:
                        info[x] = "2"
                        count =count+1
                                            
                elif True:
                    print("this worked lol11111181")

                #elif headers[x]== self.AdditionalInfo_txt.():
                 #   self.AdditionalInfo_txt.setPlainText(info[x])
                  #  count = count+1
                #elif x+1 == count2:
                 #   print("this worked lol5555555")
                  #  count = count+1
                   # break               
                
               
               

        count =0
        while count != self.owner_info.rowCount():
            count2 = len(self.header)
            for x in range(0, count2):
                if self.header[x] == self.owner_info.verticalHeaderItem(count).text():
                   self.information[x] = self.owner_info.item(count,0).text()
                   count=count+1
                   break
                elif x+1 == count2:
                    count = count+1
                    break
            
        self.Very_interested.setEnabled(False)
        self.Interested.setEnabled(False)
        self.Not_interested.setEnabled(False)
        self.Respond_person.setEnabled(False)
        self.Button_NOresponse.setEnabled(False)
        self.Button_responded.setEnabled(False)
        self.AdditionalInfo_txt.setReadOnly(True)
        self.filltable(self.header, self.information)

        '''
        here the method would call the data base to save any changes.
        '''

    def searchAdressZillow (self):
        Adress="/"
        count = len(self.header)
        for x in range(0, count):
            if self.header[x] == "Adress:":
                HoldD = self.information[x].split(" ")
                print(HoldD)
                for y in range(0, len(HoldD)):
                    if y==len(HoldD)-1:
                        Adress=Adress+HoldD[y]
                    else:
                        Adress=Adress+HoldD[y]+"-"
                print(Adress)
        for x in range(0, count):
            if self.header[x] == "City:":
                Adress = Adress+",-"+self.information[x]
        for x in range(0, count):
            if self.header[x] == "Zip Code:":
                Adress = Adress+"-"+self.information[x]
        for x in range(0, count):
            if self.header[x] == "State:":
                Adress = Adress+"-"+self.information[x]
            print('lol')


        print(Adress)
        Adress = "https://www.zillow.com/homes/for_sale"+Adress+"_rb/"
        print(Adress)
        url = Adress
        print(url)
        # for MacOS
        #chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

        # Linux
        # chrome_path = '/usr/bin/google-chrome %s'

        # for Windows
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)
    #def searchAdressOtherPage(self):
        #fjf

if __name__ == '__main__':                      #
    import sys

    app = QApplication(sys.argv)
    window = UI_ProfilePage()
    window.show()
    sys.exit(app.exec_())
