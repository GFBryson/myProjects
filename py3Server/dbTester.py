import strugDB

db=strugDB.sdb()

print("IMPORTS COMPLEATED")

print("TABLE CREATED")

print('adding to tabl')
db.add_event("2018-02-12","2:25","p","C7QGCSYMS","test event 1")

print("printing table")
db.print_events()


