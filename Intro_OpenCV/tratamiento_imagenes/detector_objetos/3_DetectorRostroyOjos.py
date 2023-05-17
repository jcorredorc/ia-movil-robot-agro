import numpy as np
import cv2

dir = "Intro_OpenCV/tratamiento_imagenes/detector_objetos/"
# Cargamos el archivo xml del detector seleccionado
face_classifier = cv2.CascadeClassifier(
    dir + "Haarcascades/haarcascade_frontalface_default.xml"
)
eye_classifier = cv2.CascadeClassifier(dir + "Haarcascades/haarcascade_eye.xml")

# Leemos la imagen
imagen = cv2.imread(dir + "3.jpg")

# Convertimos la imagen a escala de grises
gray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# El clasificador retorna el ROI de la cara detectada como un tupla de valores
# Esta está compuesta por la coordenada superior izquierda y la inferior derecha
faces = face_classifier.detectMultiScale(gray, 1.3, 5)

# Cuando no detecta caras o rostros, el clasificador returna una tupla vacía
if faces is ():
    print("No se encontraron rostros")

# Se itera a través del array de rostros detectados y se dibuja
# un rectángulo sobre cada una de ellas
for x, y, w, h in faces:
    cv2.rectangle(imagen, (x, y), (x + w, y + h), (127, 0, 255), 2)
    cv2.imshow("Deteccion de Rostros", imagen)

# Se itera a través del array de ojos detectados y se dibuja
# un rectángulo sobre cada una de ellos
eyes = eye_classifier.detectMultiScale(gray)
for ex, ey, ew, eh in eyes:
    cv2.rectangle(imagen, (ex, ey), (ex + ew, ey + eh), (255, 255, 0), 2)
    cv2.imshow("Deteccion de Rostro y Ojos", imagen)

# Cuando no detecta ojos, el clasificador returna una tupla vacía
if eyes is ():
    print("No se encontraron ojos")

cv2.waitKey(0)
cv2.destroyAllWindows()
