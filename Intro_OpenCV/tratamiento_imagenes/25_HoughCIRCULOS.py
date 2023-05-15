import cv2
import numpy as np

imagen = cv2.imread('7.jpg',1)
img = imagen.copy()

gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

circulos = cv2.HoughCircles(gris, cv2.HOUGH_GRADIENT,1,20,param1=50,param2=50,minRadius=10,maxRadius=100)
print(circulos)

circulos = np.uint16(np.around(circulos))
print(circulos)

cv2.imshow('Imagen Original',imagen)

for i in circulos[0,:]:
    #Dibujar el círculo
    cv2.circle(img, (i[0], i[1]), i[2], (0,255,0), 2)
    #Dibujar el centro del círculo
    cv2.circle(img, (i[0], i[1]), 2, (0,0,255), 3)

    cv2.waitKey(0)
    cv2.imshow('Circulos Detectados',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
