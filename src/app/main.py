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


@app.route('/destination')
def getdestination():
    print(request.json)
    data = request.json
    place = data['destination']
    id = ''
    go = ''
    cords = {}
    if 'bloq' in place.lower():
        print('no es el bloque i')
        id = place[len(place)-1]
        if 'bloqj1' == place.lower():
            print('es el bloque j')
            id = place[len(place) - 2]
    else:
        print('es el bloque i')
        id = place[len(place)-2] + place[len(place)-1]
    with open('src/resources/data/csvfile.csv', newline='') as File:
        reader = csv.reader(File)
        for row in reader:
            if ("Bloque " + id).lower() in row[0].lower():
                print(row)
                cords.update({"latitude": row[1], "longitude": row[2]})
                go = row

    return jsonify({"response": "200", "message": "Quieres ir al bloque " + id, "bloque": go, "cords": cords})


@ app.route('/destination', methods=['POST'])
def destination():
    print("haciendo post")
    print(request.json)
    data = request.json
    place = data['destination']
    id = ''
    go = ''
    cords = {}
    destination = ''
    if 'bloq' in place.lower():
        print('no es el bloque i')
        id = place[len(place)-1]
        if 'bloqj1' == place.lower():
            print('es el bloque j')
            id = place[len(place) - 2]

    else:
        print('es el bloque i')
        id = place[len(place)-2] + place[len(place)-1]
    print(id)
    with open('src/resources/data/csvfile.csv', newline='') as File:
        reader = csv.reader(File)
        for row in reader:
            if ("Bloque " + id).lower() in row[0].lower():
                print(row)
                cords.update({"latitude": row[1], "longitude": row[2]})
                go = row
    with open('src/data/destination.json', 'w') as destination:
        json.dump(cords, destination)
    return jsonify({"response": "200", "message": "Quieres ir al bloque " + id, "bloque": go, "cords": cords})


@ app.route('/location', methods=["POST"])
def get_location():
    print("haciendo post")
    print(request.json)

    with open('src/data/location.json', 'w') as location:
        location.write(str(request.json).replace("'", '"'))

    return jsonify({"response": "200"})


@ app.route('/location')
def location():
    start = ''
    end = ''
    with open('src/data/location.json', 'r') as data:
        start = json.load(data)
    with open('src/data/destination.json', 'r')as destination:
        end = json.load(destination)

    return jsonify({"response": "200", "location": (start), "destination": (end)})


@app.route('/x', methods=['POST'])
def x():
    print(request.json)
    return jsonify({"response": "200"})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
