import datetime
import os.path
import pickle
from pprint import pprint
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport import requests
import pytz
from services import Services


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
    
    def get_event(self, day, service):
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
            start = event['start'].get('dateTime')
            print(start, event['end'].get('dateTime'), event['summary'])
    def is_available(self):
        pass

    def startServices():
        pass

    def endService(self):
        pass
