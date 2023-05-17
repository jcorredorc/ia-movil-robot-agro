import cv2
import numpy as np

dir = "Intro_OpenCV/tratamiento_imagenes/detector_objetos/"
# Cargamos el archivo xml del detector seleccionado
body_classifier = cv2.CascadeClassifier(dir + "Haarcascades/haarcascade_fullbody.xml")

# Creamos el objeto de video
captura = cv2.VideoCapture(dir + "Personas.avi")
# captura = cv2.VideoCapture(0)

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
    # PASO_2: DETECCIÓN DE PEATONES
    bodies = body_classifier.detectMultiScale(gris, 1.2, 3)
    if bodies is ():
        continue
    # ----------------------------------------------

    # ----------------------------------------------
    # PASO_3: DIBUJAR RECTÁNGULO DELIMITADOR
    for x, y, w, h in bodies:
        cv2.rectangle(imagen, (x, y), (x + w, y + h), (0, 255, 255), 2)
    # ----------------------------------------------

    # Mostramos imagen
    cv2.imshow("Video", imagen)

    # Capturamos teclado
    tecla = cv2.waitKey(25) & 0xFF
    # Salimos si la tecla presionada es ESC
    if tecla == 27:
        break

captura.release()
cv2.destroyAllWindows()
