from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from ShowList import Ui_MainWindow

class gui(QtWidgets.QMainWindow):
    def __init__(self,width,height,db_file_loc):
        super().__init__()
        self.setObjectName("Direct Marketing CMR")
        self.setWindowTitle("Direct Marketing CMR")
        self.resize(width , height+50)

        self.main_window = Ui_MainWindow(db_file_loc)
        self.main_window.setup_main_widget(width,height)
        print(type(self.main_window))
        self.setCentralWidget(self.main_window)

        self.menuBar = self.main_window.setup_menu_bar()
        self.setMenuBar(self.menuBar)

        #self.main_window.show()

if __name__ == "__main__":
    data_base_file = 'test.db'

    app = QtWidgets.QApplication(sys.argv)
    gui = gui(1600,900,data_base_file)
    gui.show()
    sys.exit(app.exec_())
