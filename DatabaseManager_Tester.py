# https://sebastianraschka.com/Articles/2014_sqlite_in_python_tutorial.html
    # https://www.dataquest.io/blog/python-pandas-databases/
# https://www.youtube.com/watch?v=pd-0G0MigUA
#https://stackoverflow.com/questions/17044259/python-how-to-check-if-table-exists
from DatabaseManager import DatabaseManager
from Ingestor import Ingestor

# SETTING IT EQUAL TO ':memory:' WILL HAVE IT RUN ON RAM AND NO SQLITE FILE WILL BE MADE.
sqlite_file = 'test.db'
db = DatabaseManager(sqlite_file)

CLEAR_ON_COMPLETION = False

filename = "DatabaseManagerTest_15.csv"
ingestor = Ingestor(filename)
ingestor.readCSV()

tempHeaders = ingestor.getCSVHeaders()
searchCritera = [tempHeaders[0],tempHeaders[1],tempHeaders[2],tempHeaders[4],tempHeaders[5],tempHeaders[6]]

searchCriteraTwoD = ingestor.getHeaderIndex(searchCritera,tempHeaders)
print("\nDictionary of search critera and their indexes in the csv")
print(searchCriteraTwoD)

ingestor.searchRows(searchCriteraTwoD,ingestor.getRows())
print("\nPrint filtered list from unfiltered row")
print(ingestor.getRowAt(0))

searchCritera = db.remove_spaces(searchCritera)

new_table = 'Test_15'
print('\nCreating a new table using the search critera as headers')
print('If the row already exists it will throw an error and continue')
db.create_table_list(new_table,searchCritera,'string')


print('\nAdding all the rows from the CSV file into new table')
for person in ingestor.getRows():
    db.add_row_list(new_table, searchCritera, person)
# db.add_list_of_rows(new_table,searchCritera,ingestor.getRows())
  
# print('\nPrinting table headers')
# print(db.get_headers(new_table))
#  
# print('\nPrinting all table entries')
# print(db.get_table(new_table))
#  
# print("\nPrinting the names of all tables in the database")
# print(db.get_table_names())
#  
# print("\nGet row with address %s (columns)" % ingestor.getRowAt(2)[0])
# print(db.get_row_at(new_table,column_name=searchCritera[0],column_value=ingestor.getRowAt(2)[0]))
#  
# print("\nGet row with address using column and 1435 North St. Should return nothing")
# print(db.get_row_at(new_table,searchCritera[0],"1435 North St."))
#  
# print("\nGet row with address using column and 88730 Barby Park Should return something")
# print(db.get_row_at(new_table,searchCritera[0],"88730 Barby Park"))

test_row = 9

# rowToBeDel = db.get_row_at(new_table,row_id=test_row)
# print(len(rowToBeDel))
# rowAfterToBeDel = db.get_row_at(new_table,row_id=test_row+1)
# print(len(rowAfterToBeDel))
# 
# print("\nGet row with row id %d" % test_row)
# print(rowToBeDel)
#  
# print("\nGet row with row id %d" % (test_row+1))
# print(rowAfterToBeDel)
#  
# print("\nDelete row with row id %d" % test_row)
# print(db.delete_row_at(new_table,row_id=test_row))
#  
# print('\nIs the new row %d equal to the old row %d' % (test_row,test_row+1))
# print(rowAfterToBeDel == db.get_row_at(new_table,row_id=test_row))

updated_row1 = ["ahouse", "josh", "green", "ssd4fr33@montalbano.com", "228-192-2819", "$2.17"]
updated_row2 = ["notahouse", "Josh", "Anderson", "SCAMUORME@GMAIL>COM", "1-800-CALLMEANTHONY", "$123.456"]
print("\nUpdate row with row id %d" % test_row)
print(db.update_row_at(new_table,primary_key = test_row, new_row = updated_row1))

print("\nUpdate row with given column_name and column_value")
print(db.update_row_at(new_table,searchCritera[0], updated_row1[0], new_row = updated_row2))
db.get_table(new_table)

if CLEAR_ON_COMPLETION:
    print("\nClearing table")
    db.clear_table(new_table)
    print("\nPrinting table to show it is cleared")
    db.get_table(new_table)
else:
    print("\nClear on completion is false")
