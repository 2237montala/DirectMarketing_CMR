from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from ShowList import Ui_MainWindow
from UI_LogIn_Page import Ui_LogIn_Page
from PyQt5.Qt import QDesktopWidget

class gui(QtWidgets.QMainWindow):
    def __init__(self,width,height,db_file_loc):
        super().__init__()
        self.setObjectName("Direct Marketing CMR")
        self.setWindowTitle("Direct Marketing CMR")
        self.resize(width , height + 50)
        #self.main_window = Ui_MainWindow(db_file_loc)
        #self.main_window.setup_main_widget(width,height)

        self.main_window = Ui_LogIn_Page(db_file_loc)

        self.setCentralWidget(self.main_window)

        #self.menuBar = self.main_window.setup_menu_bar()
        #self.setMenuBar(self.menuBar)

        #self.main_window.show()
        self.main_window.pushButton_LogIn.clicked.connect(self.switchMainWidget)

    def switchMainWidget(self):
        print('hellow')
if __name__ == "__main__":
    data_base_file = 'test.db'

    app = QtWidgets.QApplication(sys.argv)
    gui = gui(1600,900,data_base_file)
    gui.show()
    sys.exit(app.exec_())
