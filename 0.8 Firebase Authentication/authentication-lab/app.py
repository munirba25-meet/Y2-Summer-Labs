from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

firebaseConfig = {
	"apiKey": "AIzaSyAsqiNHzNQDP1F_GwDvGZfnnipwcO5ztL4",
	"authDomain": "authenticationlab-d6d04.firebaseapp.com",
	"projectId": "authenticationlab-d6d04",
	"storageBucket": "authenticationlab-d6d04.appspot.com",
	"messagingSenderId": "717647122167",
	"appId": "1:717647122167:web:6f54b8d20c64ba72ea0df2",
	"measurementId": "G-EDEPQ70PNR" ,
	"databaseURL" : ""
  }
 
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth() 
  
app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'


@app.route('/', methods=['GET', 'POST'])
def signin():
	return render_template("signin.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
	return render_template("signup.html")


@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
	return render_template("add_tweet.html")


if __name__ == '__main__':
	app.run(debug=True)