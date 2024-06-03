from flask import Blueprint, flash, render_template, request
from flask_login import current_user
from database.models import Contact
from dogfriendly import db 
from datetime import datetime


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


@views.route("contactus", methods=["GET", "POST"])
def contactus():
    if request.method == "POST":
        print("ERROR")
        email = request.form["email"]
        name = request.form["name"]
        subject = request.form["subjectTitle"]
        comments = request.form["comments"]
        now = datetime.now()
        if not email: 
            flash("Email required", category="error")
        elif not name:
            flash("Name required", category="error")
        elif not subject:
            flash("Subject required", category="error")
        elif not comments:
            flash("Comment required", category="error")
        else: 
            contact = Contact(
                email=email,
                name=name,
                subject=subject, 
                comments=comments, 
                time=now.strftime("%Y-%m-%d %H:%M.%S")

            )

            db.session.add(contact)
            db.session.commit()
            flash("Submitted")
    return render_template("contactus.html", user=current_user)
