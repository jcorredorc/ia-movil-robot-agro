import cv2

image = cv2.imread('11.jpg',1)
mascara = cv2.imread('13.png',0)

print(image.shape)
print(mascara.shape)

bola = cv2.bitwise_and(image,image, mask= mascara)

cv2.imshow('Imagen', image)
cv2.imshow('Mascara', mascara)
cv2.imshow('Salida', bola)

k = cv2.waitKey(0)

if k: # Si se pulsa cualquier tecla
    # Destruir todas las ventanas creadas
    cv2.destroyAllWindows()
