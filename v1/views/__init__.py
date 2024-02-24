#!/usr/bin/python3

from flask import Blueprint
app_views = Blueprint('app_views', __name__, url_prefix="/api/v1")

app_views.route('/api/v1/example', methods=['GET'])
@app_views.route('/status')
def status_get():
    return jsonify({'status': 'OK'})

if __name__ == '__main__':
    app.run(debug=True)



