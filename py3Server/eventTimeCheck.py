import datetime
import strugDB

stripper="%Y-%m-%d %H:%M:%S"
now=datetime.datetime.now()

print(now)


db=strugDB.sdb()

events=db.get_events()

date=now.date
print(date)
print(now.year)
print(now.month)
print(now.day)

for e in events:
	print(e)
	date=datetime.datetime.strptime(e[1],stripper)
	print((date-now).days)
	"""print(date)
	print(date.year)
	print(date.month)
	print(date.day)
	print(date.hour)
	print(date.minute)"""


