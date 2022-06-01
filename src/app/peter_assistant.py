

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
        # executes Calendar method get_event()

    def get_event(self, events):
        return self.calendario.get_event(events)
        # executes Shower method get_destination()

    def get_destination(self, data):
        return self.shower.get_destination(data)
        # executes Shower method get_location()

    def get_location(self, args):
        return self.shower.get_location(args)

        # executes Shower method post_location()
    def post_location(self, data):
        return self.shower.post_location(data)
