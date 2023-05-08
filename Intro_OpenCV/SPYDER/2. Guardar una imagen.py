# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 07:25:11 2023

@author: Julian Rene Chaux
"""

import cv2

# Cargar una imagen a escala de grises
img = cv2.imread('1.jpg', 0)    #O utilizar la bandera o argumento cv2.IMREAD_GRAYSCALE

# Mostrar imagen en ventana
cv2.imshow('Imagen', img)

# Esperar indefinidamente hasta que se pulse una tecla
k = cv2.waitKey(0)

if k == 27: # Si se pulsa la tecla ESC, cerramos las ventanas
    # Destruir todas las ventanas creadas
    cv2.destroyAllWindows()
elif k == ord('s'): #Si se pulsa la tecla 's', guardamos y salimos
    cv2.imwrite('San Agustin.png', img)
    # Destruir todas las ventanas creadas
    cv2.destroyAllWindows()