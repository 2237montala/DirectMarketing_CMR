from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from ShowList import Ui_MainWindow
from UI_LogIn_Page import Ui_LogIn_Page
from PyQt5.Qt import QDesktopWidget
from UI_After_LogIn_Page import Ui_CalendarForm

protected_table_prefix = "__ADMIN__"

#TO make this an .exe run pyinstall gui.py
#you need to install pyInstall


class gui(QtWidgets.QMainWindow):
    def __init__(self,width,height,db_file_loc):
        super().__init__()
        self.data_base_file = db_file_loc
        self.height = height
        self.width = width
        self.setObjectName("Direct Marketing CMR")
        self.setWindowTitle("Direct Marketing CMR")
        self.resize(width , height + 50)
        ## Setting initial main window to be the login page
        self.main_window = Ui_LogIn_Page(self.data_base_file, protected_table_prefix)
        self.setCentralWidget(self.main_window)
        self.main_window.valid_login_signal.connect(self.switchCalendar)

    def switchMainWidget(self):
        ## Setting the main widget to be the ShowList gui
        self.main_window = Ui_MainWindow(self.data_base_file,protected_table_prefix)
        self.main_window.setup_main_widget(self.width,self.height)
        self.main_window.log_out_signal.connect(self.switchLogIn)
        self.main_window.goto_calendar_signal.connect(self.switchCalendar)
        self.setMenuBar(self.main_window.setup_menu_bar())
        self.setCentralWidget(self.main_window)

    def switchLogIn(self):
        ## Setting the login page to be the main window
        self.main_window = Ui_LogIn_Page(self.data_base_file, protected_table_prefix)
        self.main_window.valid_login_signal.connect(self.switchCalendar)
        self.setMenuBar(QtWidgets.QMenuBar())
        self.setCentralWidget(self.main_window)

    def switchCalendar(self):
        ## Setting the calendar page to main window
        self.main_window = Ui_CalendarForm(self.data_base_file, protected_table_prefix)
        self.main_window.calendar_to_login_signal.connect(self.switchLogIn)
        self.main_window.calendar_to_lists_signal.connect(self.switchMainWidget)
        self.setMenuBar(QtWidgets.QMenuBar())
        self.setCentralWidget(self.main_window)

if __name__ == "__main__":
    data_base_file = 'programData.db'

    app = QtWidgets.QApplication(sys.argv)
    gui = gui(1600,900,data_base_file)
    gui.show()
    sys.exit(app.exec_())
