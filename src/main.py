
import time
from schedule import Calendar
from peter_assistant import PeterAssistant


asistente = PeterAssistant()
asistente.greet()
calendario = Calendar()
text = asistente.listen()
print(text)
if(text.count("clase") > 0 and text.count("próxima") > 0 ):
    calendario.startServices()
    calendario.is_available()
    
else:
    print("Disculpa no te he entendido, por favor repite")
#service = calendario.startServices()
#calendario.is_available()

# calendario.get_event(calendario.today, service)
# asistente.speak("Disculpa no te he entendido")
# asistente.speak(
#         "Puedo ayudarte a saber cual es tu proxima clase, solo debes pedirmelo")
