from flask import Flask, render_template, request, redirect, session
import requests
import json
import stravalib
import os

app = Flask(__name__)

# Get configuration variables from Heroku global environment
client_id = os.environ['strava_client_id']
client_secret = os.environ['strava_client_secret']

print "client id cc: " + str(client_id)


@app.route('/', methods=['GET'])
def homepage():
	return redirect('/authenticate')


@app.route('/authenticate', methods=['GET', 'POST'])
def authenticate():
	# if request.method =='GET':
	return render_template('authenticate.html')

@app.route('/authorized', methods=['GET', 'POST'])
def authorized():
	code = request.args.get('code')
	client = stravalib.client.Client()
	token = client.exchange_code_for_token(client_id=client_id,
		client_secret=client_secret,
		code=code)

	# Write user's username and token to tokens.json
	user = stravalib.Client(token)
	athlete = user.get_athlete()

	username = athlete.username

	user_tokens[username] = token

	with open('tokens/tokens.json', 'w') as f:
		json.dump(user_tokens, f)

	# Return authorized page
	name = athlete.firstname

	return render_template('authorized.html', code=code, token=token, name=name, email=email)


if __name__ == '__main__':
	# app.run(host='0.0.0.0') # when running on DO. Start w/ vagrant:5000/index
	# app.run(port=33507) # when run on heroku
	app.run(debug=True)
