from flask import request, jsonify, Blueprint

from database.models import Locations


api = Blueprint("api", __name__)


# API endpoint to get all locations
@api.route("/api/locations", methods=["GET"])
def get_locations():
    locations = Locations.query.all()
    return jsonify([loc.serialize() for loc in locations])


# API endpoint to save a new location
@api.route("/api/locations/save", methods=["POST"])
def save_location():
    data = request.json
    new_location = Locations(
        name=data["name"],
        address=data["address"],
        coordinates=data["coordinates"],
        category=data["category"],
        offleash=data["offleash"],
        outdoorspace=data["outdoorspace"],
    )
    db.session.add(new_location)
    db.session.commit()
    return jsonify({"message": "Location saved successfully"})


# API endpoint to filter locations by category
@api.route("/api/locations/filter", methods=["GET"])
def filter_locations():
    category = request.args.get("category")
    filtered_locations = Locations.query.filter_by(category=category).all()
    return jsonify([loc.serialize() for loc in filtered_locations])
