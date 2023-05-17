import cv2
import numpy as np

dir = "Intro_OpenCV/tratamiento_imagenes/detector_objetos/"
face_classifier = cv2.CascadeClassifier(
    dir + "Haarcascades/haarcascade_frontalface_default.xml"
)

# Creamos el objeto de video
captura = cv2.VideoCapture(0)

while True:
    # Capturamos frame a frame
    (grabbed, imagen) = captura.read()
    # Si hemos llegado al final del vi­deo salimos
    if not grabbed:
        break

    # ----------------------------------------------
    # PASO_1: CONVERSION A ESCALA DE GRISES
    gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    # ----------------------------------------------

    # ----------------------------------------------
    # PASO_2: DETECCIÓN DE ROSTROS
    faces = face_classifier.detectMultiScale(gris, 1.3, 5)
    if faces is ():
        continue
    # ----------------------------------------------

    # ----------------------------------------------
    # PASO_3: DIBUJAR RECTÁNGULO DELIMITADOR
    for x, y, w, h in faces:
        x = x - 50
        w = w + 50
        y = y - 50
        h = h + 50
        cv2.rectangle(imagen, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Mostramos imagen
    cv2.imshow("Video", imagen)

    # Capturamos teclado
    tecla = cv2.waitKey(25) & 0xFF
    # Salimos si la tecla presionada es ESC
    if tecla == 27:
        break

captura.release()
cv2.destroyAllWindows()
