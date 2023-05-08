import cv2

img = cv2.imread('4.png',1)

# Dividimos la imagen en sus canales
b , g , r  =  cv2.split(img)
cv2.imshow('Imagen', img)

# Mostramos cada plano
cv2.imshow('Canal ROJO', r)
cv2.imshow('Canal VERDE', g)
cv2.imshow('Canal AZUL', b)

# Combinamos los 3 canalaes
img1 = cv2.merge((b,g,r))
cv2.imshow('Fusion Canales',img1)

# indexacion con numpy
#img[:,:,0] -> Canal Azul
#img[:,:,1] -> Canal Verde
#img[:,:,2] -> Canal Rojo

img[:,:,2] = 155 # asignar valor de 155 al canal rojo
cv2.imshow('Imagen Numpy', img)

b = img[:,:,0] # acceder al canal Azul
cv2.imshow('plano azul',b)

k = cv2.waitKey(0)

if k: # Si se pulsa cualquier tecla
    # Destruir todas las ventanas creadas
    cv2.destroyAllWindows()

