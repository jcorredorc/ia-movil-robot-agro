import cv2
import numpy as np
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import datetime
import threading

"""
CONTROLADA POR 2 VARIABLES BOOLEANAS:

- ejecutar_hilo : controlar la ejecucion de hilo
- enviar: controlar la ejecucion de pyttsx o de twilio
"""

path = 'C:/Registros/'
filename = '20h-8m-59s.jpg'
path_file =path+filename

def enviar_msg():
        global enviar
        global ejecutar_hilo
        
        while (ejecutar_hilo == True):
                #print('Ejecutando hilo')
                
                
                if enviar == True: # envio de correo gmail

                        server = smtplib.SMTP('smtp.gmail.com:587')
                        server.starttls()
                        msg = MIMEMultipart()
                        
                        msg['From'] = "sistema.video.vigilancia00@gmail.com"
                        msg['To'] = "carlosjulioph@gmail.com"
                        time_now = datetime.datetime.now().isoformat()
                        msg['Subject'] = "Movimiento_" + filename
                        fp = open(path_file, 'rb')
                        msg.attach(MIMEImage(fp.read()))
                        
                        password = "laplace12"
                        server.login(msg['From'], password)
                        server.sendmail(msg['From'], msg['To'], msg.as_string())
                        server.quit()
                            
                        print('Correo enviado.....')
                        enviar = False

#----------------------------------------------------
#Creamos el objetto de video
captura = cv2.VideoCapture('video.mp4')

enviar =  False
ejecutar_hilo = True  # booleano para finalizar hilo
hilo1 = threading.Thread(target=enviar_msg)
hilo1.start()

while True:
        #Capturamos frame a frame
        (grabbed, imagen) = captura.read()
        # Si hemos llegado al final del vídeo salimos
        if not grabbed:
            break
        #imagen = cv2.resize(imagen,None,fx=0.5,fy=0.5)
        #Mostramos imagen  
        cv2.imshow('Video', imagen)
        #Capturamos teclado
        tecla = cv2.waitKey(25) & 0xFF
        #Salimos si la tecla presionada es ESC
        if tecla == ord('s'):
                enviar = True
                print('[INFO]Envio de correo...')
        if tecla == 27:
                 ejecutar_hilo = False
                 break
print('[INFO] Hilo finalizado!...')
#Liberamos objeto                                                  
captura.release()
#Destruimos ventanas
cv2.destroyAllWindows()

