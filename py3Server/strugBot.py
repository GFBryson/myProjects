#
#
#Gillian Bryson
#V00880054
#Feburary 9th 2018
#
# Code modifyied from tutorial at : https://www.fullstackpython.com/blog/build-first-slack-bot-python.html
#


#----------IMPORTS------------#
import os
import time
import datetime
import re
from slackclient import SlackClient
import random
import strugDB
#----------CONSTANTS----------#

db=strugDB.sdb()

READ_DELAY=1 # 1 seccond read delay
MENTIONED = "^<@(|[WU].+?)>(.*)"#what the bot uses to look for its name being mentioned
NOW=datetime.datetime.now()

#'hello' responses
hello=[]
hello.append('Hey there! how\'s it going?')
hello.append('Hi :grinning:')
hello.append('Hello, whats up?')
hello.append('Hey buddy :wave:,\nHow are you doing?')
hello.append('Hi!\nI\'m StrugBot, and I\'m super happy to be here!!')
hello.append('Sup!')
hello.append('Hi,\nwhat can I do for you?')
hello.append('.....Hey...')
hello.append('WAZZZZUUUUUUUUUUUUUUP')

#'what is the date' response
date='the date is: '

#'what time is it' response
timeCall='the time is: '

#secret trex response
tRex="I am a T-Rex!:t-rex:\nI have a BIG head and little arms,\nRAWWWRRRRR!!"


#------------CODE-------------#

#slack client
client=SlackClient(os.environ.get('SLACK_BOT_TOKEN')) # SLACK_BOT_TOKEN created in bash with $export SLACK_BOT_TOKEN='your bot user access token here' NOTE this will need to be redone each tim e you open the shell

#bot id
botID = None

#parse the commands received from the api's
def parse_CMD(slack_events):
	#parse commands from bot API's
	#print(slack_events)
	for event in  slack_events:
		print(event)
		if event["type"] == "message" and not "subtype" in event:
			userID, message = parse_mention(event["text"])
			if userID == botID:
				return message, event["channel"]
	return 'None', 'None'

#look for bot name being mentioned
def  parse_mention(message_text):
	#parse to find a direct mention to StrugBot
	match = re.search(MENTIONED, message_text)

	print("match: ") 
	print(match)

	return (match.group(1), match.group(2).strip()) if match else (None, None)


#when mentioned is confirmed this handels how the bot responds the the mention
def  handle_CMD(command, channel):
	#executes known commands
	command=command.lower()
	print("command: "+command)
	#command=command.lower()
	#Default
	default_response = "Im unsure what you mean. Try *{}*.".format('hello')

	#Find and execute given command
	response = None

	#response to hey @strugbot or hello @strugbot
	if command.startswith('hello') or command.startswith('hey'):
		#print("FIRST_COMMAND found as : ", FIRST_COMMAND)
		response=hello[random.randint(0,len(hello)-1)]#"Hello!! Welcome to StrugBot \n I'm SUPER happy to see you"
	
	if 'what is the date' in command:
		response=date+NOW.strftime("%Y %m %d")
	if ('what' in command) and ('time' in command):
		response=timeCall+NOW.strftime("%H:%M")
	
	if 'are you a secret t-rex' in command:
		response=tRex	
	
	if "make event" in command or "create event" in command:
		if "&gt;&gt;" not in command:
			response="would you like to make an event?\nUse the Syntax @StrugBot create event>> YYYY-MM-DD HH:MM a/p EVENT_NAME"

		else:
			parsed=((command.split("&gt;&gt;"))[1].strip()).split(" ")
			print("\nparsed")
			print(parsed)
			print()
			db.add_event(parsed[0],parsed[1],parsed[2],channel,parsed[3])
			db.print_events()
			response="event "+parsed[3]+" created for "+parsed[1]+" "+parsed[2]+"m on "+parsed[0]


	client.api_call(
                 "chat.postMessage",
                 channel=channel,
                 text=response or default_response
         )

if __name__ == "__main__":
	if client.rtm_connect(with_team_state=False):
		print("StrugBot up and running :D !!")

		botID=client.api_call("auth.test")["user_id"] #load bot id where previously set as 'None'
		#Used to help bot see whe it has been mentioned

		while True:
			command, channel = parse_CMD(client.rtm_read())#look for command signal

			#print("Command: "+command+" Channel: "+channel)

			if command != 'None':
				handle_CMD(command, channel)
			time.sleep(READ_DELAY) # read delay in loop
	else:
		print("Im sorry, your connection to StrugBot failed")
