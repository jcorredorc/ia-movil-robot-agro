import numpy as np
import cv2

# Creamos una imagen negra
img = np.zeros((300,300,3), np.uint8) #filas,columnas - Alto,ancho
img[:,:,0] = 255
img[:,:,1] = 255
img[:,:,2] = 255

# Dibujamos un rectangulo con un grososr de 3 px
cv2.rectangle(img,(50,50),(250,200),(0,0,255),1) #coord (x,y)

cv2.imshow('Formas', img)

k = cv2.waitKey(0)

if k: # Si se pulsa cualquier tecla
    # Destruir todas las ventanas creadas
    cv2.destroyAllWindows()
