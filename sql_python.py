# https://sebastianraschka.com/Articles/2014_sqlite_in_python_tutorial.html
    # https://www.dataquest.io/blog/python-pandas-databases/
# https://www.youtube.com/watch?v=pd-0G0MigUA
#https://stackoverflow.com/questions/17044259/python-how-to-check-if-table-exists
from DatabaseManager import DatabaseManager
from Ingestor import Ingestor

# SETTING IT EQUAL TO ':memory:' WILL HAVE IT RUN ON RAM AND NO SQLITE FILE WILL BE MADE.
sqlite_file = 'test.db'
db = DatabaseManager(sqlite_file)

filename = "/home/anthonym/Documents/SchoolWork/SoftwareEngineering/Divorce_list_08.20.18_FIXED.csv"
ingestor = Ingestor(filename)
ingestor.readCSV()

tempHeaders = ingestor.getCSVHeaders()
searchCritera = [tempHeaders[2],tempHeaders[3],tempHeaders[5],tempHeaders[15],tempHeaders[16]]

searchCriteraTwoD = ingestor.getHeaderIndex(searchCritera,tempHeaders)
print("\nDictionary of search critera and their indexes in the csv")
print(searchCriteraTwoD)

ingestor.searchRows(searchCriteraTwoD,ingestor.getRows())
print("\nPrint filtered list from unfiltered row")
print(ingestor.getRowAt(0))

for i in range(0,len(searchCritera)):
    searchCritera[i] = searchCritera[i].replace(' ','_')

new_table = 'Probate'
print('\nCreating a new table using the search critera as headers')
print('\nIf the row already exists it will throw an error and continue')
db.create_table_list(new_table,searchCritera,'string')

print('\nAdding all the rows from the CSV file into new table')
for person in ingestor.getRows():
    db.add_row_list(new_table, searchCritera, person)
    pass

print('\nPrinting all table entries')
print(db.return_table(new_table))
db.clear_table(new_table)
