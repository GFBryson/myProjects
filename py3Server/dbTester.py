import strugDB
from datetime import *
db=strugDB.sdb()

print("IMPORTS COMPLEATED")

print("TABLE CREATED")

print('adding to tabl')
date="20/10/2018"
time="3:00"
datetime_string=date+" "+time
datetime_format=datetime.strptime(date+" "+time,"%d/%m/%Y %H:%M")
print (datetime_string)
print(datetime_format)
info={'title':'dummy','loc':'place not here is there','desc':'nothing to see here folks, move it along','channel':'NULL','date':datetime_format}
a=db.add_event(info)
if a==-1:
	print("channel not found line not added")
#db.add_event("2018-02-12","2:25","p","C7QGCSYMS","test event 1")

print("printing events table")
db.print_table('events')
print("printing channels table")
db.print_table('channels')
print("test done")
db.add_channel(info['channel'])
db.add_event(info)
db.print_table('events')
db.print_table('channels')


