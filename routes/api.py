from flask import request, jsonify, Blueprint
from flask_login import current_user, login_required
from database.models import Favourites, Locations
from dogfriendly import db
from sqlalchemy import delete

api = Blueprint("api", __name__)


# API endpoint to get all locations
@api.route("/api/locations", methods=["GET"])
def get_locations():
    locations = Locations.query.all()
    favourite_ids = []
    if not current_user.is_anonymous:
        favourites = Favourites.query.filter_by(user_id=current_user.id).all()
        for fav in favourites:
            favourite_ids.append(fav.location_id)
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
                "saved": loc.id in favourite_ids
            }
            for loc in locations
        ]
    )

# API endpoint for favourites
@api.route("/api/locations/save")
def save_favourites():
    location = Locations.query.filter_by(name=request.args.get("id")).all()
    favourites = Favourites.query.filter_by(location_id=location[0].id, user_id=current_user.id).all()  
    if len(favourites) > 0:
        statement = Favourites.query.filter_by(location_id=location[0].id, user_id=current_user.id).delete()  
    else:
        statement = Favourites(location_id=location[0].id, user_id=current_user.id)
        db.session.add(statement)
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
    locations = Locations.query.filter(Locations.id.in_(location_ids)).all()
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
                "saved": True
            }
            for loc in locations
        ]
    )