from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import LoginManager
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db 

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4: 
            flash('Email must be greater than three characters', category = 'error')
        elif len(name) <2: 
            flash('Name must be more than one character', category='error')
        elif password1 != password2: 
            flash('Passwords don\'t match', category='error')
        elif len(password1) < 7:
            flash('Password must be six characters or greater', category='error')
            return render_template('sign_up.html')
        else:
            # add user to database
            new_user = User(email=email, name=name, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account created!', category= 'success')
            return redirect(url_for('views.home'))
        
        return render_template('sign_up.html')
    
@auth.route('/about')
def about():
    return render_template("about.html")

@auth.route('locations')
def locations():
    return render_template("locations.html")

@auth.route('myprofile')
def myprofile():
    return render_template("myprofile.html")

@auth.route('contactus', methods=['GET', 'POST'])
def contactus():
    return render_template("contactus.html")