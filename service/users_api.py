import os.path
import sys

from flask import Flask, jsonify

# Workaround for getting tests to run without module load errors
# TODO look into whether this is avoidable
file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)
from visitor_data.visitor_log import VisitorData

app = Flask(__name__)
visitors = VisitorData()


@app.route('/unique-users')
def get_unique_user_counts():
    count = visitors.get_unique_user_count()
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
