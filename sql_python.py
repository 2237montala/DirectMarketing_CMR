# https://sebastianraschka.com/Articles/2014_sqlite_in_python_tutorial.html
# https://www.dataquest.io/blog/python-pandas-databases/
# https://www.youtube.com/watch?v=pd-0G0MigUA
#https://stackoverflow.com/questions/17044259/python-how-to-check-if-table-exists
from DatabaseManager import DatabaseManager
from Ingestor import Ingestor

# SETTING IT EQUAL TO ':memory:' WILL HAVE IT RUN ON RAM AND NO SQLITE FILE WILL BE MADE.
sqlite_file = 'test.db'
db = DatabaseManager(sqlite_file)

filename = 
ingestor = Ingestor(filename)
ingestor.readCSV()

tempHeaders = ingestor.getCSVHeaders()
searchCritera = ["1st Owner's First Name","1st Owner's Last Name"]

dict = ingestor.getHeaderIndex(ingestor.listToDict(searchCritera,-1),tempHeaders)
print("\nDictionary of search critera and their indexes in the csv")
print(dict)

ingestor.searchRows(dict,ingestor.getRows())
print("\nPrint filtered list from unfiltered row")
print(ingestor.getRowAt(1))

new_table = 'Divorse'
headers = ["First_Name","Last_Name"]
db.create_table(new_table, headers[0],'string')
db.add_column(new_table, headers[1], 'string')
#db.add_row(new_table, "First_Name", "Steve")
#for person in ingestor.getRows():
#    db.add_row(new_table, headers, person)
#db.add_row(new_table, headers, ["Steve","Smith"])

print(db.return_table(new_table))

print(db.print_table(new_table))

#db.clear_table(new_table)
