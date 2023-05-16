import cv2
import numpy as np

# Cargamos imagen original
dir = "Intro_OpenCV/tratamiento_imagenes/"
img = cv2.imread(dir + "16.png", 1)
img1 = img.copy()

# Convertimos la a escala de grises
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Usamos la umbralización binaria manual con un umbral de 40.  Usar histograma para ver el umbral.
# Umbral seleccionado: 40
# También puede utilizar el umbral óptimo OTSU
_, binary = cv2.threshold(gray, 40, 255, cv2.THRESH_BINARY)

cv2.imshow("Imagen Original", img)
cv2.imshow("Imagen Binaria Original", binary)

# Operaciones morfologicas
mask = cv2.erode(binary, None, iterations=4)
mask = cv2.dilate(mask, None, iterations=6)
cv2.imshow("Imagen Binaria Filtrada", mask)

# Buscamos contorno en la imagen
contornos, _ = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print("Numero de Contornos: ", len(contornos))


for c in contornos:
    # Rectángulo Recto
    x, y, w, h = cv2.boundingRect(c)
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.drawContours(img, [c], -1, (0, 0, 255), 2)
    cv2.imshow("Rectangulo RECTO", img)

    k = cv2.waitKey(0)

    # Rectángulo Rotado
    rect = cv2.minAreaRect(c)
    box = cv2.boxPoints(rect)
    box = np.intp(box)
    cv2.drawContours(img1, [box], 0, (255, 0, 0), 2)
    cv2.drawContours(img1, [c], -1, (0, 0, 255), 2)
    cv2.imshow("Rectangulo ROTADO", img1)

cv2.waitKey(0)
cv2.destroyAllWindows()
