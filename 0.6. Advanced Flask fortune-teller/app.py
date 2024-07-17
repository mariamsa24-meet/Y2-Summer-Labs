from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('home.html')
    elif request.method == 'POST':
        birthmonth = request.form['birthm']
        return redirect(url_for('fortune', monthb=birthmonth))

@app.route('/fortune/<monthb>')
def fortune(monthb):
    list_for = [
        "In dreams and in love there are no impossibilities.",
        "Love is like wildflowers…it is often found in the most unlikely places.",
        "The one you love is closer than you think.",
        "Paradise is always where love dwells.",
        "Help! I'm being held prisoner in a fortune cookie factory.",
        "Life is what happens to you while you are busy making other plans.",
        "Borrow money from a pessimist. They don't expect it back.",
        "He who throws dirt is losing ground.",
        "A closed mouth gathers no feet."
    ]
    length = len(monthb)
    if 0 < length <= 9:
        return render_template("fortune.html", for_b=list_for[length - 1])
    else:
        return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True, port=5001)
