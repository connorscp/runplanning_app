from flask import Flask, render_template, request, redirect, session
import requests
import simplejson
from stravalib import Client
import os

app = Flask(__name__)

# Get configuration variables from Heroku global environment
client_id = os.environ['strava_client_id']
client_secret = os.environ['strava_client_secret']

print "client id cc: " + str(client_id)


@app.route('/',methods=['GET'])
def homepage():
	return redirect('/authenticate')

@app.route('/authenticate',methods=['GET','POST'])
def authenticate():
	#if request.method =='GET':
	return render_template('authenticate.html')

	#else:
	#	# request was a POST
	#	code = request.args.get('code', code)
	#	print "code cc: " + str(code)
	#	access_token = client.exchange_code_for_token(client_id=client_id, client_secret=str(client_secret), code=code)
	#	print "access token cc: " + str(access_token)
#
#		return render_template('authorization.html')

@app.route('/authorized')
def authorized():
	code = flask.request.args.get('code', '')
    client = stravalib.client.Client()
    token = client.exchange_code_for_token(client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            code = code)
    flask.session['access_token'] = token
    print token
    #return flask.redirect(flask.url_for('homepage'))
    return render_template('authorized.html')


if __name__ == '__main__':
	#app.run(host='0.0.0.0') # when running on DO. Start w/ vagrant:5000/index
	#app.run(port=33507) # when run on heroku
	app.run(debug=True)
