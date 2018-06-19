from strugBotIntegrations import *
import os
import sys
import json
from flask import abort, Flask, jsonify, request, make_response

app=Flask(__name__)

def is_request_valid(request):

#	print(request.form['token'],'  ',os.environ['SLACK_VERIFICATION_TOKEN'],file=sys.stdout)
	is_token_valid = request.form['token'] == os.environ['SLACK_VERIFICATION_TOKEN']

#	print(request.form['team_id'],' ', os.environ['SLACK_TEAM_ID'],file=sys.stdout)
	is_team_id_valid = request.form['team_id'] == os.environ['SLACK_TEAM_ID']

	return is_token_valid and is_team_id_valid

@app.route('/hello-there', methods=['POST'])
def hello_there():
	print(request.form)
	print(request.form['trigger_id'])
	if not is_request_valid(request):
		print('request is invalid')
		abort(400)
	return jsonify(
		response_type='in_channel',
		text='command received',
	)

@app.route('/attach-trial', methods=['POST'])
def attach_trial():
	print('attach_trial entered')
	if not is_request_valid(request):
		print('request is invalid')
		abort(400)
	if button_test(None,None,None,request.form['channel_id']):
		return make_response("",200)
	else:
		abort(400)
@app.route('/event',methods=['POST'])
def event_catcher():
	args=request.form['text'].split(' ')
	print(args)
	if args[0]=='':
		sucsess,return_me=event_create_dialog(request.form['trigger_id'])

	elif args[0]=='list':
		sucsess,return_me=list_events(request.form['channel_id'])
	if not sucsess:
		return return_me
	return make_response("",200)
@app.route('/interact',methods=['POST'])
def button_catcher():
	payload=json.loads(request.form['payload'])#get  payload information out of the POST request
	#print(payload)
	sucsess=False#did we sucsess from the api call in strugBotIntegrations
	if payload['type']=='interactive_message':#if response is from an interactive message
		if payload['callback_id']=='test_button': #if button type is test button
			sucsess,return_me=button_test(payload['actions'][0]['value'],payload['trigger_id'],payload['message_ts'],payload['channel']['id'])#cale api call specific to button value and save sucsess value

	elif payload['type']=='dialog_submission':#if response is for a dialogue submission
#		print(payload['channel']['id'])

		sucsess,return_me= dialog_handler(payload['callback_id'],payload['submission'],payload['channel']['id'])#get response to dialogue update
		
	else:#this should never happen as there are only two types of messages from slack that would come to /interact
		print('aborting button catcher')
		abort(400)
	if sucsess:#if api call made
		return make_response("",200)
	else:#if sucsess is false then no api call was made
		return return_me
@app.route('/events',methods=['POST'])
def event_subscriptions():#more needs to be implemented to make this rspond properly to slack_events but for now it does the authentication an dreturns the challange var

	c=request.get_json(force=True)
	b=(c['challenge'])
	a=make_response(b,200)
	return a




