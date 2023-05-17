import cv2
import numpy as np
import os
import datetime

# Creamos el objeto de video
dir = "Intro_OpenCV/tratamiento_imagenes/detector_movimiento/SCRIPTS/"
captura = cv2.VideoCapture(dir + "video.mp4")

fondo = None

while True:
    # Capturamos frame a frame
    (grabbed, imagen) = captura.read()
    # Si hemos llegado al final del vÃ­deo salimos
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

    # ----------------------------------------------
    # PASO_3: RESTA DE FRAME ACTUAL Y FONDO PREDEFINIDO
    resta = cv2.absdiff(gris, fondo)
    cv2.imshow("Resta", resta)
    # ----------------------------------------------

    # ----------------------------------------------
    # PASO_4: UMBRALIZACION
    _, MASCARA = cv2.threshold(resta, 100, 255, cv2.THRESH_BINARY)
    cv2.imshow("Mascara", MASCARA)

    # Dilatamos el umbral para tapar agujeros
    MASCARA = cv2.erode(MASCARA, None, iterations=2)
    MASCARA = cv2.dilate(MASCARA, None, iterations=25)
    cv2.imshow("MASCARA", MASCARA)
    # ----------------------------------------------

    # ----------------------------------------------
    # PASO_5: CONTEO DE PIXELES BLANCOS
    pixeles_blancos = cv2.countNonZero(MASCARA)
    print("Numero de pixeles blancos: ", pixeles_blancos)
    # ----------------------------------------------

    # ----------------------------------------------
    # PASO_6: REGISTRO LOCAL
    if pixeles_blancos > 2000:
        # print('ALERTA')
        # --- definir formato para guardar 18h-5m-12s
        ahora = datetime.datetime.now()
        hora = str(ahora.hour)
        minuto = str(ahora.minute)
        segundo = str(ahora.second)
        nombre_imagen = hora + "h-" + minuto + "m-" + segundo + "s" + ".jpg"
        cv2.imwrite(nombre_imagen, imagen)
    # ----------------------------------------------

    # ----------------------------------------------
    # PASO_7: BUSQUEDA DE CONTORNOS
    # Buscamos contorno en la imagen
    contornos, _ = cv2.findContours(MASCARA, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    print("Numero de contornos: ", contornos)
    # ----------------------------------------------

    # ----------------------------------------------
    # PASO_8: DIBUJO DE CONTORNOS
    for c in contornos:
        # Eliminamos los contornos más pequeños
        area = cv2.contourArea(c)
        if area < 5000:
            continue

        # Obtenemos el bounds del contorno, el rectángulo mayor que engloba al contorno
        (x, y, w, h) = cv2.boundingRect(c)
        # Dibujamos el rectángulo del bounds
        cv2.rectangle(imagen, (x, y), (x + w, y + h), (6, 1, 205), 7)
        # cv2.drawContours(imagen, [c], -1, (0, 255, 0), 2, cv2.LINE_AA)
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
