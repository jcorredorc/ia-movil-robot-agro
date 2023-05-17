import cv2
import numpy as np
from matplotlib import pyplot as plt

# Cargamos imagen original
dir = "Intro_OpenCV/tratamiento_imagenes/Taller/"
img = cv2.imread(dir + "imagen.jpg", 1)
cv2.imshow("Imagen Original", img)
cv2.waitKey(0)

# Convertimos la a escala de grises
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


## histograma

# plt.subplot(2, 1, 1), plt.imshow(gray, cmap="gray")
# plt.title("Imagen Escala de Grises"), plt.xticks([]), plt.yticks([])

# plt.subplot(2, 1, 2), plt.hist(gray.ravel(), 256)
# plt.title("Histograma"), plt.xticks(np.arange(0, 255, step=25)), plt.yticks([])

# plt.xlabel("Valor de los pixels (Intensidad)")
# plt.ylabel("Cantidad de pixeles")
# plt.xlim(0, 260)

# plt.show()


# Usamos la umbralización binaria manual con un umbral.  Usar histograma para ver el umbral.
# Umbral seleccionado: 230
# También puede utilizar el umbral óptimo OTSU
retVal, binary = cv2.threshold(gray, 230, 255, cv2.THRESH_BINARY)
cv2.imshow("Imagen binaria", binary)
cv2.waitKey(0)

kernel = np.ones((3, 3), np.uint8)
# Operaciones morfologicas
mask = cv2.erode(binary, kernel, iterations=2)
mask = cv2.dilate(mask, kernel, iterations=3)
cv2.imshow("Imagen Binaria Filtrada", mask)
cv2.waitKey(0)

# 3. FILTRO GAUSSIANO
# gausiano = cv2.GaussianBlur(img, (3, 3), 50)
# gausiano1 = cv2.GaussianBlur(img, (5, 5), 50)
# gausiano2 = cv2.GaussianBlur(img, (7, 7), 50)
# gausiano3 = cv2.GaussianBlur(img, (11, 11), 50)

# bordes cany
# bordes = cv2.Canny(mask, 10, 200)

# cv2.imshow("Imagen Original", img)
# cv2.imshow("Imagen Escala de Grises", mask)
# cv2.imshow("BORDES", bordes)

# cv2.waitKey(0)

# Buscamos contorno en la imagen
# Usamos una copia de la imagen binaria umbralizada para no dañar la original
# Modo de contorno: cv2.RETR_EXTERNAL, Método de Aproximación: cv2.CHAIN_APPROX_SIMPLEZ
contornos, hierarchy = cv2.findContours(
    mask.copy(), cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE
)

print("Cantidad de contornos: ", len(contornos))
print("Cantidad de contornos: ", len(contornos[0]))


# Características del texto
ubicacion = (200, 200)
font = cv2.FONT_HERSHEY_SIMPLEX
tamañoLetra = 2
colorLetra = (0, 0, 0)
grosorLetra = 2
num_c = 0

# CALCULO DE AREA
for c in contornos:
    if cv2.contourArea(c) >= 10000 and cv2.contourArea(c) <= 160000:
        k = cv2.waitKey(0)
        num_c += 1
        # Momentos
        M = cv2.moments(c)

        # Cálculo de centroide
        cx = int(M["m10"] / M["m00"])
        cy = int(M["m01"] / M["m00"])
        print("Centroide: ", cx, cy)

        # calculo de Area
        # area = M["m00"]
        area1 = cv2.contourArea(c)
        # print("Area de Contorno: ", area)
        print("Area de Contorno1: ", area1)

        # Dibujar centroide
        cv2.circle(img, (cx, cy), 4, (0, 255, 0), -1)
        # cv2.circle(img,(cx,cy),5,(255,0,0),2)

        # Escribir texto
        cv2.putText(
            img,
            str(num_c),
            (cx - 20, cy - 30),
            font,
            tamañoLetra,
            colorLetra,
            grosorLetra,
        )
        cv2.putText(
            img,
            str(area1),
            (cx - 40, cy + 60),
            cv2.FONT_HERSHEY_PLAIN,
            tamañoLetra - 1,
            colorLetra,
            grosorLetra,
        )
        cv2.drawContours(img, [c], -1, (0, 0, 255), 2)
        cv2.imshow("Centroide", img)

cv2.waitKey(0)
cv2.imwrite(dir + "output_.jpg", img)

# cv2.imshow("Imagen Original", img)
# cv2.imshow("Imagen Binaria", mask)

# # Dibujar Contornos
# cv2.drawContours(img, contornos, -1, (0, 0, 255), 3, cv2.LINE_AA)
# cv2.imshow("Imagen Original con Contornos", img)

# cv2.waitKey(0)
cv2.destroyAllWindows()
