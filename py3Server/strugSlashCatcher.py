from strugBotIntegrations import *
import os
import sys
import json
from flask import abort, Flask, jsonify, request

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
		abort(400)
	return jsonify(
		response_type='in_channel',
		text='command received',
	)

@app.route('/attach-trial', methods=['POST'])
def attach_trial():
	if not is_request_valid(request):
		abort(400)
	return jsonify(button_test(None,None))
@app.route('/interact',methods=['POST'])
def button_catcher():
	print('hello')
	a=json.loads(request.form['payload'])['type']
	print(a)
	jsn=None
	if a=='interactive_message':
		value=json.loads(request.form['payload'])['actions'][0]['value']
		t_id=json.loads(request.form['payload'])['trigger_id']
		id=json.loads(request.form['payload'])['callback_id']
		if id=='test_button': 
				jsn=button_test(value,t_id)
		if jsn!=None:
				return jsonify(jsn)
	elif a=='dialog_submission':
		callback_id=json.loads(request.form['payload'])['callback_id']
		info=json.loads(request.form['payload'])['submission']
		return jsonify(trial_dialogue_msg_update(callback_id,info))
#	print(json.loads(request.form['payload']))		
	else:
		print('aborting cutton catcher')
		abort(400)



