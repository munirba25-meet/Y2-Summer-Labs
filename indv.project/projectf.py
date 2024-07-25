from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

firebaseConfig = {
  "apiKey": "AIzaSyBQXkKRNwS7pOxJe5jmi3RdH8yPC0hMBfY",
  "authDomain": "idvproject.firebaseapp.com",
  "databaseURL": "https://idvproject-default-rtdb.europe-west1.firebasedatabase.app",
  "projectId": "idvproject",
  "storageBucket": "idvproject.appspot.com",
  "messagingSenderId": "948092994361",
  "appId": "1:948092994361:web:0652a393125a825ededee8",
  "measurementId": "G-Q5TR5E2PWE",
  "databaseURL":"https://idvproject-default-rtdb.europe-west1.firebasedatabase.app/"
};

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth() 
db=firebase.database()

@app.route('/home')
def home():
	return render_template("home.html")

@app.route('/signin', methods=['GET', 'POST'])
def signin():
	if request.method == "GET":
		return render_template("signin.html")
	else:
		email = request.form["email"]
		password = request.form["password"]
		login_session["user"]=auth.sign_in_with_email_and_password(email, password)
		return redirect(url_for("past"))
	


@app.route('/', methods=['GET', 'POST'])
def signup():
	if request.method == "GET":
		return render_template("signup.html")
	else:
		email = request.form["email"]
		password = request.form["password"]
		name = request.form["name"]

	


		user_data={
				'email':email,
				'password':password
		}
		db.child('users').child(login_session["user"]['localId']).set(user_data)
		login_session['user']=auth.create_user_with_email_and_password(email,password)
		return redirect(url_for("questions"))

		



@app.route('/questions', methods=['GET', 'POST'])
def questions():
	if request.method == 'GET':
		return render_template("questions.html")
	else:
		subject = request.form["subject"]
		food = request.form["food"]
		time = request.form["time"]
		questions={"subject":subject ,
							 "food": food ,
							 "time" : time 
							              }



		db.child('user').child(login_session["user"]['localId']).set(questions)
		return redirect(url_for("bye"))
				
		





@app.route('/bye')
def bye():
	uid = login_session['user']["localId"]
	return render_template('bye.html',subject=db.child('user').child(uid).child('subject').get().val(),
		food=db.child('user').child(uid).child('food').get().val(),
		time=db.child('user').child(uid).child('time').get().val())
if __name__ == '__main__':
    app.run(debug = True)
