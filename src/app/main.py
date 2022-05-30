import datetime
from src.app.schedule import Calendar
from src.app.peter_assistant import PeterAssistant
# from schedule import Calendar
# from peter_assistant import PeterAssistant
from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import csv


# from event import Event

asistente = PeterAssistant()


app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    pass


@app.route('/event', methods=['POST'])
def event():
    return jsonify(asistente.get_event(request.json['events']))


@ app.route('/destination')
def destination():
    return jsonify(asistente.get_destination(request.args))


@ app.route('/location', methods=["POST"])
def get_location():
    return jsonify(asistente.post_location(request.json))


@ app.route('/location')
def location():
    return jsonify(asistente.get_location(request.args))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
