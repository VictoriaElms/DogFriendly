# from database import db
from flask_login import UserMixin

from dogfriendly import db


class Locations(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True)
    address = db.Column(db.String(200))
    coordinates = db.Column(db.Integer)
    category = db.Column(db.String(150))
    offleash = db.Column(db.Integer)
    hours = db.Column(db.String(150))
    outdoorspace = db.Column(db.Integer)


class Favourites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location_id = db.Column(db.Integer, db.ForeignKey("locations.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    name = db.Column(db.String(150))
    username = db.Column(db.String(150))
