class Event:
    end = None
    start = None
    summary = None
    location = None
    description = None

    def __init__(self, end, start, summary, location, description):
        self.end = end
        self.start = start
        self.summary = summary
        self.location = location
        self.description = description

    def get_clase(self):
        return {'end': self.end, 'start': self.start, 'summary': self.summary, 'location': self.location, 'description': self.description}
