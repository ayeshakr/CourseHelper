from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def hello_world():
	return render_template("index.html")

@app.route('/register')
def registration():
	return render_template("register.html")