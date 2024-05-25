from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import (
    current_user,
    login_user,
    login_required,
    logout_user,
)
from werkzeug.security import generate_password_hash, check_password_hash

from database.models import Users
from dogfriendly import db

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = Users.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash("Logged in successfully!", category="success")
                login_user(user, remember=True)
                return redirect(url_for("views.myprofile"))
            else:
                flash("Incorrect password", category="error")
        else:
            flash("Email does not exist", category="error")

    return render_template("login.html", user=current_user)


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("views.home"))


@auth.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        email = request.form.get("email")
        name = request.form.get("name")
        username = request.form.get("username")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
        user = Users.query.filter_by(email=email).first()
        if user:
            flash("Email already exists", category="error")
        elif len(email) < 4:
            flash("Email must be greater than three characters", category="error")
        elif len(name) < 2:
            flash("Name must be more than one character", category="error")
        elif password1 != password2:
            flash("Passwords don't match", category="error")
        elif len(password1) < 7:
            flash("Password must be six characters or greater", category="error")
            return render_template("signup.html", user=current_user)
        else:
            # add user to database
            new_user = Users(
                email=email,
                name=name,
                password=generate_password_hash(password1, method="sha256"),
                username=username,
            )
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash("Account created!", category="success")
            return redirect(url_for("views.home"))

    return render_template("signup.html", user=current_user)


