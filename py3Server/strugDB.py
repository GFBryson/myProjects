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
		date_time DATE,
		channel VARCHAR(30),
		title VARCHAR(60),
		description VARCHAR(300)
		);"""

		self.cursor.execute(sql_command)
		self.connection.commit()


	def add_event(self,dateV,channelV,titleV):
		sql_command = """INSERT INTO events (id,date_time,channel,title,description)
		VALUES(NULL,"{date_time}","{channel}","{title}","{des}");"""

		sql_command=sql_command.format(date_time=dateV,channel=channelV,title=titleV,des=description)
		self.cursor.execute(sql_command)
		self.connection.commit()

	def print_events(self):
		self.cursor.execute("SELECT * FROM events ORDER BY date_time")
		result=self.cursor.fetchall()
		for r in result:
			print(r)

	def get_events(self):
		return self.cursor.execute("SELECT * FROM events ORDER BY date_time").fetchall()
