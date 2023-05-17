"""
Es necesario habilitar el Acceso de aplicaciones poco seguras,
en la configuracion de la cuenta de gmail utilizada para envio

NOTA: el modulo smtplib no se instala
"""
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import datetime

path = 'C:/Registros/'
filename = '20h-8m-38s.jpg'
path_file =path+filename

# Creamos un objeto SMTP para la conexion al servidor
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()

# Creamo sun objeto de mensaje MIMEMultipart y adjuntamos los encabezados
msg = MIMEMultipart()

msg['From'] = "sistema.video.vigilancia00@gmail.com"
destinatarios = "carlosjulioph@gmail.com, visionporcomputador.curso@gmail.com"
#msg['To'] = "carlosjulioph@gmail.com"
msg['Subject'] = "Movimiento_" + filename

# Adjuntamos imagen
fp = open(path_file, 'rb')
msg.attach(MIMEImage(fp.read()))

# Ingresamos a la cuenta y enviamos mensaje
password = "laplace12"
server.login(msg['From'], password)
server.sendmail(msg['From'], destinatarios.split(','), msg.as_string())
#server.sendmail(msg['From'], msg['To'], msg.as_string())
server.quit()

