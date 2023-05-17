"""
PROCESO

1. Deteccion de maximo contorno
2. Registro en carpeta local
3. Envio de imagen a gmail cada 50 movimientos
"""

import numpy as np
import cv2
import time
import os
import datetime
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import datetime


#-------------------------------------------------
path = 'C:/Registros/'
camara = cv2.VideoCapture('12.mp4')
#camara = cv2.VideoCapture(0)
frame_width = int(camara.get(3))
frame_height = int(camara.get(4))
out = cv2.VideoWriter('salida_0.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 15, (frame_width,frame_height))

fondo = None
movimientos = 0
# Recorremos todos los frames
while True:
        # Obtenemos el frame
        (grabbed, frame) = camara.read()
 
        # Si hemos llegado al final del vídeo salimos
        if not grabbed:
                break
 
        # Convertimos a escala de grises
        gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
 
        # Aplicamos suavizado para eliminar ruido
        gris = cv2.GaussianBlur(gris, (7, 7), 0)
 
        # Si todavía no hemos obtenido el fondo, lo obtenemos
        # Será el primer frame que obtengamos
        if fondo is None:
                fondo = gris
                continue
 
        # Calculo de la diferencia entre el fondo y el frame actual
        resta = cv2.absdiff(fondo, gris)
 
        # Aplicamos un umbral
        umbral = cv2.threshold(resta, 30, 255, cv2.THRESH_BINARY)[1]
 
        # Dilatamos el umbral para tapar agujeros
        umbral = cv2.erode(umbral,  None, iterations=2)
        umbral = cv2.dilate(umbral, None, iterations=25)

        copia_frame = frame.copy()
        img_fg = cv2.bitwise_and(copia_frame,copia_frame,mask = umbral)
 
        # Copiamos el umbral para detectar los contornos
        contornosimg = umbral.copy()
        
        # Buscamos contorno en la imagen
        contornos, hierarchy = cv2.findContours(contornosimg,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        frame_copy = frame.copy()
        # Recorremos todos los contornos encontrados
        if len(contornos) > 0:
                c = max(contornos, key=cv2.contourArea)
                if cv2.contourArea(c) < 8800:
                        continue
 
                # Obtenemos el bounds del contorno, el rectángulo mayor que engloba al contorno
                (x, y, w, h) = cv2.boundingRect(c)
                # Dibujamos el rectángulo del bounds
                cv2.rectangle(frame, (x, y), (x + w, y + h), (7, 223, 235), 7)#(6, 1, 205)
                cv2.drawContours(frame, [c], -1, (0, 0, 255), 1, cv2.LINE_AA)
                # efecto translucido
                
                roi_1 = frame_copy[y:y+h,x:x+w]
                cv2.rectangle(frame, (x, y), (x + w, y + h),(159, 173, 33), -1,1)  #(184, 169, 165), -1,1)
                roi = frame[y:y+h,x:x+w]
                dst = cv2.addWeighted(roi,0.4,roi_1,0.6,0)
                frame[y:y+h,x:x+w] = dst

                # --- definir formato para guardar 18h5m12s
                ahora = datetime.datetime.now()
                hora = str(ahora.hour)
                minuto = str(ahora.minute)
                segundo = str(ahora.second)
                filename = hora+'h-'+minuto+'m-'+segundo+'s'+'.jpg'
                cv2.imwrite(os.path.join(path , filename), frame_copy)
                movimientos = movimientos + 1

                if movimientos == 50: # envio a gmail
                        movimientos = 0
                        #-------------------------------------------------
                        server = smtplib.SMTP('smtp.gmail.com:587')
                        msg = MIMEMultipart()
                        password = "laplace9216"
                        msg['From'] = "carlosjulioph@gmail.com"
                        msg['To'] = "visionporcomputador.curso@gmail.com"
                        time_now = datetime.datetime.now().isoformat()
                        msg['Subject'] = "ALERTA DE SEGURIDAD_" + time_now[0:10]
                        path_file =path+filename 
                        fp = open(path_file, 'rb')
                        #fp = open("C:/fakes.png", 'rb')
                        msg.attach(MIMEImage(fp.read()))
                        server.starttls()
                        server.login(msg['From'], password)
                        server.sendmail(msg['From'], msg['To'], msg.as_string())
                        server.quit()
                
        out.write(frame)
 
        # Mostramos las imágenes de la cámara, el umbral y la resta
        cv2.imshow('Curso_VISION POR COMPUTADOR - Ing. CARLOS JULIO PARDO', frame)
        """
        cv2.imshow('Umbral', umbral)
        cv2.imshow('Resta', resta)
        #cv2.imshow('Contorno', contornosimg)
        cv2.imshow('Segmentacion', img_fg)
        #cv2.imshow('Fondo', fondo)
        """
 
        # Capturamos una tecla para salir
        key = cv2.waitKey(25) & 0xFF
 
        
 
        # Si ha pulsado la letra s, salimos
        if key == 27:
                break
 
# Liberamos la cámara y cerramos todas las ventanas
camara.release()
out.release()
cv2.destroyAllWindows()

print('Numero de movimientos: ',movimientos )

