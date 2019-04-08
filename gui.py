from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class gui(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()


    def setupUi(self,width,height):
        self.resize(width , height+50)


    def run(self):
        app = QtWidgets.QApplication(sys.argv)
        self.setupUi(width,height)
        self.show()
        sys.exit(app.exec_())




if __name__ == "__main__":
    data_base_file = 'test.db'
    app = gui()
    app.run(1600,900)
