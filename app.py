from flask import Flask, render_template, request, redirect
import requests
import simplejson
from stravalib import Client
import configparser

app = Flask(__name__)

# Load the config from a file
cfg = configparser.ConfigParser(default_section="StravaClient")
cfg.read("strava.cfg")

client_id = cfg.get("StravaClient", "ClientId")
print client_id

@app.route('/',methods=['GET'])
def index():
	return redirect('/index')

@app.route('/index',methods=['GET','POST'])
def home():
	if request.method =='GET':
		return render_template('authenticate.html')
	else:
		# request was a POST
		code = request.get('code')
		access_token = client.exchange_code_for_token(client_id=1234, client_secret='asdf1234', code=code)


if __name__ == '__main__':
	#app.run(host='0.0.0.0') # when running on DO. Start w/ vagrant:5000/index
	#app.run(port=33507) # when run on heroku
	app.run(debug=True)