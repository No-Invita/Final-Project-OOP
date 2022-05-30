from src.app.services import Services
# from services import Services


class Block:

    name = ""
    latitude = ""
    longitude = ""
    description = ""
    pictures = [""]

    def __init__(self, name, latitude, longitude, description) -> None:
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.description = description

    def dispaly(self, info) -> str:
        pass

    def get_location() -> list:
        pass

    def get_block(self):
        return {'name': self.name, 'latitude': self.latitude, 'longitude': self.longitude, 'description': self.description}

    def __str__(self):
        return str({'name': self.name, 'latitude': self.latitude, 'longitude': self.longitude, 'description': self.description})
