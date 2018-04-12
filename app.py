from flask import Flask, render_template, request, make_response, redirect, url_for, session

app = Flask(__name__)

@app.route("/")
def main():
	return render_template('index.html')	


if __name__ == "__main__":
	app.run(debug = True, threaded = True)