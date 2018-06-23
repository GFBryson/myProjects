import datetime
import sqlite3


class sdb:
	connection=None
	cursor=None

	def __init__(self):#needed to either create to or connect to the strug and maked the events table
		self.connection = sqlite3.connect("classMate.db")
		self.cursor = self.connection.cursor()
		self.create_events_table()

	def create_events_table(self):
		print("in table maker")
		
		sql_commands= [e for e in (open('build_db.txt','r').read()).split('--split--') if ('--' not in e)]

		
		print("file read")
		for c in sql_commands:
			try:
				self.cursor.execute(c)
			except Exception as e:
				raise e
			print("executed")
		self.connection.commit()
		print("committed")


	def add_channel(self,ch):
		if self.cursor.execute('select * from channels where ch_id = "{channel}";'.format(channel=ch)).fetchall() == []:
			self.cursor.execute('insert into channels(ch_id) values("{channel}");'.format(channel=ch))
	def add_event(self,info):
		self.cursor.execute('select ch_id from channels where ch_id ="{ch}";'.format(ch=info['channel']))
		a=self.cursor.fetchall()
		if a==[]:
			return -1
		sql_command = """INSERT INTO events (ev_id,date_time,ch_id,title,description,loc)
		VALUES(NULL,"{date_time}","{channel}","{title}","{des}","{loc}");""".format(date_time=info['date'],channel=info['channel'],title=info['title'],des=info['desc'],loc=info['loc'])
		self.cursor.execute(sql_command)
		self.connection.commit()
		return 1
	def print_table(self,table):
		self.cursor.execute("SELECT * FROM {tbl}".format(tbl=table))
		result=self.cursor.fetchall()
		for r in result:
			print(r)

	def get_events(self,order_by=None):
		if order_by==None:
			return self.cursor.execute("select * from events;").fetchall()
		return self.cursor.execute("SELECT * FROM events ORDER BY '{order}'".format(order=order_by)).fetchall()
	def select_event(self,ch):
		return self.cursor.execute("select * from events where ch_id = '{channel}';".format(channel=ch)).fetchall()
		
