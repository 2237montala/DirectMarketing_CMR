'''
Created on Apr 1, 2019

@author: Alberto Fernandez
'''
import PyQt5, sys 
from UI_CreateAccount import *
from UI_Login_Page import *

class INITIALIZE:
    def __init__(self):
        app = PyQt5.QtWidgets.QApplication(sys.argv)
        INITIALIZE.massForm = Ui_LogIn_Page()
        INITIALIZE.massForm.show()
        INITIALIZE.compForm = Ui_CreateAccount()
        app.exec_()

def main():
    program = INITIALIZE()

