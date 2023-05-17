
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
   engine.setProperty('voice', voice.id)
   engine.say('Hola Carlos Julio, bienvenido')
   print (voice.id)
engine.runAndWait()

"""
#para definir una voz en particular
engine = pyttsx3.init()
voices = engine.getProperty('voices')
#indice para voz [0] - Español-SABINA  [1] - INGLES - ZIRA
engine.setProperty('voice', voices[0].id)
engine.say('Hola Carlos Julio')
engine.runAndWait()
"""
