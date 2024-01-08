#!/usr/bin/python3
""" Index view
"""
from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


@app_views.route("/status", strict_slashes=False)
def status_route():
    """ Status of the web server
    """
    return jsonify({"status": "OK"})
