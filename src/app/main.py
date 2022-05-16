from src.app.schedule import Calendar
from src.app.peter_assistant import PeterAssistant
from flask import Flask, jsonify, request
from flask_cors import CORS
import json

# from event import Event

asistente = PeterAssistant()
calendario = Calendar()


calendario.startServices()
if calendario.is_available():
    events = calendario.get_event(
        calendario.today, calendario.service
    )
else:
    print("Lo siento, no he podido obtener tus eventos")


app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    if calendario.is_available():
        events = calendario.get_event(
            calendario.today, calendario.service
        )
    return jsonify(events)


@app.route('/location', methods=["POST"])
def get_location():
    print("haciendo post")
    print(request.json)

    with open('src/data/location.json', 'w') as location:
        location.write(str(request.json).replace("'", '"'))

    return jsonify({"response": "200"})


@app.route('/location')
def location():
    with open('src/data/location.json', 'r') as data:
        datas = json.load(data)
        print(datas)
        return jsonify({"response": "200", "location": (datas)})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
