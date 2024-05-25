from flask import request, jsonify, Blueprint
from database.models import Locations
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
                "outdoorspace": loc.outdoorspace
            }
            for loc in locations
        ]
    )


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
        hours=data["hours"],
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

def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'address': self.address,
            'category': self.category
        }

@api.route("/api/locations/search", methods=["GET"])
def search_locations():
    query = request.args.get("q", "")
    if query:
        results = Locations.query.filter(Locations.name.ilike(f"%{query}%")).all()
    else:
        results = []
    return jsonify([loc.serialize() for loc in results])


#@api.route("/api/locations/favorites", methods=["GET"])
#@login_required
#def get_favorite_locations():
 #   user_id = current_user.id
  #  favorite_locations = Locations.query.join(Favorites).filter(Favorites.user_id == user_id).all()
    
   # results = []
    #for location in favorite_locations:
     #   results.append({
      #      "id": location.id,
       #     "name": location.name,
        #    "address": location.address,
         #   "category": location.category,
            # Include any other fields you want to send back
       # })
    
  #  return jsonify(results)


# API endpoint to save locations to profiles
#@api.route("/api/locations/save", methods=["POST"])
#def save_locations():
