import cv2
import numpy as np

dir = "Intro_OpenCV/VSCODE/"


# Creamos el objeto de video desde un archivo
# captura = cv2.VideoCapture("video.mp4")

# Creamos el objeto de video desde una camara
captura = cv2.VideoCapture(0)

# width = captura.get(cv2.CAP_PROP_FRAME_WIDTH) #ID_3
# height = captura.get(cv2.CAP_PROP_FRAME_HEIGHT) #ID_4

w_video = captura.get(3)  # cv2.CAP_PROP_FRAME_WIDTH
h_video = captura.get(4)  # cv2.CAP_PROP_FRAME_HEIGHT
fps = captura.get(cv2.CAP_PROP_FPS)
print("Ancho del video", w_video)
print("Alto del video", h_video)
print("Fotogramas por segundos FPS", fps)

# Cargamos el logo
logo = cv2.imread(dir + "LogoVideo/logo.png", 1)
# cv2.imshow('Imagen', logo)
# Extraemos las caracter�sticas del logo

h_logo, w_logo, c_logo = logo.shape
print("Ancho del logo", h_logo)
print("Alto del logo", w_logo)
print("Canales del logo", c_logo)
# print logo.shape

while True:
    # Capturamos frame a frame
    (lectura, imagen_video) = captura.read()

    # Si hemos llegado al final del video salimos
    if not lectura:
        break

    # Extraemos las caracteristicas del video
    h_video, w_video, c_video = imagen_video.shape

    # Recortamos el video, del mismo tama�o del logo
    roi_1 = imagen_video[h_video - h_logo : h_video, w_video - w_logo : w_video]
    roi_2 = logo

    # sumamos el logo al pedazo de video recortado
    suma = cv2.addWeighted(roi_1, 1.0, roi_2, 1.0, 0)

    # Adicionamos el logo al video
    imagen_video[h_video - h_logo : h_video, w_video - w_logo : w_video] = suma

    # Mostramos la imagen
    cv2.imshow("Video", imagen_video)
    # cv2.imshow('Video Recortado',roi_1)

    # Capturamos teclado
    tecla = cv2.waitKey(1) & 0xFF

    # Salimos si la tecla presionada es ESC
    if tecla == 27:
        break

# Liberamos el objeto
captura.release()

# Destruimos ventanas
cv2.destroyAllWindows()
