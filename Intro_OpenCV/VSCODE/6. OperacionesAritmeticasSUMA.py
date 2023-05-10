import cv2

dir = "Intro_OpenCV/VSCODE/"


img1 = cv2.imread(dir + "5.jpg", 1)
img2 = cv2.imread(dir + "6.jpg", 1)

print(img1.shape)
print(img2.shape)

suma1 = img1 + img2

suma2 = cv2.add(img1, img2)

suma3 = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)

cv2.imshow("Suma Matrices", suma1)
cv2.imshow("Suma OpenCV", suma2)
cv2.imshow("Suma transparencia", suma3)


k = cv2.waitKey(0)

if k:  # Si se pulsa cualquier tecla
    # Destruir todas las ventanas creadas
    cv2.destroyAllWindows()
