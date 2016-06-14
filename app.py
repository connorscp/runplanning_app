from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
	return redirect('/index')

@app.route('/index',methods=['GET','POST'])
def home():
	if request.method =='GET':
		return render_tempate('authenticate.html')
	else:
		# request was a POST
		pass


if __name__ == '__main__':
	#app.run(host='0.0.0.0') # when running on DO. Start w/ vagrant:5000/index
	#app.run(port=33507) # when run on heroku
	app.run(debug=True)