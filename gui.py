from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from ShowList import Ui_MainWindow
from UI_LogIn_Page import Ui_LogIn_Page
from PyQt5.Qt import QDesktopWidget

protected_table_prefix = "__ADMIN__"

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
        self.main_window.valid_login_signal.connect(self.switchMainWidget)

    def switchMainWidget(self):
        ## Setting the main widget to be the ShowList gui
        self.main_window = Ui_MainWindow(self.data_base_file,protected_table_prefix)
        self.main_window.setup_main_widget(self.width,self.height)
        self.main_window.log_out_signal.connect(self.log_out)

        self.setMenuBar(self.main_window.setup_menu_bar())
        self.setCentralWidget(self.main_window)
        
    def log_out(self):
        ## Setting the login page to be the main window
        self.main_window = Ui_LogIn_Page(self.data_base_file, protected_table_prefix)
        self.main_window.valid_login_signal.connect(self.switchMainWidget)
        self.setCentralWidget(self.main_window)
        
if __name__ == "__main__":
    data_base_file = 'test.db'

    app = QtWidgets.QApplication(sys.argv)
    gui = gui(1600,900,data_base_file)
    gui.show()
    sys.exit(app.exec_())
