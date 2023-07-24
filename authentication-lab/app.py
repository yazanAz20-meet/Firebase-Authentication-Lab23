from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

Config = {
  "apiKey": "AIzaSyAhHAIZZqAzesSo9jOGcLiVIR_0-CkHOWI",
  "authDomain": "yazanazaizah-3f2ad.firebaseapp.com",
  "projectId": "yazanazaizah-3f2ad",
  "storageBucket": "yazanazaizah-3f2ad.appspot.com",
  "messagingSenderId": "763389423409",
  "appId": "1:763389423409:web:e205b9f936d9c61c874a10",
  "measurementId": "G-1BETT1J7T6",
  "databaseURL": "",

}


firebase = pyrebase.initialize_app(Config)
auth = firebase.auth()


app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'


@app.route('/', methods=['GET', 'POST'])
def signin():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        try: 
            login_session['user'] = auth.sign_in_with_email_and_password(email,password)
            return redirect(url_for('add_tweet'))
        except:
            print("error2")
    
    return render_template("signin.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        try: 
            login_session['user'] = auth.create_user_with_email_and_password(email,password)
            return redirect(url_for('add_tweet'))
        except:
            print("error")
    return render_template("signup.html")


@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    return render_template("add_tweet.html")


if __name__ == '__main__':
    app.run(debug=True)