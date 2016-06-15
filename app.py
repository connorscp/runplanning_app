from flask import Flask, render_template, request, redirect, session
import requests
import json
import stravalib
import os

app = Flask(__name__)

# Get configuration variables from Heroku global environment
client_id = os.environ['strava_client_id']
client_secret = os.environ['strava_client_secret']


@app.route('/', methods=['GET'])
def homepage():
	return redirect('/authenticate')


# Authenticate page displays the 'Connect to Strava' button
@app.route('/authenticate', methods=['GET', 'POST'])
def authenticate():
	# if request.method =='GET':
	return render_template('authenticate.html')


# Converts code to access_token and outputs to authorized page
@app.route('/authorized', methods=['GET', 'POST'])
def authorized():
	# Get code from auth url and convert to token
	code = request.args.get('code')
	client = stravalib.client.Client()
	token = client.exchange_code_for_token(client_id=client_id,
		client_secret=client_secret,
		code=code)

	user = stravalib.Client(token)
	athlete = client.get_athlete()
	firstname = athlete.firstname

	# Output token to user on authorized.html
	return render_template('authorized.html', token=token, name=firstname)


if __name__ == '__main__':
	# app.run(host='0.0.0.0') # when running on DO. Start w/ vagrant:5000/index
	# app.run(port=33507) # when run on heroku
	app.run(debug=True)
