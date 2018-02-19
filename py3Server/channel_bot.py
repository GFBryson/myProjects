from slackclient import SlackClient
import os 

slack_token = os.environ.get("SLACK_BOT_TOKEN")
sc = SlackClient(slack_token)

channel_call=sc.api_call("channels.list",exclude_archived=1)['channels']

#print(a)

channels=[]

for response in channel_call:
	channels.append(response['id'])

print(b) 




