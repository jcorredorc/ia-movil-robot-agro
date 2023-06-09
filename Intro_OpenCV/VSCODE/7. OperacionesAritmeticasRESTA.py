import cv2

dir = "Intro_OpenCV/VSCODE/"

img1 = cv2.imread(dir + "7.jpg", 0)  # 0 --> escala grises
cv2.imshow("Imagen 1", cv2.imread(dir + "7.jpg", 1))

img2 = cv2.imread(dir + "8.jpg", 0)
cv2.imshow("Imagen 2", cv2.imread(dir + "8.jpg", 1))

# Resta de imagenes
resta = cv2.absdiff(img1, img2)

cv2.imshow("Resta", resta)

k = cv2.waitKey(0)

if k:  # Si se pulsa cualquier tecla
    # Destruir todas las ventanas creadas
    cv2.destroyAllWindows()
