import abc


class Services(abc.ABC):
    
    settings = [""]
    avalible = False

    def __init__(self):
        ...

    def is_available(self):
        ...

    def startServices():
        ...

    def endService(self):
        ...