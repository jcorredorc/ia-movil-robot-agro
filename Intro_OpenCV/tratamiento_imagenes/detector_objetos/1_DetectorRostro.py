import numpy as np
import cv2

dir = "Intro_OpenCV/tratamiento_imagenes/detector_objetos/"

# Cargamos el archivo xml del detector seleccionado
face_classifier = cv2.CascadeClassifier(
    dir + "Haarcascades/haarcascade_frontalface_default.xml"
)

# Leemos la imagen
image = cv2.imread(dir + "1.jpg")

# Convertimos la imagen a escala de grises
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# El clasificador retorna el ROI de la cara detectada como un tupla de valores
# Esta está compuesta por la coordenada superior izquierda y la inferior derecha
faces = face_classifier.detectMultiScale(gray, 1.3, 5)

# Cuando no detecta caras o rostros, el clasificador returna una tupla vacía
if faces is ():
    print("No se encontraron rostros")

# Se itera a través del array de caras detectadas y se dibuja
# un rectángulo sobre cada una de ellas
for x, y, w, h in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (127, 0, 255), 2)
    cv2.imshow("Face Detection", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
