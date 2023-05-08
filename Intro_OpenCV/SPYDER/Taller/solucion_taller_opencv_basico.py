import cv2

user_video_imagen = int(
    input(
        "Si desea cargar una imagen digite 0, si desea cargar un video de la webcam digite 1: "
    )
)
user_save = input("Desea hacer una copia? S/N: ")


# ----------------------
#        Imagen
# ----------------------

if user_video_imagen == 0:
    if user_save == "N" or user_save == "n":
        img = cv2.imread(
            "/home/javier/git/ia-movil-robot-agro/Intro_OpenCV/SPYDER/Taller/images.jpeg",
            cv2.IMREAD_COLOR,
        )
        cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
        # Mostrar imagen en ventana
        cv2.imshow("Image", img)
        # Esperar indefinidamente hasta que se pulse una tecla
        k = cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif user_save == "s" or user_save == "S":
        img = cv2.imread(
            "Intro_OpenCV/SPYDER/Taller/images.jpeg",
            cv2.IMREAD_GRAYSCALE,
        )
        cv2.imwrite("Intro_OpenCV/SPYDER/Taller/images_copy.png", img)
        # Destruir todas las ventanas creadas
        cv2.destroyAllWindows()
# ----------------------
#         Video
# ----------------------
elif user_video_imagen == 1:
    # escojer entrada video
    captura = cv2.VideoCapture(0)
    if user_save == "N" or user_save == "n":
        print("oprima 'ESC' para salir")
        while True:
            # Capturamos frame a frame
            (grabbed, imagen) = captura.read()

            # Si hemos llegado al final del video, salimos
            if not grabbed:
                break

            # Mostramos la imagen
            cv2.imshow("Video", imagen)

            # Capturamos teclado y esperamos un tiempo 25 ms
            tecla = cv2.waitKey(1)

            # Salimos si la tecla presionada es ESC
            if tecla == 27:
                break

    elif user_save == "s" or user_save == "S":
        # Creamos el objeto VideoWriter
        salida = cv2.VideoWriter(
            "Intro_OpenCV/SPYDER/Taller/videoSalida.mp4",
            cv2.VideoWriter_fourcc(*"XVID"),
            20.0,
            (640, 480),
        )

        while True:
            # Capturamos frame a frame
            (grabbed, imagen) = captura.read()

            # Si hemos llegado al final del video, salimos
            if not grabbed:
                break

            # Mostramos la imagen
            cv2.imshow("Video en Vivo", imagen)

            # Guardamos los fotogramas
            salida.write(imagen)

            # Capturamos teclado y esperamos un tiempo 25 ms
            tecla = cv2.waitKey(1)

            # Salimos si la tecla presionada es ESC
            if tecla == 27:
                break
    # Liberamos objeto
    captura.release()

    # Liberamos objeto
    salida.release()

    # Destruimos ventanas
    cv2.destroyAllWindows()
