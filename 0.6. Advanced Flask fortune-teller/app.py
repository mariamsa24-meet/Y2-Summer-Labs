from flask import Flask, render_template
import random
app=Flask(__name__)

@app.route('/')
def hello():
	return render_template("home.html")


@app.route('/fortune')
def fortune():
	fortune_list=["Happiness is not by chance its by choice",
"live is short and it is here to be lived","none but ourselves can free out minds","search for soul in everything",
"trust the magic of new beginnings","your patience is your power","everyday is a second chance", "i exist as i am",
"enjoy life ","be happy"]
	lol=random.choice(fortune_list)
	return render_template("fortune.html", lol=lol)

if __name__ == "__main__":  # Makes sure this is the main process
	app.run(debug=True)