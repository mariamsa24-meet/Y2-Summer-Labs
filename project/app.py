from flask import Flask, render_template, request, redirect, url_for, session
import pyrebase
app = Flask(__name__,template_folder='templates',static_folder='static')

firebaseConfig = {
  "apiKey": "AIzaSyDyvXt0Y8_o0cVKGzTYwjOxdgXZrnIZ3o8",
  "authDomain": "website-f6cdf.firebaseapp.com",
  "projectId": "website-f6cdf",
  "storageBucket": "website-f6cdf.appspot.com",
  "messagingSenderId": "151451809325",
  "appId": "1:151451809325:web:69e2dbd1862813f2656aa4",
  "measurementId": "G-97PX3Y94GL",
  "databaseURL":"https://website-f6cdf-default-rtdb.firebaseio.com/"
}

app.secret_key = 'your_secret_key'
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = auth.create_user_with_email_and_password(email, password)
        return redirect(url_for('ing'))
    return render_template('signup.html')

@app.route('/sigin', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = auth.get_user_by_email(email)
        session['user_id'] = user.uid
        return redirect(url_for('ing'))
    return render_template('signin.html')

@app.route('/ing', methods=['GET', 'POST'])
def ing():
    if request.method == 'GET':
        print("meow")
        return render_template('ing.html')
    else:
        flavor = request.form['flavors']
        try:
            if flavor == 'Lemon':
                return redirect(url_for('lemon'))
            elif flavor == 'carrots':
                return redirect(url_for('carrots'))
            elif flavor == 'chocolate':
                return redirect(url_for('choclate'))
            else:
                return redirect(url_for('vanilla'))
        except Exception as e:
            print(e)
    return render_template('ing.html')


@app.route('/lemon', methods=['GET', 'POST'])
def lemon():
    return render_template('lemon.html')

@app.route('/carrots', methods=['GET', 'POST'])
def carrots():
    return render_template('carrots.html')

@app.route('/choclate', methods=['GET', 'POST'])
def choclate():
    return render_template('choco.html')

@app.route('/vanilla', methods=['GET', 'POST'])
def vanilla():
    return render_template('vanilla.html')





if __name__ == '__main__':
    app.run(debug = True)