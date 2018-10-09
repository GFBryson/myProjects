import math
from datetime import *
import os
from slackclient import SlackClient as slack
import re 
import classMateDB


db=classMateDB.sdb()
slack_client = slack(os.environ['SLACK_BOT_TOKEN'])

#handels making the api calls to slack after server gets POST
#needs to be changed so that it can better interact with the orriginal chat bot 
def button_test(name,trigger,time,ch):#rename when no longer in testing phase
#	print('button_test entered, type:',type,' trigger:',trigger)
	print("name: ",name)
	if name==None:
		b=slack_client.api_call (
			"chat.postMessage",
			channel=ch,
			text='this should not be in the attachement',
			attachments=[{
				'text':'this should be in the attachment',
				'fallback':'im sorry, that didnt work',	
				'color':"#30A3E3",
				'callback_id':'test_button',
				'attachemnt_type':'default',
				'actions':[
					{
						'name':'button_test',
						'text':'I am a button',
						'type':'button',
						'value':'test_button_pressed'
					}]
			}]
		)
		return True,None

	if name=='test_button_pressed':
		b=slack_client.api_call(
			"chat.update",
			ts=time,
			channel=ch,
			text='this should not be in the attachement',
			attachments=[{
				'text':'this should be in the attachment\n:heavy_check_mark: Great!',
				'fallback':'im sorry, that didnt work',	
				'color':"#3AA3E3",
				'callback_id':'test_button',
				'attachemnt_type':'default',
			}]
		)
		print(b)
		return True,None
	return False,None # if we are here then there was  nothing to trigger
		
def event_create_dialog(trigger):# This extra method is unesseesary but was made to make it easier to find durinf testing/learning/debugging. When working move into button_test method
	print('trial dilogue entered')
	d=slack_client.api_call(
		'dialog.open',
		trigger_id=trigger,
		dialog={
			'title':'Create Event',
			'submit_label':'Create',
			'callback_id':'add_event',
			'elements':[{
				'type':'text',
				'label':'event title',
				'name':'title',
				'max_length':60
				},{
				'type':'text',
				'label':'Date',
				'hint':'DD/MM/YY',
				'name':'date'
				},{
				'type':'text',
				'label':'Time',
				'hint':'hh:mm am/pm',
				'name':'time'
				},{
				'type':'text',
				'label':'Location',
				'max_length':60,
				'name':'loc',
				'optional':True
				},{
				'type':'textarea',
				'label':'Description',
				'hint':'provide more information as needed',
				'name':'description',
				'max_length':1000,
				'optional':True
				}]	
		}
	)
	return True,None
def asignment_create_dialog (trigger):
	d=slack_client.api_call(
		'dialog.open',
		trigger_id=trigger,
		dialog={
			'title':'Create Assignment',
			'submit_label':'Create_Assignemnt',
			'callback_id':'add_assignment',
			'elements':[{
				'type':'text',
				'label':'assignment title',
				'name':'title',
				'max_length':60
				},{
				'type':'text',
				'label':'Date',
				'hint':'DD/MM/YY',
				'name':'date'
				},{
				'type':'text',
				'label':'Time',
				'hint':'hh:mm am/pm     If not specified default will be 9:00 am',
				'name':'time',
				'value':'9:00 am',
				'optional':True		
				},{
				'type':'text',
				'label':'Location',
				'max_length':60,
				'name':'loc',
				'optional':True
				},{
				'type':'textarea',
				'label':'Description',
				'hint':'provide more information as needed',
				'name':'description',
				'max_length':1000,
				'optional':True
				}]	
		}
	)
return True,None
def dialog_handler(name,info,ch):
	if name=='add_event':
	#print(name)
		error,ret=errorCall(info)
		if error:
			return False,ret
		db.add_channel(ch)
		print(len(info['date']))
		if len(info['date'])<9:#while the regrex will allow for a date int the form dd/mm/yy i need dd/mm/yyyy for the datetime parser so this just gives any date without yyyy a +2000
			dt_tmp=info['date'].split('/')
			dt_tmp[2]= str(int(dt_tmp[2])+2000)
			info['date']=dt_tmp[0]+"/"+dt_tmp[1]+"/"+dt_tmp[2]
		tm_tmp=info['time'].split(' ')#checking for  am or pm, as for pm i need to add 12h for the datetime object to be accurate
		if (tm_tmp[1]=='pm')and(int(tm_tmp[0].split(':')[0])<12):#if time is pm and is not a noon time
			tm_tmp[0]=(str(int(tm_tmp[0].split(':')[0])+12))+':'+(tm_tmp[0].split(':')[1])
		if (tm_tmp[1]=='am') and (int(tm_tmp.split(':')[0])==12):#if am and 12 specified time should be 0:##
			tm_tmp[0]='0:'+tm_tmp[0].split(':')[1]
		sucsess=db.add_event({'title':info['title'],'loc':info['loc'],'desc':info['description'],'channel':ch,'date':datetime.strptime(info['date']+' '+tm_tmp[0],'%d/%m/%Y %H:%M')})
		if sucsess == 1:
			slack_client.api_call(
				'chat.postMessage',
				channel=ch,
				text=db.get_events(order_by=ch)
			)
		else:
			slack_client.api_call(
				'chat.postMessage',
				channel=ch,
				text="event failed to be added"
			)
	elif name == 'add_assignment':
		error,ret=errorCall(info)
		if error:
			return False,ret
		db.add_channel(ch)
		print(len(info['date']))
		if len(info['date'])<9:#while the regrex will allow for a date int the form dd/mm/yy i need dd/mm/yyyy for the datetime parser so this just gives any date without yyyy a +2000
			dt_tmp=info['date'].split('/')
			dt_tmp[2]= str(int(dt_tmp[2])+2000)
			info['date']=dt_tmp[0]+"/"+dt_tmp[1]+"/"+dt_tmp[2]
		tm_tmp=info['time'].split(' ')#checking for  am or pm, as for pm i need to add 12h for the datetime object to be accurate
		if (tm_tmp[1]=='pm')and(int(tm_tmp[0].split(':')[0])<12):#if time is pm and is not a noon time
			tm_tmp[0]=(str(int(tm_tmp[0].split(':')[0])+12))+':'+(tm_tmp[0].split(':')[1])
		if (tm_tmp[1]=='am') and (int(tm_tmp.split(':')[0])==12):#if am and 12 specified time should be 0:##
			tm_tmp[0]='0:'+tm_tmp[0].split(':')[1]
		sucsess=db.add_assignment({'title':info['title'],'loc':info['loc'],'desc':info['description'],'channel':ch,'date':datetime.strptime(info['date']+' '+tm_tmp[0],'%d/%m/%Y %H:%M')})
		if sucsess == 1:
			slack_client.api_call(
				'chat.postMessage',
				channel=ch,
				text=db.get_assignments(order_by=ch)
			)
		else:
			slack_client.api_call(
				'chat.postMessage',
				channel=ch,
				text="event failed to be added"
			)
	elif name == add_exam:
		print('Exam response section triggered, no response created yet, returning error')
		return False,"uncreated"
	else:
		print('unknown dialogue call')
		return False,None
	return True,None
	

def errorCall(info):
	ret_me = "{'errors':["
	error=False
	if not re.search(r"^(?:(?:31(\/|-|\.)(?:0?[13578]|1[02]|(?:Jan|Mar|May|Jul|Aug|Oct|Dec)))\1|(?:(?:29|30)(\/|-|\.)(?:0?[1,3-9]|1[0-2]|(?:Jan|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec))\2))(?:(?:1[6-9]|[2-9]\d)?\d{2})$|^(?:29(\/|-|\.)(?:0?2|(?:Feb))\3(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00))))$|^(?:0?[1-9]|1\d|2[0-8])(\/|-|\.)(?:(?:0?[1-9]|(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep))|(?:1[0-2]|(?:Oct|Nov|Dec)))\4(?:(?:1[6-9]|[2-9]\d)?\d{2})$",info['date']):
 #i owe the regex to Alok Chaudhary on Stack overflow https://stackoverflow.com/questions/15491894/regex-to-validate-date-format-dd-mm-yyyy?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa

		error=True
		ret_me+="{'name':'date','error':'Please Follow Formatting: MM/DD/YYYY'}"
	if not re.search(r"^((1[0-2]|0?[1-9]):([0-5][0-9]) ([AaPp][Mm]))$",info['time']):
		if error:
			ret_me+=","
		ret_me+="{'name':'time','error':'Please follow date formatting HH:mm'}"
		error=True
	ret_me+="]}"

	if error:
		return True, ret_me
	return False, None	

def list_events(ch):
	events=db.select_event(ch)
	print(events)
	return True, None




