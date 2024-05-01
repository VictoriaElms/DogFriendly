import json
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///locations.db'  # Adjust the database URI as needed
db = SQLAlchemy(app)

# Define the Locations model
class Locations(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True)
    address = db.Column(db.String(200))
    coordination = db.Column(db.Integer)
    category = db.Column(db.String(150))
    offleash = db.Column(db.Integer)
    outdoorspace = db.Column(db.Integer)
    favourite = db.relationship('Favourite', backref='location')

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'address': self.address,
            'coordination': self.coordination,
            'category': self.category,
            'offleash': self.offleash,
            'outdoorspace': self.outdoorspace
        }

# API endpoint to get all locations
@app.route("/api/locations", methods=["GET"])
def get_locations():
    locations = Locations.query.all()
    return jsonify([loc.serialize() for loc in locations])

# API endpoint to save a new location
@app.route("/api/locations", methods=["POST"])
def save_location():
    data = request.json
    new_location = Locations(
        name=data['name'],
        address=data['address'],
        coordination=data['coordination'],
        category=data['category'],
        offleash=data['offleash'],
        outdoorspace=data['outdoorspace']
    )
    db.session.add(new_location)
    db.session.commit()
    return jsonify({"message": "Location saved successfully"})

# API endpoint to filter locations by category
@app.route("/api/locations/filter", methods=["GET"])
def filter_locations():
    category = request.args.get("category")
    filtered_locations = Locations.query.filter_by(category=category).all()
    return jsonify([loc.serialize() for loc in filtered_locations])


@app.route("/")
def home():
    return jsonify({"message": "Home"})


@app.route("/about")
def about():
    return jsonify({"message": "About"})


@app.route("/locations")
def locations(): 
    return jsonify({"message": "Locations"})


@app.route("/signup")
def signup():
    return jsonify({"message": "Sign up"})


@app.route("/login")
def login():
    return jsonify({"message": "Login"})


@app.route("/logout")
def logout():
    return jsonify({"message": "Logout"})


@app.route("/myprofile")
def myprofile():
    return jsonify({"message": "My Profile"})


@app.route("/contactus")
def contactus():
    return jsonify({"message": "Contact us"})


if __name__=="__main__":
    app.run(debug=True)