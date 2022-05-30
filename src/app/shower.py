import csv
import json
from src.app.block import Block
from src.app.services import Services
# from block import Block
# from services import Services


class Shower (Services):

    events = [""]
    blocks = []

    def __init__(self):
        with open('src/resources/data/csvfile.csv', newline='') as File:
            reader = csv.reader(File)
            for row in reader:
                block = Block(row[0], row[1], row[2], row[3])
                self.blocks.append(block)
            print(self.blocks[1].get_block()['name'])

    def render(self):
        pass

    def display_events(self):
        pass

    def dispaly_blocks():
        pass

    def get_destination(self, data):
        p = data['id']
        place = data['destination']
        id = ''
        go = ''
        cords = {}
        destination = ''
        if 'bloq' in place.lower():
            print('no es el bloque i')
            id = place[len(place)-1]
            if 'bloqj1' == place.lower() or 'bloqg' in place.lower():
                print('es el bloque j')
                id = place[len(place) - 2]
        else:
            print('es el bloque i')
            id = place[len(place)-2] + place[len(place)-1]
        print(id)
        for row in self.blocks:
            if ("Bloque " + id).lower() in row.name.lower():
                print(row)
                cords.update(
                    {"latitude": row.latitude, "longitude": row.longitude})
                go = row
        with open(f'src/data/{p}destination.json', 'w') as destination:
            json.dump(cords, destination)
        return {"response": "200", "message": "Quieres ir al bloque " + id, "bloque": go.get_block(), "cords": cords}

    def get_location(self, args):
        id = args['id']
        start = ''
        end = ''
        with open('src/data/location.json', 'r') as data:
            start = json.load(data)
        with open(f'src/data/{id}destination.json', 'r')as destination:
            end = json.load(destination)
        return {"response": "200", "location": (start), "destination": (end)}

    def post_location(self, data):
        with open('src/data/location.json', 'w') as location:
            location.write(str(data).replace("'", '"'))
        return {"response": "200"}
