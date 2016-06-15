from flask import Flask, render_template, request, redirect, session
import requests
import simplejson
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

	# else:
	#	# request was a POST
	#	code = request.args.get('code', code)
	#	print "code cc: " + str(code)
	#	access_token = client.exchange_code_for_token(client_id=client_id, client_secret=str(client_secret), code=code)
	#	print "access token cc: " + str(access_token)

	#	return render_template('authorization.html')

@app.route('/authorized', methods=['GET', 'POST'])
def authorized():
	code = request.args.get('code')
	client = stravalib.client.Client()
	token = client.exchange_code_for_token(client_id=client_id,
		client_secret=client_secret,
		code=code)

	client2 = stravalib.Client(token)
	athlete = client2.get_athlete()
	name = athlete.firstname
	email = athlete.email

	print name
	print email


	return render_template('authorized.html', code=code, token=token, name=name, email=email)
"""
Congratulations! We've successfully authorized to connect your running history to 
the Run Planning app! The code is 6546d8346384d41dc26a99f5d40654981355d415. 
The token is e4bd0abdb7726b04a7a2c715684b0576f14414ca
"""




"""
@app.route('/authorized')
def authorized():
	code = flask.request.args.get('code', '')
    client = stravalib.client.Client()
    token = client.exchange_code_for_token(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, code = code)
    flask.session['access_token'] = token
    print token
    # return flask.redirect(flask.url_for('homepage'))
    return render_template('authorized.html')
"""

if __name__ == '__main__':
	# app.run(host='0.0.0.0') # when running on DO. Start w/ vagrant:5000/index
	# app.run(port=33507) # when run on heroku
	app.run(debug=True)
