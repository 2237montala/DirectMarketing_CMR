'''
Created on Feb 18, 2019

@author: Alberto Fernandez
'''

import csv;
from _sqlite3 import Row
from tkinter.tix import COLUMN
from collections import defaultdict
from pip._vendor.msgpack.fallback import TYPE_ARRAY, xrange


class MyClass(object):
    


    def getData(self, filename):
        with open(filename) as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            print(readCSV)
            #print(next(readCSV)[7])
    
            lines = csvfile.readlines()
            print(lines[0])
            print(lines[0].split(','))
    
            listOfCriteria = lines[0].split(',')
    
            WantedCriteria = ['Site Address', 'Site City', 'Site State','Site Zip Code']
    
            NumberC = [];
            count=0
            for x in listOfCriteria:
                if  WantedCriteria.__contains__(x):
                    NumberC.append(count)
                    print(count)
                    print(x)
                count = count+1
            print("its herrrrrreee=")
            print(NumberC[0])
    
            cols = NumberC.__len__()
            rows = lines.__len__()
    
            adresses = [([0]*cols) for row in xrange(rows)]
   
            count1 =0;
            for c in lines:
                #print(lines[0])
                count0 =0;
                #print(count1)
                for y in NumberC:
                    #print(y)
                    adresses[count1][count0]=lines[count1].split(',')[y]
            
                    count0 = 1+count0
            
            
        
                count1 +=1
    
        
       
            
            
            print(adresses)
            return adresses
   
    
    filename="Absenty.csv"
    self = 0
    AU=getData(self, filename)
   
    def __init__(self):
        self.run = self.methods['getData'] 