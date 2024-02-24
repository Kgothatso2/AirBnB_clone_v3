#!/usr/bin/python3

from api.v1.views import app_views
from flask import jsonify, Blueprint

@app_views.route('/status', methods=['GET'])
def get_status():
    """Return a JSON response with status OK."""
    return jsonify({"status": "OK"})
