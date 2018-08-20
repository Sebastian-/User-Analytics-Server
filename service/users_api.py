import os.path
import sys

from flask import Flask, jsonify, request

# Workaround for getting tests to run without module load errors
# TODO look into whether this is avoidable
file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)
from visitor_data.visitor_log import VisitorData

app = Flask(__name__)
visitors = VisitorData()


@app.route('/unique-users')
def unique_user_counts():
    osQuery = request.args.get('os').split(',') if request.args.get('os') else []
    deviceQuery = request.args.get('device').split(',') if request.args.get('device') else []

    count = visitors.get_unique_users_count(osQuery, deviceQuery)
    return jsonify({
        'count': count
        })


@app.route('/ping')
def ping():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
        })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
