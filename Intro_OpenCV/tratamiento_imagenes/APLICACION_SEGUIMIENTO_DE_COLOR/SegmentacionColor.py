import cv2
import numpy as np
 
#Iniciamos la camara
captura = cv2.VideoCapture(1)
#captura = cv2.VideoCapture("perro.mp4")

# **********************************************************************************
# VERDES
# ********************************************************************************** 
verde_bajos = np.array([49,50,50], dtype=np.uint8)
verde_altos = np.array([80, 255, 255], dtype=np.uint8)
# **********************************************************************************
# AZULES
# ********************************************************************************** 
#azul_bajos = np.array([100,100,20], dtype=np.uint8)
#azul_altos = np.array([125, 255, 255], dtype=np.uint8)
# **********************************************************************************
# AMARILLOS
# ********************************************************************************** 
#amarillo_bajos = np.array([15,100,20], dtype=np.uint8)
#amarillo_altos = np.array([45, 255, 255], dtype=np.uint8)
# **********************************************************************************
# ROJOS
# ********************************************************************************** 
#rojo_bajos_1 = np.array([0,100,20], dtype=np.uint8)
#rojo_altos_1 = np.array([5, 255, 255], dtype=np.uint8)
#rojo_bajos_2 = np.array([175,100,20], dtype=np.uint8)
#rojo_altos_2 = np.array([179, 255, 255], dtype=np.uint8)
 
while True:
     
        #Capturamos una imagen y la convertimos de RGB -> HSV
        #_, imagen = captura.read()
        (grabbed, imagen) = captura.read()
 
        # Si hemos llegado al final del video salimos
        if not grabbed:
            break

        hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)

        #Crear una mascara con solo los pixeles dentro del rango de verdes
        mask = cv2.inRange(hsv, verde_bajos, verde_altos)
        #mask = cv2.inRange(hsv, azul_bajos, azul_altos)
        #mask = cv2.inRange(hsv, amarillo_bajos, amarillo_altos)
        #maskRojo1 = cv2.inRange(hsv,rojo_bajos_1,rojo_altos_1)
        #maskRojo2 = cv2.inRange(hsv,rojo_bajos_2,rojo_altos_2)
        #mask = cv2.add(maskRojo1,maskRojo2)        

        #Dilatacion y Erosion
        mask = cv2.erode(mask,  None, iterations=2)
        mask = cv2.dilate(mask, None, iterations=2)
        contornosimg = mask.copy()

        # Buscamos contorno en la imagen
        contornos, _ = cv2.findContours(contornosimg,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        for c in contornos:
            moments = cv2.moments(c)
            area = moments['m00']
            # Eliminamos los contornos más pequeños
            if cv2.contourArea(c) < 200:
                 continue
 
            # Obtenemos el bounds del contorno, el rectángulo mayor que engloba al contorno
            #(x, y, w, h) = cv2.boundingRect(c)
            # Dibujamos el rectángulo del bounds
            #cv2.rectangle(imagen, (x, y), (x + w, y + h), (0, 0, 255), 2)
            #Determinamos las coordenadas del Centro
            x = int(moments['m10']/moments['m00'])
            y = int(moments['m01']/moments['m00'])
         
            #Mostramos sus coordenadas por pantalla
            print("x = ", x)
            print("y = ", y)
 
            #Dibujamos una marca en el centro del objeto
            #cv2.rectangle(imagen, (x, y), (x+2, y+2),(0,0,255), 2)

            # Escribimos el centro
            cv2.putText(imagen, f"({str(x)}, {str(y)})", (int(x),int(y-10)), cv2.FONT_HERSHEY_SIMPLEX, 1, (11,255,35), 1)

            # Dibujar centroide
            cv2.circle(imagen,(x,y),4,(0,255,0),-1)
            cv2.circle(imagen,(x,y),5,(255,0,0),2)
            cv2.drawContours(imagen, [c],-1,(0, 0, 255), 2)     
     
        #Mostramos la imagen original con la marca del centro y
  
        cv2.imshow('mask', mask)
        cv2.imshow('Camara', imagen)
        tecla = cv2.waitKey(5) & 0xFF
       
        if tecla == 27:
                 break
                                                  
captura.release() 
cv2.destroyAllWindows()
