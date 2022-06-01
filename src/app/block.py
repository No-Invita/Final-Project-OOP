from src.app.services import Services
# from services import Services


class Block:

    name = ""
    latitude = ""
    longitude = ""
    description = ""

    def __init__(self, name, latitude, longitude, description) -> None:
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.description = description

        # Return a dictionary with the block's information:

    def get_block(self):
        return {'name': self.name, 'latitude': self.latitude, 'longitude': self.longitude, 'description': self.description}

        # Return a string with the block's information:
    def __str__(self):
        return str({'name': self.name, 'latitude': self.latitude, 'longitude': self.longitude, 'description': self.description})
