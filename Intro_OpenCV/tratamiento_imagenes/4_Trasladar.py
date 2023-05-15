import cv2
import numpy as np

dir = "Intro_OpenCV/tratamiento_imagenes/"
img = cv2.imread(dir + "5.png", 1)
cv2.imshow("Imagen Original", img)

# TRASLACION - cantidad de filas, columnas y canales
print(img.shape)
filas, columnas, canales = img.shape

# Trasladar la imagén a la posición x = 100, y = 50
# M matriz de transformación
M = np.float32([[1, 0, 100], [0, 1, 50]])

dst = cv2.warpAffine(img, M, (columnas, filas))

cv2.imshow("Imagen Trasladada", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
