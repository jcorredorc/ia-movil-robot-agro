import cv2
import numpy as np

img = cv2.imread('14.jpg',1)
gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

bordes = cv2.Canny(gris,10,200)

cv2.imshow('Imagen Original',img)
cv2.imshow('Imagen Escala de Grises',gris)
cv2.imshow('BORDES',bordes)

cv2.waitKey(0)
cv2.destroyAllWindows()
