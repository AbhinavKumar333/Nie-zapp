from flask import Flask, render_template, request, make_response, redirect, url_for, session
from firebase import firebase
firebase = firebase.FirebaseApplication('https://niezapp-ce5a9.firebaseio.com',None)
app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def main():	
	if request.method == 'POST':
		res = request.form
		ip = firebase.post('/posts' + postId,res['postInput'])		
		ret = firebase.get('/posts',None)
		return render_template('index.html',d=ret)
	ret = firebase.get('/posts',None)
	return render_template('index.html',d=ret)

@app.route("/login")
def login():
	return render_template('login.html')

@app.route("/signup")
def signup():
	return render_template('signup.html')

if __name__ == "__main__":
	app.run(debug = True, threaded = True)
