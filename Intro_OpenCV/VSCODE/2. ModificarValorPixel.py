import cv2

img = cv2.imread('1.jpg')

# Acceder a valor de pixel en las coordenadas (x,y)=(50,100)
px = img[100,50]
print(px)

#Modificar valor de pixel
img[100,50] = [0,0,255]
px = img[100,50]
print(px)

#Modificar Region de pixeles
img[0:100,0:50] = [255,0,0]

#Mostramos imagen en ventana
cv2.imshow('Imagen',img)

k = cv2.waitKey(0)

if k: # Si se pulsa cualquier tecla
    # Destruir todas las ventanas creadas
    cv2.destroyAllWindows()


