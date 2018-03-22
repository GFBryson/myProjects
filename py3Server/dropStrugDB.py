import sqlite3

connection = sqlite3.connect("strugBot.db")
cursor = connection.cursor()

cursor.execute("DROP TABLE events;")


