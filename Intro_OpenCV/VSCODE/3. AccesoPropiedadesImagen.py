import cv2

img = cv2.imread('2.jpg',0)

print("La forma de Imagen es :", img.shape)
print("El tamaño total de pixeles es:",img.size)
print("El tipo de datos de imagen es:", img.dtype)

#Mostramos imagen en ventana
cv2.imshow('Imagen',img)

k = cv2.waitKey(0)

if k: # Si se pulsa cualquier tecla
    # Destruir todas las ventanas creadas
    cv2.destroyAllWindows()

