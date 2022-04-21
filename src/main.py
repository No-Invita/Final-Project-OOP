
from itertools import count
from schedule import Calendar
from peter_assistant import PeterAssistant
# from Event import Event


asistente = PeterAssistant()
asistente.greet()
text = asistente.listen()
str(text)
if(text.count("clase") > 0 ):
    calendario = Calendar()
    service = calendario.getcalendarservices()
    calendario.get_event(calendario.today, service)
else:
    asistente.speak("Disculpa no te he entendido")
    asistente.speak(
        "Puedo ayudarte a saber cual es tu proxima clase, solo debes pedirmelo")

print(text)
