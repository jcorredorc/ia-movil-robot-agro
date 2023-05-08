# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 23:15:38 2023

@author: Julian Rene Chaux
"""

import cv2

#Creamos el objeto de video
captura = cv2.VideoCapture(0)

#Creamos el objeto VideoWriter
salida = cv2.VideoWriter('../videoSalida.mp4',cv2.VideoWriter_fourcc(*'XVID'),20.0,(640,480))

while True:
    #Capturamos frame a frame
    (grabbed, imagen) = captura.read()
    
    #Si hemos llegado al final del video, salimos
    if not grabbed:
        break
    
    #Mostramos la imagen
    cv2.imshow('Video en Vivo', imagen)
    
    #Guardamos los fotogramas
    salida.write(imagen)
    
    #Capturamos teclado y esperamos un tiempo 25 ms
    tecla = cv2.waitKey(1)
    
    #Salimos si la tecla presionada es ESC
    if tecla == 27:
        break
    
#Liberamos objeto
captura.release()

#Liberamos objeto
salida.release()

#Destruimos ventanas
cv2.destroyAllWindows()


