import cv2
import numpy as np

# Creamos el objeto de video
dir = "Intro_OpenCV/tratamiento_imagenes/detector_movimiento/SCRIPTS/"
captura = cv2.VideoCapture(dir + "video.mp4")

fondo = None

while True:
    # Capturamos frame a frame
    (grabbed, imagen) = captura.read()
    # Si hemos llegado al final del video salimos
    if not grabbed:
        break
    # ----------------------------------------------
    # PASO_1: CONVERSION A ESCALA DE GRISES Y SUAVIZAMOS
    gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

    # Aplicamos suavizado para eliminar ruido
    gris = cv2.GaussianBlur(gris, (7, 7), 0)
    # ----------------------------------------------

    # ----------------------------------------------
    # PASO_2: DEFINICION DE FONDO
    # Si todavía no hemos obtenido el fondo, lo obtenemos
    # Será el primer frame que obtengamos
    if fondo is None:
        fondo = gris
        cv2.imwrite("Fondo.jpg", fondo)
        continue
    cv2.imshow("Fondo", fondo)
    # ----------------------------------------------

    # Mostramos imagen
    cv2.imshow("Video", imagen)

    # Capturamos teclado
    tecla = cv2.waitKey(25) & 0xFF
    # Salimos si la tecla presionada es ESC
    if tecla == 27:
        break

# Liberamos objeto
captura.release()
# Destruimos ventanas
cv2.destroyAllWindows()
