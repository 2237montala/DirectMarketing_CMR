# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Property_Profile.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets
from distutils.log import info
from PyQt5.Qt import QWidget, QApplication, QAbstractItemView, QTableWidgetItem
from _sqlite3 import Row
from sys import platform

import webbrowser
#from ShowList import ShowList

class UI_ProfilePage(QtWidgets.QDialog):

    CheckEdit = True

    def __init__(self):
        super().__init__()
        self.setupUi()
        self.show()

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
        self.owner_info.setRowCount(12)
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
        self.owner_info.setVerticalHeaderItem(11, item)
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
        self.pushButton_Redfin.clicked.connect(self.searchAdressHomesnap)

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
        item.setText(_translate("Form", "Site_Address"))
        item = self.house_info.verticalHeaderItem(1)
        item.setText(_translate("Form", "Site_City"))
        item = self.house_info.verticalHeaderItem(2)
        item.setText(_translate("Form", "Site_Zip_Code"))
        item = self.house_info.verticalHeaderItem(3)
        item.setText(_translate("Form", "Site_State"))
        item = self.house_info.verticalHeaderItem(4)
        item.setText(_translate("Form", "Property_Type"))
        item = self.house_info.verticalHeaderItem(5)
        item.setText(_translate("Form", "Building_Size"))
        item = self.house_info.verticalHeaderItem(6)
        item.setText(_translate("Form", "Lot_Size_(SqFt)"))
        item = self.house_info.verticalHeaderItem(7)
        item.setText(_translate("Form", "Baths"))
        item = self.house_info.verticalHeaderItem(8)
        item.setText(_translate("Form", "Bedrooms"))
        item = self.house_info.verticalHeaderItem(9)
        item.setText(_translate("Form", "APN_/_Parcel_Number"))
        item = self.house_info.verticalHeaderItem(10)
        item.setText(_translate("Form", "Year_Built"))
        item = self.house_info.verticalHeaderItem(11)
        item.setText(_translate("Form", "Number_of_Units"))
        item = self.house_info.verticalHeaderItem(12)
        item.setText(_translate("Form", "Primary_Garage_Type"))
        item = self.house_info.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Information", "Hello"))
        item = self.owner_info.verticalHeaderItem(0)
        item.setText(_translate("Form", "1st_Owner's_First_Name"))
        item = self.owner_info.verticalHeaderItem(1)
        item.setText(_translate("Form", "1st_Owner's_Last_Name"))
        item = self.owner_info.verticalHeaderItem(2)
        item.setText(_translate("Form", "Mail_Address"))
        item = self.owner_info.verticalHeaderItem(3)
        item.setText(_translate("Form", "Mailing_City"))
        item = self.owner_info.verticalHeaderItem(4)
        item.setText(_translate("Form", "Mailing_Zip_Code"))
        item = self.owner_info.verticalHeaderItem(5)
        item.setText(_translate("Form", "Mailing_State"))
        item = self.owner_info.verticalHeaderItem(6)
        item.setText(_translate("Form", "Loan_To_Value_Ratio"))
        item = self.owner_info.verticalHeaderItem(7)
        item.setText(_translate("Form", "Total_Outstanding_Loans"))
        item = self.owner_info.verticalHeaderItem(8)
        item.setText(_translate("Form", "Amount_of_Delinquent_Taxes"))
        item = self.owner_info.verticalHeaderItem(9)
        item.setText(_translate("Form", "Owner_Occupied"))
        item = self.owner_info.verticalHeaderItem(10)
        item.setText(_translate("Form", "Purchased_Prise"))
        item = self.owner_info.verticalHeaderItem(11)
        item.setText(_translate("Form", "Phone_Number"))
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
        

    def filltable(self, info, headers):
        #Parameters: header, information, nameOfList
        #Selected_info = self.sl.table_item_clicked().selectedRow
        #Table_Headers = self.sl.table_item_clicked().columHeaders
        
        
        
        
        print("llllllllllllllllllllllllllllll")
        
        
        
        self.header = headers
        self.information=info
        count =0
        while count != self.house_info.rowCount()-1:
            count2 = len(self.header)
            for x in range(0, count2):

                if headers[x] == self.house_info.verticalHeaderItem(count).text():
                   item = QtWidgets.QTableWidgetItem(str(info[x]))
                   
                   
                   if self.CheckEdit:
                       item.setFlags(QtCore.Qt.ItemIsEditable)

                   self.house_info.setItem(count,0, item)
                   count=count+1
                   break

                elif self.header[x]=="Interested":
                    if self.information[x] == "0":
                        self.Very_interested.setChecked(True)
                    elif self.information[x] == "1":
                        self.Interested.setChecked(True)
                    elif self.information[x] == "2":
                        self.Not_interested.setChecked(True)
                    count=count+1

                elif self.header[x] == "Status":

                    if self.information[x] == "0":
                        self.Respond_person.setChecked(True)
                    elif self.information[x] == "1":
                        self.Button_NOresponse.setChecked(True)
                    elif self.information[x] == "2":
                        self.Button_responded.setChecked(True)
                    count =count+1


                elif headers[x]== self.label_8.text():
                    self.AdditionalInfo_txt.setPlainText(info[x])
                    count += 1
                elif x+1 == count2:
                   count = count+1
                   break


            '''
            count=count+1

            item= QtWidgets.QTableWidgetItem()
            item.setText("You did it")
            self.house_info.setItem(count,0, item)
            count=count+1
            '''
        count =0
        while count != self.owner_info.rowCount()-1:
            count2 = len(self.header)
            for x in range(0, count2):
                if self.header[x] == self.owner_info.verticalHeaderItem(count).text():
                   item = QtWidgets.QTableWidgetItem(self.information[x])

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
        for x in range(0,3):
            self.CheckEdit = False
            self.update()
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

        count =0
        while count != self.house_info.rowCount()-1:
            count2 = len(self.header)
            for x in range(0, count2):
                print(self.house_info.verticalHeaderItem(count).text())
                if self.header[x] == self.house_info.verticalHeaderItem(count).text():

                   self.information[x] = self.house_info.item(count,0).text()

                   print(self.information[x])
                   count=count+1
                   break


                elif self.header[x]=="Interested":
                    if self.Very_interested.isChecked:
                        info[x] = "0"

                        count =count+1

                    elif self.Interested.isChecked():
                        self.information[x] = "1"
                        count =count+1


                    elif self.Not_interested.sisChecked():
                        self.information[x] = "2"
                        count =count+1

                    elif self.Not_interested.sisChecked:
                        info[x] = "2"

                        count =count+1
                    break


                elif self.header[x] == "Status":
                    if self.Respond_person.isChecked():
                        self.information[x] = "0"
                        count =count+1


                    elif self.Button_NOresponse.isChecked():
                        self.information[x] = "1"
                        count =count+1

                    elif self.Button_responded.isChecked():
                        self.information[x] = "2"
                        count =count+1
                    break



                elif self.header[x]== self.label_8.text():
                    self.information[x]=self.AdditionalInfo_txt.toPlainText().txt()
                    count = count+1

                elif x+1 == count2:
                    count = count+1
                    break

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
    def searchOS (self):
        """
        This method uses the python platform package to identify what type of
        operating system the user is using.
        """
        print('this is after search')
        from sys import platform
        if platform == "linux" or platform == "linux2":
            a =1
        elif platform == "Darwin" or platform == "darwin":
            a =2
        elif platform == "win32":
            a = 3
        else:
            a = -1
        return a

    def searchAdressZillow (self):
        """
        Looks up the property on zillow.com. It takes the street address, zip,
        and county and forms a url for zillow and opens the web page
        """
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


        print(Adress)
        Adress = "https://www.zillow.com/homes/for_sale"+Adress+"_rb/"
        print(Adress)
        url = Adress
        print(url)
        system = self.searchOS()
        webbrowser.open(url, new=1, autoraise=True)
        
    def searchAdressHomesnap (self):
        """
        
        Looks up the property on zillow.com. It takes the street address, zip, 
        and county and forms a url for zillow and opens the web page
        """
        print('start')
        Adress="/"
        count = len(self.header)
        for x in range(0, count):
            if self.header[x] == "State:":
                print(self.information[x])
                info=self.information[x]
                info= info.replace("Alabama", "AL")
                info= info.replace("Illinois", "IL")
                info = info.replace("Montana", "MT")
                info = info.replace("Alaska", "AK")
                info = info.replace("Nebraska", "NE")
                info = info.replace("Arizona", "AZ")
                info = info.replace("Nevada", "NV")
                info = info.replace("Arkansas", "AR")
                info = info.replace("New Hampshire", "NH")
                info = info.replace("California", "CA")
                info = info.replace("New Jersey", "NJ")
                info = info.replace("Colorado", "CO")
                info = info.replace("New Mexico", "NM")
                info = info.replace("Connecticut", "CT")
                info = info.replace("New York", "NY")
                info = info.replace("Delaware", "DE")
                info = info.replace("North Carolina", "NC")
                info = info.replace("Florida", "FL")
                info = info.replace("North Dakota", "ND")
                info = info.replace("Georgia", "GA")
                info = info.replace("Ohio", "OH")
                info = info.replace("Hawaii", "HI")
                info = info.replace("Oklahoma", "OK")
                info = info.replace("Idaho", "ID")
                info = info.replace("Oregon", "OR")
                info = info.replace("Pennsylvania", "PA")
                info = info.replace("Indiana", "IN")
                info = info.replace("Rhode Island", "RI")
                info = info.replace("Iowa", "IA")
                info = info.replace("South Carolina", "SC")
                info = info.replace("Kansas", "KS")
                info = info.replace("South Dakota", "SD")
                info = info.replace("Kentucky", "KY")
                info = info.replace("Tennesse", "TN")
                info = info.replace("Louisiana", "LA")
                info = info.replace("Texas", "TX")
                info = info.replace("Maine", "ME")
                info = info.replace("Utah", "UT")
                info = info.replace("Maryland", "MD")
                info = info.replace("Vermont", "VT")
                info = info.replace("Massachusetts", "MA")
                info = info.replace("Wyoming", "WY")
                info = info.replace("Missouri", "MO")
                info = info.replace("Wisconsin", "WI")
                info = info.replace("Mississippi", "MS")
                info = info.replace("Washington", "WA")
                info = info.replace("Michigan", "MI")
                info = info.replace("Virginia", "VA")
                Adress = Adress+ info
        for x in range(0, count):
            if self.header[x] == "City:":
                Adress = Adress+"/"+self.information[x]+"/"
        
        for x in range(0, count):
            if self.header[x] == "Adress:":
                HoldD = self.information[x].split(" ")
                print('hold d')
                print(HoldD)
                for y in range(0, len(HoldD)):
                    if y==len(HoldD)-1:
                        Adress=Adress+HoldD[y]
                    else:
                        Adress=Adress+HoldD[y]+"-"
                print(Adress)
                find_street_type = Adress.split('-')
                print(find_street_type[2])
                find_street_type[2] = find_street_type[2].replace("Ave","Avenue")
                find_street_type[2] = find_street_type[2].replace('ALy', "Alley") 
                find_street_type[2] = find_street_type[2].replace("BCH","Beach")
                find_street_type[2] = find_street_type[2].replace("BLVD", "Boulevard")
                find_street_type[2] = find_street_type[2].replace("CT", "Court")
                find_street_type[2] = find_street_type[2].replace("DR","Drive")
                find_street_type[2] = find_street_type[2].replace("FLD","Field")
                find_street_type[2] = find_street_type[2].replace("FLS","Falls")
                find_street_type[2] = find_street_type[2].replace("HL","Hills")
                print(find_street_type[2])
                s = "-"
                s = s.join(find_street_type)  
                Adress = s
                print("cl")
                print("kkdkdkdkd")
                               
             
             
        print(Adress)
        Adress = "https://www.homesnap.com"+Adress
        print(Adress)
        url = Adress
        print(url)
        system = self.searchOS()
        webbrowser.open(url, new=1, autoraise=True)

if __name__ == '__main__':                      #
    
    import sys

    app = QApplication(sys.argv)

    header = ["Site_Address", "Site_City", "Zip Code", "State","Status","Comments of Property"]
    information = ["517 Madison Ave", "Glencoe", "60022","Illinois","0","comments"]
    window = UI_ProfilePage()
    window.filltable(information,header)
    window.show()
    sys.exit(app.exec_())
