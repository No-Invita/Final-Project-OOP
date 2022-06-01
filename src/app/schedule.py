import datetime
from src.app.event import Event
from src.app.services import Services
# from event import Event
# from services import Services


class Calendar(Services):
    # gets the current date and time
    def get_date(self):
        self.today = datetime.date.today()
        self.current_time = datetime.datetime.now().time()

        # processes the events and returns the ones that are happening today and have the right format
    def get_event(self, events):
        clases = []
        if not events:
            print('No tienes eventos por ahora')
        else:
            for event in events:
                if (event['start'] and event['end'] and event['summary'] and event['description']):
                    self.start = str(event['start'].get(
                        'dateTime', event['start'].get('date')).split('T')[1].split("-")[0])
                    self.end = str(event['end'].get('dateTime', event['end'].get(
                        'date')).split('T')[1].split("-")[0])
                    clase = Event(self.end, self.start, str(event['summary']), str(
                        event['location']), str(event['description']))

                    clases.append(clase.get_clase())

        return clases
