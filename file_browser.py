from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog

class file_browser(QWidget):
    def __init__(self,window_title):
        super().__init__()
        self.title = window_title
        self.setWindowTitle(self.title)

        #Opens 1 file


        #Opens multiple files
        #self.openFileNamesDialog()

        #Saves 1 file
        #self.saveFileDialog()


    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getget_tableOpenFileName()", "","All Files (*);;CSV Files (*.csv)", options=options)
        if file_name:
            print(file_name)
            return file_name

    def openFileNamesDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(self,"QFileDialog.getOpenFileNames()", "","All Files (*);;Python Files (*.py)", options=options)
        if files:
            print(files)

    def saveFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","All Files (*);;Text Files (*.txt)", options=options)
        if fileName:
            print(fileName)

    def open_window(self):
        return self.openFileNameDialog()

if __name__ == '__main__':
    app = QApplication([])
    ex = file_browser()
    app.exec_()
