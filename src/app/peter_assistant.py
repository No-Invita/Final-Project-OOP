import speech_recognition as sr
import pyttsx3

class PeterAssistant:
    
    voice_id = 'spanish-latin-am'
    listener = sr.Recognizer()
    
    engine = pyttsx3.init()
    voices = engine.getProperty('voices') # getting to know current volume level (min=0 and max=1)
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 150)
    
    def __init__(self):
        pass
    def greet(self):
        
        self.speak("Hola, Anyone")
        self.speak("¿Que puedo hacer por ti?")
        
    def listen(self):
        
        try:
            with sr.Microphone() as source:
                print("Speak now")
                voice = self.listener.listen(source)
                self.listener.energy_threshold = 4000
                self.listener.adjust_for_ambient_noise(source, duration = 1)
                command = self.listener.recognize_google(
                    voice, language='es-CO')
                command = command.lower()
                return command
        except:
            return "Sin conexion, por favor conectate a internet"
    
    def speak(self, speech):
        
        self.engine.say(speech)
        self.engine.runAndWait()
    
    def init_service():
        pass
    
    def show_block():
        pass
    
    def get_indications():
        pass