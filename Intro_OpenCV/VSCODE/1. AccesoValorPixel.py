
import cv2

img = cv2.imread('1.jpg')

# Acceder a valor de pixel en las coordenadas (x,y)=(50,100)
px = img[100,50]
print(px)


# Acceder a Componente R de pixel en las coordenadas (x,y)=(50,100)
pxR = img[100,50,2]
print(pxR)
# Acceder a Componente G de pixel en las coordenadas (x,y)=(50,100)
pxG = img[100,50,1]
print(pxG)
# Acceder a Componente B de pixel en las coordenadas (x,y)=(50,100)
pxB = img[100,50,0]
print(pxB)

#Mostramos imagen en ventana
cv2.imshow('Imagen',img)

k = cv2.waitKey(0)

if k: # Si se pulsa cualquier tecla
    # Destruir todas las ventanas creadas
    cv2.destroyAllWindows()


