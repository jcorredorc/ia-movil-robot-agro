import cv2

dir = "Intro_OpenCV/tratamiento_imagenes/"
img = cv2.imread(dir + "2.jpg", 1)
print(img.shape)

cv2.imshow("Imagen Original", img)
cv2.waitKey(0)

# Escalar-REDIMENSIONAR
# Si no se define el método de interpolación, se toma por defecto cv2.INTER_LINEAR
img_resize = cv2.resize(img, (1280, 960))
print(img_resize.shape)


cv2.imshow("Imagen Escalada", img_resize)

cv2.waitKey(0)
cv2.destroyAllWindows()
