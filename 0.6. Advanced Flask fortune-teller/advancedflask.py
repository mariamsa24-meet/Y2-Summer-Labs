from flask import flask, render_template
import random
app=flask(_name_)

@app.route('/')
def hello():
	return render_template("home.html")
render_template('hello.html')

