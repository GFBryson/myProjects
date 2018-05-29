#
#
#Gillian Bryson
#V00880054
#Feburary 9th 2018
#
# Code modifyied from basic tutorial at : https://www.fullstackpython.com/blog/build-first-slack-bot-python.html
#


#----------IMPORTS------------#
import os
import time
import datetime
import re
from slackclient import SlackClient
import random
import strugDB
from StrugEvents import strugEvents
from botResponses import responder
#----------CONSTANTS----------#

db=strugDB.sdb()

READ_DELAY=1 # 1 seccond read delay
MENTIONED = "^<@(|[WU].+?)>(.*)"#what the bot uses to look for its name being mentioned


NOW=datetime.datetime.now()



#------------CODE-------------#

#slack client
client=SlackClient(os.environ.get('SLACK_BOT_TOKEN')) # SLACK_BOT_TOKEN created in bash with $export SLACK_BOT_TOKEN='your bot user access token here' NOTE this will need to be redone each tim e you open the shell

#bot id
botID = None
def get_channels():
	chnl_api= client.api_call("channels.list") # get list of channel permissions attributes in json
	channel_list=[] # empty list which will hold channels if they exist
	if chnl_api["ok"] == True: # make sure channels exist
		channels= chnl_api["channels"] # get list of channels in json
		for c in channels: #for channel data group in channels json

			if c["is_member"]==True:# if The bot was invited into that group NOTE not necessary but prevents channels without events being pinged for no reason
				channel_list.append(c["id"])# add channel id to the list of chanels
	return channel_list
#parse the commands received from the api's
def parse_CMD(slack_events):
	#parse commands from bot API's
	#print(slack_events)
	for event in  slack_events:
		#print(event)
		if event["type"] == "message" and not "subtype" in event:
			print(event)
			userID, message = parse_mention(event["text"])
			if userID == botID:
				return message, event["channel"], event["user"]
	return 'None', 'None', 'None'

#look for bot name being mentioned
def  parse_mention(message_text):
	#parse to find a direct mention to StrugBot
	match = re.search(MENTIONED, message_text)

	#returns found ID and the rest of the message NOTE this means that bot MUST be mentioned first
	return (match.group(1), match.group(2).strip()) if match else (None, None)


#when mentioned is confirmed this handels how the bot responds the the mention
def  handle_CMD(command, channel,user):
	#executes known commands
	command=command.lower()

	#Default response
	default_response = "Im unsure what you mean. Try *{}*.".format('hello')

	#set response to None so if not set default_response is used
	response = None

	#Find and execute given command
	if command.startswith('hello') or command.startswith('hey'):#response to hey @strugbot or hello @strugbot
		response=responder.resp_hello()[random.randint(0,len(responder.resp_hello())-1)].format(usr="<@"+user+">")
		#"Hello!! Welcome to StrugBot \n I'm SUPER happy to see you"


	elif((user == 'U8KHG0P1U') and (('thanks bot' in command) or ('fuck you' in command))):# a little something special to troll a friend ;) 
		response="Russell the bot cannot register your reply at this time. Please do not harass the bot"
		response="hello"
		
	elif ('what' in command) and ('date' in command):# to return current date
		response=responder.resp_date()+NOW.strftime("%Y %m %d")
	elif ('what' in command) and ('time' in command):#to return current time
		response=responder.resp_time()+NOW.strftime("%H:%M")

	elif 'are you a secret t-rex' in command: #shhhh this is a secret ;)
		response=responder.resp_trex()

	elif ("make event" in command) or ("create event" in command) or ('add event' in command): # to make an event in the database

		if "&gt;&gt;" not in command: # respond with propper syntaxing for event creation
			response="would you like to make an event?\nUse the Syntax @StrugBot create event>> YYYY-MM-DD HH:MM a/p EVENT_NAME : DESCRIPTION"
		else:
			#print("making event")
			response=strugEvents.makeEvent(command,channel)

	elif('events' in command) and ('this' in command) and ('week' in command): # to tell the user what events are coming up in the next 7 days
		#print("sending events")
		response=strugEvents.print_week(channel) #rets string of events (multiline)


	client.api_call( # makes the call to the slack api with response or with default_response if no response is set
                 "chat.postMessage",
                 channel=channel,
                 text=response or default_response # if default then no conditions were met
         )

if __name__ == "__main__":
	if client.rtm_connect(with_team_state=False): # attempt to connect the bot
		print("StrugBot up and running :D !!")

		botID=client.api_call("auth.test")["user_id"] #load bot id where previously set as 'None'
		#Used to help bot see whe it has been mentioned
		weekly = False
		daily=False
		while True:
			command, channel, user = parse_CMD(client.rtm_read())#look for command signal

			#print("Command: "+command+" Channel: "+channel)

			if command != 'None':
				handle_CMD(command, channel, user)
			#checkEvents
			time.sleep(READ_DELAY) # read delay in loop
			now = datetime.datetime.now() #date and time current
		#	print(now.weekday()," ",now.hour," ",now.minute)


			#----------------ALL TIME EVENTS SHOULD BE MOVED TO A SEPERATE FILE FOR FUTURE MULTITHREADDING
			#checking for daily reminder of events
			if (now.hour == 9) and (now.minute==0):
				for ch in get_channels():
					client.api_call(
						"chat.postMessage",
						channel=ch,
						text="Unable to fetch Daily events at this time. Apologies for the inconveniance"
					)
			# checking for time match (if date then print upcomming events for the week)
			if (now.weekday() == 0) and (now.hour == 17) and (now.minute == 46):
				if(not weekly): #stops this printing for the whole minute
					weekly=True
					print("time trigger activated")
					for ch in get_channels(): #for every channel bot is a member of ...
						
						client.api_call( # ... send message containing the weeks events to that channel
							"chat.postMessage",
							channel=ch,
							text=strugEvents.print_week(ch)
						 )
			else:
				weekly = False #resets weekly check once time has passed
	else:
		print("Im sorry, your connection to StrugBot failed") # usually happens when the auth key is incorrect
