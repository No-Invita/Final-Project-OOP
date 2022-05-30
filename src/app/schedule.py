import datetime
# from services import Services
from src.app.services import Services


class Calendar(Services):

    scopes = ['https://www.googleapis.com/auth/calendar']
    credentials_file = 'credentials.json'
    result = ""

    def get_date(self):
        self.today = datetime.date.today()
        self.current_time = datetime.datetime.now().time()

    def get_event(self, events):
        clases = []
        if not events:
            print('No tienes eventos por ahora')
        else:
            for event in events:
                self.start = str(event['start'].get(
                    'dateTime', event['start'].get('date')).split('T')[1].split("-")[0])
                self.end = str(event['end'].get('dateTime', event['end'].get(
                    'date')).split('T')[1].split("-")[0])
                end_time = datetime.datetime.strptime(self.end, '%X').time()
                clase = {
                    'end': self.end,
                    'start': self.start,
                    'summary': str(event['summary']),
                    'location': str(event['location']),
                    'description': str(event['description']),
                }
                clases.append(clase)
                if self.current_time < end_time:
                    self.summary = event['summary']
                    print(self.start, self.end,
                          self.summary)

        return clases
