import cv2

dir = "Intro_OpenCV/tratamiento_imagenes/"

img = cv2.imread(dir + "4.jpg", 1)
print(img.shape)

# Especifica factor de escala
img_resize_1 = cv2.resize(img, None, fx=0.2, fy=0.2, interpolation=cv2.INTER_AREA)
print(img_resize_1.shape)
img_resize_2 = cv2.resize(img, None, fx=0.2, fy=0.2, interpolation=cv2.INTER_LINEAR)
print(img_resize_2.shape)
img_resize_3 = cv2.resize(img, None, fx=0.2, fy=0.2, interpolation=cv2.INTER_CUBIC)
print(img_resize_3.shape)
img_resize_4 = cv2.resize(img, (640, 480), interpolation=cv2.INTER_AREA)
print(img_resize_4.shape)

# Muestras las imágenes transformadas
cv2.imshow("Imagen Original", img)
cv2.imshow("INTER_AREA", img_resize_1)
cv2.imshow("INTER_LINEAR", img_resize_2)
cv2.imshow("INTER_CUBIC", img_resize_3)
cv2.imshow("INTER_AREA_MANUAL", img_resize_4)

# Guarda la imágenes transformadas
cv2.imwrite(dir + "inter_AREA.jpg", img_resize_1)
cv2.imwrite(dir + "inter_CUBIC.jpg", img_resize_3)
cv2.imwrite(dir + "inter_LINEAR.jpg", img_resize_2)

cv2.waitKey(0)
cv2.destroyAllWindows()
