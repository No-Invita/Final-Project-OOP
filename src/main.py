from schedule import Calendar
from peter_assistant import PeterAssistant
from event import Event

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

