import datetime
import strugDB
import re

db=strugDB.sdb()

res=db.get_events()

for r in res:
	print(r)
now=datetime.datetime.now()

#break test

#db.add_event("breakDate","breakTime","b","breaktest","testingforbreak")



#db.print_events()

print("CHECKING FOR SUNDAY")
print(now.weekday())

print("checking for date")
check= re.compile('^(20)+(1[8-9]|[2-9][0-9])+(-)+(0[1-9]|1[0-2])+(-)+([0-9]{2})$')
i="2018-03-20"
a=check.match(i)
if a:
	print(" hello")
print(a)
b=check.match("2017-02-13")
if b:
	print("world")
print(b)


exit()

