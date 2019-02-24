# https://sebastianraschka.com/Articles/2014_sqlite_in_python_tutorial.html
    # https://www.dataquest.io/blog/python-pandas-databases/
# https://www.youtube.com/watch?v=pd-0G0MigUA
#https://stackoverflow.com/questions/17044259/python-how-to-check-if-table-exists
from DatabaseManager import DatabaseManager
from Ingestor import Ingestor

# SETTING IT EQUAL TO ':memory:' WILL HAVE IT RUN ON RAM AND NO SQLITE FILE WILL BE MADE.
sqlite_file = 'test.db'
db = DatabaseManager(sqlite_file)

filename = '/home/anthonym/Documents/SchoolWork/SoftwareEngineering/The_lists/Probate 08.19.18.csv'
ingestor = Ingestor(filename)
ingestor.readCSV()

tempHeaders = ingestor.getCSVHeaders()
searchCritera = [tempHeaders[2],tempHeaders[3],tempHeaders[5],tempHeaders[15],tempHeaders[16]]

#searchCritera = [tempHeaders[3],tempHeaders[5],tempHeaders[15],tempHeaders[16]]

searchCriteraTwoD = ingestor.getHeaderIndex(searchCritera,tempHeaders)
print("\nDictionary of search critera and their indexes in the csv")
print(searchCriteraTwoD)

ingestor.searchRows(searchCriteraTwoD,ingestor.getRows())
print("\nPrint filtered list from unfiltered row")
print(ingestor.getRowAt(0))

for i in range(0,len(searchCriteraTwoD)):
    pass
    #searchCriteraTwoD[i][0] = searchCriteraTwoD[i][0].replace(' ','_')
    #searchCriteraTwoD[i][0] = searchCriteraTwoD[i][0].replace("'",'"')

print(searchCriteraTwoD)

new_table = 'Probate'
db.create_table(new_table, searchCritera,'string')

for i in range(1,len(searchCritera)):
    db.add_column(new_table,searchCritera,'string')

#db.add_column(new_table, headers[1], 'string')
#db.add_row(new_table, ['Site_Address'], ["Steve"])
#print(ingestor.getRows())
db.add_row(new_table,searchCritera,ingestor.getRowAt(0))

#for person in ingestor.getRows():
    #print(person)
    #db.add_row(new_table, searchCritera, person)
#db.add_row(new_table, headers, ["Steve","Smith"])

print(db.return_table(new_table))

#print(db.print_table(new_table))

db.clear_table(new_table)
