from flask import Flask, render_template, request, make_response, redirect, url_for, session
import pyrebase
config = {
  "apiKey": "AIzaSyA6Fbat93GU8zkkI82mDZKqqdqMM-LPP-c",
  "authDomain": "niezapp-ce5a9.firebaseapp.com",
  "databaseURL": "https://niezapp-ce5a9.firebaseio.com",
  "storageBucket": "niezapp-ce5a9.appspot.com",
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()
app = Flask(__name__)
app.secret_key = 'asdf123'
name = 'string';
@app.route("/", methods=['POST', 'GET'])
def main():
	all_posts = db.child('posts').get()
	
	if request.method == 'POST' and 'usn' in session:
		res = request.form
		db.child("posts").child(session['usn']).push(res['postInput'])
		all_posts = db.child('posts').get()
		print(all_posts)
		return render_template('index.html',name = name,all_posts=all_posts.val())
	return render_template('index.html',name = name,all_posts=all_posts.val())

@app.route("/login",methods=['POST','GET'])
def login():
	if request.args.get('action') == 'logout':
		session.clear()
	if request.method == 'POST':
		res = request.form
		all_users = db.child('users').get()
		for user in all_users.each():
			if user.key() == res['USN']:
				if user.val()['password'] == res['pass']:
					session['usn'] = res['USN']
					global name
					name = user.val()['name']
					return redirect(url_for('main'))
				else:
					
					return '<script>alert("Wrong Password");</script>'+render_template('login.html')
			print(user.key())	
	return render_template('login.html')

@app.route("/signup",methods=['POST','GET'])
def signup():
	if request.method == 'POST':
		res = request.form
		all_users = db.child('users').get()
		for user in all_users.each():
			if user.key() == res['usn']:
				return '<script>alert("USN already registered");</script>'+render_template('signup.html')
		if 'usn' not in session:
			db.child('users').child(res['usn']).set(res)
			session['usn'] = res['usn']
			all_users = db.child('users').get()
			for user in all_users.each():
				if user.key() == res['usn']:
					global name
					name = user.val()['name']
					print(name)
		return redirect(url_for('main'))
	return render_template('signup.html')

if __name__ == "__main__":
	app.run(debug = True, threaded = True)
