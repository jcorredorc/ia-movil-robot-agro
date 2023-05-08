# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 23:04:13 2023

@author: Julian Rene Chaux
"""

import cv2

#Creamos el objeto de video
#captura = cv2.VideoCapture("1. video.mp4")
#captura = cv2.VideoCapture("2. Intro.mp4")
captura = cv2.VideoCapture(4)

while True:
    #Capturamos frame a frame
    (grabbed, imagen) = captura.read()
    
    #Si hemos llegado al final del video, salimos
    if not grabbed:
        break
    
    #Mostramos la imagen
    cv2.imshow('Video', imagen)
    
    #Capturamos teclado y esperamos un tiempo 25 ms
    tecla = cv2.waitKey(1)
    
    #Salimos si la tecla presionada es ESC
    if tecla == 27:
        break
    
#Liberamos objeto
captura.release()

#Destruimos ventanas
cv2.destroyAllWindows()

