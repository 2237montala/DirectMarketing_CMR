'''
Created on Mar 27, 2019

@author: Alberto Fernandez
'''
import Accounts_DataBase

class MyClass(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        Accounts_DataBase.Create_Table("Accounts","Username","string")
        
        