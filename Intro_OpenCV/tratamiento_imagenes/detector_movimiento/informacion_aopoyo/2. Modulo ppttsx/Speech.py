import pyttsx3
"""
MODULO PYTTSX
 es un paquete de Python que admite motores comunes
 de conversión de texto a voz en Mac OS X, Windows y Linux.

"""
engine = pyttsx3.init()
engine.say('Hola, Bienvenido al curso de Introduccion a la Vision Artificial')
engine.runAndWait()
