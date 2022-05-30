

from src.app.schedule import Calendar
from src.app.shower import Shower
# from shower import Shower
# from schedule import Calendar


class PeterAssistant:
    calendario = None
    shower = None

    def __init__(self):
        self.calendario = Calendar()
        self.shower = Shower()
        pass

    def get_event(self, events):
        return self.calendario.get_event(events)

    def get_destination(self, data):
        return self.shower.get_destination(data)

    def get_location(self, args):
        return self.shower.get_location(args)

    def post_location(self, data):
        return self.shower.post_location(data)
