# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 23:57:02 2023

@author: Julian Rene Chaux
"""

import cv2


# Cargar una imagen a color
img = cv2.imread("photo1.jpg", cv2.IMREAD_COLOR)
# img = cv2.imread('1.jpg', -1)
# img = cv2.imread('1.jpg', cv2.IMREAD_GRAYSCALE)
# img = cv2.imread('1.jpg', 0)

cv2.namedWindow("Image", cv2.WINDOW_NORMAL)

# Mostrar imagen en ventana
cv2.imshow("Image", img)

# Esperar indefinidamente hasta que se pulse una tecla
cv2.waitKey(0)

# Destruir todas las ventanas creadas
cv2.destroyAllWindows()
