#!/usr/bin/python3
from flask import Blueprint

app_views = Blueprint('app_views', __name__)
app_views.route('/api/v1/example', methods=['GET'])
def example_route():
return "Hello"


