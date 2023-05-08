import numpy as np
import cv2

# Creamos una imagen negra
#img = np.zeros((300,300,3), np.uint8) #filas,columnas - Alto,ancho
img = cv2.imread('3.jpg',1)

#Dibujamos un circulo en el centro de la imagen
# con un radio de 60 px
cv2.circle(img,(150,150), 60, (255,255,255), 3) #coord (x,y)

cv2.imshow('Formas', img)

k = cv2.waitKey(0)

if k: # Si se pulsa cualquier tecla
    # Destruir todas las ventanas creadas
    cv2.destroyAllWindows()


