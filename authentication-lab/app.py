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
  "databaseURL": "https://yazanazaizah-3f2ad-default-rtdb.firebaseio.com/",

}


firebase = pyrebase.initialize_app(Config)
auth = firebase.auth()
db = firebase.database()


app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'


@app.route('/', methods=['GET', 'POST'])
def signin():
    error = ""
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        try: 
            
            login_session['user'] = auth.sign_in_with_email_and_password(email,password)
            

            
            return redirect(url_for('add_tweet'))
        except:
            error = "SIGN IN Authenticitoinsaoinsa / database afaiedkeedlead"
    
    return render_template("signin.html", msg_error = error)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error = ""
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
    #try:
        
        login_session['user'] = auth.create_user_with_email_and_password(email,password)
        UID = login_session['user']['localId']
        user = {"fullname":request.form['fullname'],
        "username":request.form['username'],
        "email":request.form['email'],
        "password":request.form['password'],
        "bio":request.form['bio']
        }
        db.child("Users").child(UID).set(user)
        return redirect(url_for('add_tweet'))
    #except:
        error = "SIGN UP Authenticitoinsaoinsa / database afaiedkeedlead"
    return render_template("signup.html", msg_error = error)


@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    if request.method=='POST':
        tweet = {"Title":request.form['Title'],"Text":request.form['Text'],"uid":login_session['user']['localId']}
        db.child("Tweets").push(tweet)
        return redirect(url_for('all_tweets'))

    return render_template("add_tweet.html")

@app.route('/all_tweets')
def all_tweets():
    return render_template('tweets.html', tweets = db.child("Tweets").get().val())



if __name__ == '__main__':
    app.run(debug=True)