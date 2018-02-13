import datetime
import sqlite3


class sdb:
	connection=None
	cursor=None

	def __init__(self):#needed to either create to or connect to the strug and maked the events table
		self.connection = sqlite3.connect("strugBot.db")
		self.cursor = self.connection.cursor()
		self.create_events_table()

	def create_events_table(self):
		sql_command = """CREATE TABLE IF NOT EXISTS events(
		id INTEGER PRIMARY KEY,
		date DATE,
		time TIME,
		ampm CHAR(1),
		channel VARCHAR(30),
		title VARCHAR(60)
		);"""

		self.cursor.execute(sql_command)
		self.connection.commit()	


	def add_event(self,dateV,timeV,ampmV,channelV,titleV):
		sql_command = """INSERT INTO events (id,date,time,ampm,channel,title)
		VALUES(NULL,"{date}","{time}","{channel}","{title}","{ampm}");"""
	
		sql_command=sql_command.format(date=dateV,time=timeV,ampm=ampmV,channel=channelV,title=titleV)
		self.cursor.execute(sql_command)
		self.connection.commit()

	def print_events(self):
		self.cursor.execute("SELECT * FROM events")
		result=self.cursor.fetchall()
		for r in result:
			print(r)


