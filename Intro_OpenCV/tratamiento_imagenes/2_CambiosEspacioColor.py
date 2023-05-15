import cv2

dir = "Intro_OpenCV/tratamiento_imagenes/"

img = cv2.imread(dir + "1.jpg", 1)  # Imagen a color
escala_grises = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imshow("Color", img)
cv2.imshow("Escala de Grises", escala_grises)
cv2.imshow("Espacio de Color HSV", img_HSV)

cv2.waitKey(0)
cv2.destroyAllWindows()
