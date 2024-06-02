from flask import request, jsonify, Blueprint
from flask_login import current_user, login_required
from database.models import Favourites, Locations
from dogfriendly import db

api = Blueprint("api", __name__)


# API endpoint to get all locations
@api.route("/api/locations", methods=["GET"])
def get_locations():
    locations = Locations.query.all()
    return jsonify(
        [
            {
                "address": loc.address,
                "category": loc.category,
                "coordinates": loc.coordinates,
                "name": loc.name,
                "offleash": loc.offleash,
                "hours": loc.hours,
                "outdoorspace": loc.outdoorspace,
            }
            for loc in locations
        ]
    )


# API endpoint for favourites
@api.route("/api/locations/save")
def save_favourites():
    location = Locations.query.filter_by(name=request.args.get("id")).all()
    new_save = Favourites(location_id=location[0].id, user_id=current_user.id)
    db.session.add(new_save)
    db.session.commit()
    return "Location added to favourites"


# API endpoint for show favourites
@api.route("api/locations/favourites", methods=["GET"])
def get_favourites():
    login_required
    rows = Favourites.query.filter_by(user_id=current_user.id).all()
    location_ids = []
    for row in rows:
        location_ids.append(row.location_id)
    locations = Locations.query.filter(Locations.id in location_ids).all()
    return jsonify(
        [
            {
                "address": loc.address,
                "category": loc.category,
                "coordinates": loc.coordinates,
                "name": loc.name,
                "offleash": loc.offleash,
                "hours": loc.hours,
                "outdoorspace": loc.outdoorspace,
            }
            for loc in locations
        ]
    )

    # Make this end points: get userID then find all of the matching rows in the favourites table and then get the location ids
    # return the rows from the locations table that matches the ids
    # write front end function in locations.js that adds locations to the div almost the same as the formatLocations