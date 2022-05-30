

# from app.schedule import Calendar
# from app.shower import Shower
from shower import Shower
from schedule import Calendar


class PeterAssistant:
    calendario = None
    shower = None

    def __init__(self):
        self.calendario = Calendar()
        self.shower = Shower()
        pass

    def init_service():
        pass

    def get_event(self, events):
        return self.calendario.get_event(events)

    def get_destination(self, data):
        return self.shower.get_destination(data)

    def get_location(self, args):
        return self.shower.get_location(args)

    def post_location(self, data):
        return self.shower.post_location(data)

    def show_block():
        pass

    def get_indications():
        pass
