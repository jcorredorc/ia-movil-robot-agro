#Importar librería cv2
import cv2

#Leer imagen
img = cv2.imread('12.jpg')
cv2.imshow('Original', img)

#Características del texto
texto = "SENA"
ubicacion = (200,200)
font = cv2.FONT_HERSHEY_SIMPLEX
tamañoLetra = 5
colorLetra = (0,255,0)
grosorLetra = 10

#Escribir texto
cv2.putText(img, texto, ubicacion, font, tamañoLetra, colorLetra, grosorLetra)

#Guardar imagen
cv2.imwrite('Salida.jpg', img)

#Mostrar imagen
cv2.imshow('imagen',img)

k = cv2.waitKey(0)

if k: # Si se pulsa cualquier tecla
    # Destruir todas las ventanas creadas
    cv2.destroyAllWindows()


