# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Search_For_Leads_Page.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1650, 950)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(1125, 0, 75, 30))
        self.pushButton_4.setObjectName("pushButton_4")
        self.buttonFrame = QtWidgets.QFrame(self.centralwidget)
        self.buttonFrame.setGeometry(QtCore.QRect(1100, 300, 301, 501))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(11, 202, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(11, 202, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(11, 202, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(11, 202, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.buttonFrame.setPalette(palette)
        self.buttonFrame.setAutoFillBackground(True)
        self.buttonFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.buttonFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.buttonFrame.setObjectName("buttonFrame")
        self.refreshButton = QtWidgets.QPushButton(self.buttonFrame)
        self.refreshButton.setGeometry(QtCore.QRect(40, 30, 221, 41))
        self.refreshButton.setObjectName("refreshButton")
        self.functionButton2 = QtWidgets.QPushButton(self.buttonFrame)
        self.functionButton2.setGeometry(QtCore.QRect(40, 130, 221, 41))
        self.functionButton2.setObjectName("functionButton2")
        self.functionButton3 = QtWidgets.QPushButton(self.buttonFrame)
        self.functionButton3.setGeometry(QtCore.QRect(40, 330, 221, 41))
        self.functionButton3.setObjectName("functionButton3")
        self.functionButton4 = QtWidgets.QPushButton(self.buttonFrame)
        self.functionButton4.setGeometry(QtCore.QRect(40, 230, 221, 41))
        self.functionButton4.setObjectName("functionButton4")
        self.functionButton5 = QtWidgets.QPushButton(self.buttonFrame)
        self.functionButton5.setGeometry(QtCore.QRect(40, 430, 221, 41))
        self.functionButton5.setFlat(False)
        self.functionButton5.setObjectName("functionButton5")
        self.radioButton_4 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_4.setGeometry(QtCore.QRect(850, 50, 100, 20))
        self.radioButton_4.setObjectName("radioButton_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1225, 95, 100, 25))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.dataArray1 = QtWidgets.QTableWidget(self.centralwidget)
        self.dataArray1.setGeometry(QtCore.QRect(250, 300, 751, 501))
        self.dataArray1.setProperty("dataArrayString", "")
        self.dataArray1.setObjectName("dataArray1")
        self.dataArray1.setColumnCount(1)
        self.dataArray1.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.dataArray1.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataArray1.setHorizontalHeaderItem(0, item)
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(850, 140, 100, 20))
        self.radioButton_2.setObjectName("radioButton_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(1200, 0, 75, 30))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(1200, 0, 75, 30))
        self.pushButton_7.setObjectName("pushButton_7")
        self.radioButton_12 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_12.setGeometry(QtCore.QRect(1100, 80, 100, 20))
        self.radioButton_12.setObjectName("radioButton_12")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(850, 110, 100, 20))
        self.radioButton.setObjectName("radioButton")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(475, 160, 100, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(1050, 0, 75, 30))
        self.pushButton_6.setObjectName("pushButton_6")
        self.radioButton_6 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_6.setGeometry(QtCore.QRect(975, 50, 100, 20))
        self.radioButton_6.setObjectName("radioButton_6")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(1125, 0, 75, 30))
        self.pushButton_8.setObjectName("pushButton_8")
        self.radioButton_8 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_8.setGeometry(QtCore.QRect(975, 80, 100, 20))
        self.radioButton_8.setObjectName("radioButton_8")
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(850, 80, 100, 20))
        self.radioButton_3.setObjectName("radioButton_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 1650, 30))
        self.label_2.setAutoFillBackground(True)
        self.label_2.setObjectName("label_2")
        self.radioButton_9 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_9.setGeometry(QtCore.QRect(1100, 110, 100, 20))
        self.radioButton_9.setObjectName("radioButton_9")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(1100, 260, 301, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(9, 240, 24))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(9, 240, 24))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(9, 240, 24))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(9, 240, 24))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(27)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAutoFillBackground(True)
        self.label.setObjectName("label")
        self.radioButton_5 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_5.setGeometry(QtCore.QRect(975, 110, 100, 20))
        self.radioButton_5.setObjectName("radioButton_5")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(1050, 0, 75, 30))
        self.pushButton_3.setObjectName("pushButton_3")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(245, 160, 200, 25))
        self.comboBox.setEditable(True)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.radioButton_11 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_11.setGeometry(QtCore.QRect(1100, 140, 100, 20))
        self.radioButton_11.setObjectName("radioButton_11")
        self.radioButton_10 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_10.setGeometry(QtCore.QRect(1100, 50, 100, 20))
        self.radioButton_10.setObjectName("radioButton_10")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(250, 260, 751, 541))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.scrollArea = QtWidgets.QScrollArea(self.tab)
        self.scrollArea.setGeometry(QtCore.QRect(50, 70, 751, 491))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 749, 489))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.radioButton_7 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_7.setGeometry(QtCore.QRect(975, 140, 100, 20))
        self.radioButton_7.setObjectName("radioButton_7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1650, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_4.setText(_translate("MainWindow", "Logout"))
        self.refreshButton.setText(_translate("MainWindow", "Function 1"))
        self.functionButton2.setText(_translate("MainWindow", "Function 2"))
        self.functionButton3.setText(_translate("MainWindow", "Function 4"))
        self.functionButton4.setText(_translate("MainWindow", "Function 3"))
        self.functionButton5.setText(_translate("MainWindow", "Function 5"))
        self.radioButton_4.setText(_translate("MainWindow", "RadioButton"))
        self.pushButton_2.setText(_translate("MainWindow", "Advanced Search"))
        item = self.dataArray1.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.dataArray1.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Column"))
        self.radioButton_2.setText(_translate("MainWindow", "RadioButton"))
        self.pushButton_5.setText(_translate("MainWindow", "Search"))
        self.pushButton_7.setText(_translate("MainWindow", "Search"))
        self.radioButton_12.setText(_translate("MainWindow", "RadioButton"))
        self.radioButton.setText(_translate("MainWindow", "RadioButton"))
        self.pushButton.setText(_translate("MainWindow", "Search"))
        self.pushButton_6.setText(_translate("MainWindow", "Home"))
        self.radioButton_6.setText(_translate("MainWindow", "RadioButton"))
        self.pushButton_8.setText(_translate("MainWindow", "Logout"))
        self.radioButton_8.setText(_translate("MainWindow", "RadioButton"))
        self.radioButton_3.setText(_translate("MainWindow", "RadioButton"))
        self.label_2.setText(_translate("MainWindow", "Chicago Turnkey Properties"))
        self.radioButton_9.setText(_translate("MainWindow", "RadioButton"))
        self.label.setText(_translate("MainWindow", " OTHER FUNCTIONS"))
        self.radioButton_5.setText(_translate("MainWindow", "RadioButton"))
        self.pushButton_3.setText(_translate("MainWindow", "Home"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Divorce"))
        self.comboBox.setItemText(1, _translate("MainWindow", "New Item"))
        self.comboBox.setItemText(2, _translate("MainWindow", "New Item"))
        self.comboBox.setItemText(3, _translate("MainWindow", "New Item"))
        self.radioButton_11.setText(_translate("MainWindow", "RadioButton"))
        self.radioButton_10.setText(_translate("MainWindow", "RadioButton"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.radioButton_7.setText(_translate("MainWindow", "RadioButton"))


