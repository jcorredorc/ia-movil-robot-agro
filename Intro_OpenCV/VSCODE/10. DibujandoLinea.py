import numpy as np
import cv2

# Creamos una imagen negra
img = np.ones((300, 300, 3), np.uint8)  # filas,columnas - Alto,ancho

# Dibujamos una linea verde diagonal con un grosor de 5 px
cv2.line(img, (50, 0), (299, 499), (0, 255, 0), 5)

cv2.imshow("Formas", img)

k = cv2.waitKey(0)

if k:  # Si se pulsa cualquier tecla
    # Destruir todas las ventanas creadas
    cv2.destroyAllWindows()
