import math
import datetime
import os
from slackclient import SlackClient as slack

slack_client = slack(os.environ['SLACK_BOT_TOKEN'])
def button_test(name,trigger):
#	print('button_test entered, type:',type,' trigger:',trigger)
	if name==None:
		return {
			'response_type':'in_channel',
			'text':'this should not be in the attachement',
			'attachments':[{
				'text':'this should be in the attachment',
				'fallback':'im sorry, that didnt work',	
				'color':"#3AA3E3",
				'callback_id':'test_button',
				'attachemnt_type':'default',
				'actions':[
					{
						'name':'button_test',
						'text':'I am a button',
						'type':'button',
						'value':'test_button_pressed'
					},
					{
						'name':'dialogue_test',
						'text':'test dialogue',
						'type':'button',
						'value':'dialogue_trigger'
					}
				]
			}]
		}

	if name=='test_button_pressed':
		return{
			'response_type':'in_channel',
			'text':'this should not be in the attachement',
			'attachments':[{
				'text':'this should be in the attachment\n:heavy_check_mark: Great!',
				'fallback':'im sorry, that didnt work',	
				'color':"#3AA3E3",
				'callback_id':'test_button',
				'attachemnt_type':'default',

			}]
		}
	if name=='dialogue_trigger':
		trial_dialogue(trigger)
		return None
def trial_dialogue(trigger):
	print('trial dilogue entered')
	d=slack_client.api_call(
		'dialog.open',
		trigger_id=trigger,
		dialog={
			'title':'test dialogue block',
			'submit_label':'test_dialogue',
			'callback_id':'dialogue_test_call',
			'elements':[{
				'type':'text',
				'label':'enter some text',
				'name':'test_text'
			}]	
		}
	)
#	print(d)
def trial_dialogue_msg_update(name,info):
	print(name)
	if name=='dialogue_test_call':
		return {
			'response_type':'in_channel',
			'txt':info['test_text']
			}
	else:
		print('unknown dialogue call')
	return {}











