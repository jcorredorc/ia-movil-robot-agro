import cv2
import numpy as np

dir = "Intro_OpenCV/tratamiento_imagenes/"
img = cv2.imread(dir + "2.jpg", 1)
cv2.imshow("Imagen Original", img)

# ROTACION
filas, columnas, canales = img.shape

# Sin factor de escala
M = cv2.getRotationMatrix2D(
    (columnas / 2, filas / 2), 150, 1
)  # pto de rotación (centro), grados de rotacion (150), escala (1)
dst = cv2.warpAffine(img, M, (columnas, filas))
cv2.imshow("Imagen Rotada sin Escala", dst)

# Con factor de escala
M1 = cv2.getRotationMatrix2D((columnas / 2, filas / 2), 90, 0.5)
dst1 = cv2.warpAffine(img, M1, (columnas, filas))
cv2.imshow("Imagen Rotada con Escala", dst1)

# Guarda la imágenes transformadas
cv2.imwrite("ImagenRotada.jpg", dst1)

cv2.waitKey(0)
cv2.destroyAllWindows()
