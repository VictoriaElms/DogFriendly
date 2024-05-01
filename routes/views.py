from flask import Blueprint, render_template
from flask_login import current_user


views = Blueprint("views", __name__)


@views.route("/")
def home():
    return render_template("home.html", user=current_user)


@views.route("/about")
def about():
    return render_template("about.html", user=current_user)


@views.route("locations")
def locations():
    return render_template("locations.html", user=current_user)


@views.route("myprofile")
def myprofile():
    return render_template("myprofile.html", user=current_user)


@views.route("contactus", methods=["GET", "POST"])
def contactus():
    return render_template("contactus.html", user=current_user)
