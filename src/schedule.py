import datetime
import os.path
import pickle
from pprint import pprint
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport import requests
import pytz
from services import Services
import time


class Calendar(Services):

    scopes = ['https://www.googleapis.com/auth/calendar']
    credentials_file = 'credentials.json'

    def __init__(self):
        self.get_date()

    def getcalendarservices(self):

        creds = None
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(requests.Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    "credentials.json", scopes=self.scopes)
                creds = flow.run_local_server(port=0)

            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        service = build('calendar', 'v3', credentials=creds)

        return service

    def get_date(self):
        self.today = datetime.date.today()
        self.current_time = datetime.datetime.now().time()

    def get_event(self, day, service, current):
        start_date = datetime.datetime.combine(
            day, datetime.datetime.min.time())
        end_date = datetime.datetime.combine(day, datetime.datetime.max.time())
        utc = pytz.UTC
        start_date = start_date.astimezone(utc)
        end_date = end_date.astimezone(utc)

        result = service.events().list(calendarId='primary', timeMin=start_date.isoformat(), timeMax=end_date.isoformat(),
                                       singleEvents=True,
                                       orderBy='startTime').execute()
        events = result.get('items', [])

        if not events:
            print('No tienes eventos por ahora')
        for event in events:
            start = str(event['start'].get(
                'dateTime', event['start'].get('date')).split('T')[1].split("-")[0])
            end = str(event['end'].get('dateTime', event['end'].get(
                'date')).split('T')[1].split("-")[0])
            end_time = datetime.datetime.strptime(end, '%X').time()
            if current < end_time:
                print(start, end, event['summary'])
                find = True
                break
            else:
                find = False

        if(not(find)):
            pprint('No tienes eventos por ahora')

    def is_available(self):
        if self.getcalendarservices != None:
            self.get_event(
                self.today, self.getcalendarservices(), self.current_time)
        else:
            pprint("Lo siento no he podido obtener tus eventos")

    def startServices(self):
        self.getcalendarservices()

    def endService(self):
        pass
