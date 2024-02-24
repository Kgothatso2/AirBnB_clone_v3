#!/usr/bin/python3
"""
Implement error handling mechanisms to provide meaningful error messages and status codes.

"""
from models import storage
from api.v1.views import app_views
from flask import Flask, jsonify, Response

app = flask(__name__)
app.register_blueprint(app_views)
@app.teardown_appcontext
def close_storage(exception):
    """Close the storage connection after each request."""
    if storage is not None:
        try:
            storage.close()
        except Exception as e:
            print(f"Error closing storage: {e}")

def create_app():
    app = Flask(__name__)
    app.teardown_appcontext(close_storage)

def create_app():
    app = Flask(__name__)
    app.teardown_appcontext(close_storage)
    return app

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000 threaded=True)

