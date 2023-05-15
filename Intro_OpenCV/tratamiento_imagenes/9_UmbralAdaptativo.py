import cv2

dir = "Intro_OpenCV/tratamiento_imagenes/"
imagen = cv2.imread(dir + "9.jpg", 0)

# umbralizacion global con umbral de 140
ret, th = cv2.threshold(imagen, 140, 255, cv2.THRESH_BINARY)

# Umbralizacion adaptativo con método cv2.ADAPTIVE_THRESH_MEAN_C
th1 = cv2.adaptiveThreshold(
    imagen, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 15, 12
)  # tamaño bloque 15

cv2.waitKey(0)

# Umbralizacion adaptativo con método cv2.ADAPTIVE_THRESH_GAUSSIAN_C
th2 = cv2.adaptiveThreshold(
    imagen, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 12
)

cv2.imshow("umbral", imagen)
cv2.imshow("Global", th)
cv2.imshow("Adaptativo MEAN", th1)
cv2.imshow("Adptativo GAUSSIAN", th2)

cv2.waitKey(0)
cv2.destroyAllWindows()
