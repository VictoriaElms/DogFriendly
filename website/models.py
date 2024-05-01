from . import db 
from flask_login import UserMixin
from sqlalchemy.sql import func 

class Locations(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True)
    address = db.Column(db.String(200))
    coordination = db.Column(db.Integer)
    category = db.Column(db.String(150))
    offleash = db.Column(db.Integer)
    outdoorspace =db.Column(db.Integer)
    favourite = db.relationship('Favourite') #Not sure if I need this

class Favourite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location_id = db.Column(db.Integer, db.ForeignKey('locations.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    timeAdded = db.Column(db.DateTime(timezone=True), default=func.now())

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True) 
    password = db.Column(db.String(150)) 
    name = db.Column(db.String(150)) 
    username = db.Column(db.String(150))
    favourite = db.relationship('Favourite')