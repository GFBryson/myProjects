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
import re
from slackclient import SlackClient

#----------CONSTANTS----------#

READ_DELAY=1 # 1 seccond read delay
FIRST_COMMAND='hello'
MENTION_LOOK= "^<@(|[WU].+?)>(.*)"#what the bot uses to look for its name being mentoined

#------------CODE-------------#

#slack client
client=SlackClient(os.environ.get('SLACK_BOT_TOKEN')# SLACK_BOT_TOKEN created in bash with $export SLACK_BOT_TOKEN='your bot user access token here'

#bot id
botID=None

if __name__ = "__main__":
	if client.rtm_connect(with_team_state=False):
		print("StrugBot up and running :D !!")
		
		botID=client.api_call("auth.test")["user_id"] #load bot id where previously set as 'None'
		#Used to help bot see whe it has been mentioned

		while True:
			command, channel = parse_bot_commands(client.rtm_read)#look for command signal
			
			if command:
				handle_command(command, channel)
			time.sleep(READ_DELAY) # read delay in loop
	else:
		print("Im sorry, your connection to StrugBot failed")


def parse_CMD(slack_events):
	#parse commands from bot API's
	
	for event in  slack_events:
		if event["type"] == "message" and not "subtype" in event:
			userID, message = parse_direct_mention(event["text"])
			if userID == botID
			return message, event["channel"]
	return None, None

def  parse_mention(message_text):
	#parse to find a direct mention to StrugBot
	match = re.search(MENTION_LOOK, message_text)
	
	return (match.group(1), match.group(2).strip()) if matches else (None, None)

def  handel_CMD(command, channel):
	#executes known commands
	
	#Default
	default_response = "Im unsure what you mean. Try *{}*.".format(FIRST_COMMAND)
	
	#Find and execute given command
	response = None
	
	#here we go !! :D 
	if command.startswith(FIRST_COMMAND):
		response="Hello!! Welcome to StrugBot \n I'm SUPER happy to see you"
	slack _client_.api_call(
		"chat.postessage",
		channel=channel,
		text=reponse or default_response
	) 







