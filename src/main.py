
from schedule import Calendar
from peter_assistant import PeterAssistant
# from Event import Event


asistente = PeterAssistant()
asistente.greet()
text = asistente.listen()
calendario = Calendar()
service = calendario.getcalendarservices()    
calendario.get_event(calendario.today,service)


