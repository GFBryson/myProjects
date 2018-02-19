import strugDB
import datetime

db=strugDB_datetime.sdb()

db.add_event(datetime.datetime(2018,2,20,10,01),"ch","test01")
db.add_event(datetime.datetime(2018,2,28,10,40),"ch","test02")
db.add_event(datetime.datetime(2018,2,16,10,40),"ch","test03")
db.add_event(datetime.datetime(2018,2,19,10,40),"ch","test04")

print("datetime_DB loaded")



