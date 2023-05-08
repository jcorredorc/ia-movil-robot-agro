import cv2

#Creamos el objeto de video
#captura = cv2.VideoCapture(0)

captura = cv2.VideoCapture('rtsp://admin:12345@10.192.74.28:554/cam/realmonitor?channel=2&subtype=0')  #DVR channel=N
#captura = cv2.VideoCapture('rtsp://admin:admin123@192.168.1.108:554/cam/realmonitor?channel=2&subtype=0')   #Cámara Térmica

while True:
    #Capturamos frame a frame
    (grabbed, imagen) = captura.read()
    
    #Si hemos llegado al final del video, salimos
    if not grabbed:
        break
    
    #Mostramos la imagen
    cv2.imshow('Video', imagen)
    
    #Capturamos teclado y esperamos un tiempo 25 ms
    tecla = cv2.waitKey(1)
    
    #Salimos si la tecla presionada es ESC
    if tecla == 27:
        break
    
#Liberamos objeto
captura.release()

#Destruimos ventanas
cv2.destroyAllWindows()