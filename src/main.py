from schedule import Calendar
from peter_assistant import PeterAssistant
from flask import Flask, jsonify, request
# from event import Event

asistente = PeterAssistant()
asistente.greet()
calendario = Calendar()
# text = asistente.listen()
# print(text)

# if(text.count("clase") > 0 and text.count("próxima") > 0 ):
if True:
    calendario.startServices()
    if calendario.is_available():
       events = calendario.get_event(
            calendario.today, calendario.service
        )
    else:
        print("Lo siento, no he podido obtener tus eventos")

  
else:
    
    print("Disculpa no te he entendido, por favor repite")

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify(events)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')