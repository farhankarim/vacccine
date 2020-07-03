from flask import render_template,redirect,url_for,flash,request
from flaskapp.forms import RegistrationForm,RegisterUser,LoginUser
from flaskapp.models import User,Post
import random
from flaskapp import app,db
from passlib.hash import sha256_crypt
from flask_login import login_user,current_user,logout_user,login_required

@app.route("/success")
def success():
    return render_template("formsuccess.html")


@app.route("/reservations",methods=['GET','POST'])
def reservations():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        flash('Welcome '+form.email.data+".",'success')
        return redirect(url_for('register'))

    return render_template("reservation.html",form=form)

@app.route("/login",methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("dashboard"))
    form=LoginUser()
    if request.method == 'POST' and form.validate():
        user=User.query.filter_by(email=form.email.data).first()
        password=sha256_crypt.verify(form.password.data,user.password_hash)
        if user and password:
            login_user(user)
            next_page=request.args.get('next')
            flash("User Logged in successfully","success")
            return redirect(next_page) if next_page else redirect(url_for('dashboard'))
        else:
            flash("Email/Password incorrect","danger")
            return redirect(url_for('login'))

    return render_template("login.html",form=form)


@app.route("/dashboard",methods=['GET','POST'])
@login_required
def dashboard():
    return render_template("dashboard.html")

@app.route("/profile",methods=['GET','POST'])
@login_required
def profile():
    return render_template("profile.html")

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("login"))

@app.route("/register",methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("dashboard"))
    form=RegisterUser()
    
    if request.method == 'POST' and form.validate():
        hashed_password=sha256_crypt.encrypt(str(form.password.data))
        user=User(email=form.email.data, username=form.username.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Created user with email '+form.email.data+" successfully.",'success')
        return redirect(url_for('register'))

    return render_template("register.html",form=form)
#functionality Flask provide
#create yurts.html,activites.html,reseravation.html in templates folder
#create routes for each page
# pass page h1 tag from function to html page

#set FLASK_APP=app.py
#python app.py
# @app.route('/home')
#extra function given below
@app.route('/about')
def about():
    #create menu and activties list here
    menu=["home","about","contact","sign up"]
    data=["apple","mangoes","oranges","banana"]
    nums=[random.randint(1,100) for x in range(10)]
    user="Farhan Karim"
    title="My Portfolio"
    return render_template('index.html',title=title,nums=nums)

#functionality Flask provide
# main page of your website
@app.route('/')
#extra function given below
def index():
    return render_template('home.html')
