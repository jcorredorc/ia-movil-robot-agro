import cv2

img1 = cv2.imread('9.jpg',0)
img2 = cv2.imread('10.jpg',0)
print(img1.shape)
print(img2.shape)

img_AND = cv2.bitwise_and(img1, img2)
img_OR = cv2.bitwise_or(img1, img2)
img_XOR = cv2.bitwise_xor(img1, img2)
img_NOT = cv2.bitwise_not(img2)

cv2.imshow('Imagen 1', img1)
cv2.imshow('Imagen 2', img2)
cv2.imshow('Operacion AND', img_AND)
cv2.imshow('Operacion OR', img_OR)
cv2.imshow('Operacion XOR', img_XOR)
cv2.imshow('Operacion NOT', img_NOT)

k = cv2.waitKey(0)

if k: # Si se pulsa cualquier tecla
    # Destruir todas las ventanas creadas
    cv2.destroyAllWindows()
