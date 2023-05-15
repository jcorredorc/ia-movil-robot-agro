import cv2
import numpy as np

dir = "Intro_OpenCV/tratamiento_imagenes/"
img = cv2.imread(dir + "11.png", 0)
kernel = np.ones((5, 5), np.uint8)
print(kernel)

# EROSION
# Si los pixeles adyacentes al centro del kernel son todos 0, se pone el centro en cero,
#
erosion1 = cv2.erode(img, kernel, iterations=1)
erosion2 = cv2.erode(img, kernel, iterations=3)

cv2.imshow("Imagen Original", img)
cv2.imshow("Imagen Erosionada Iteracion 1", erosion1)
cv2.imshow("Imagen Erosionada Iteracion 3", erosion2)

cv2.waitKey(0)
cv2.destroyAllWindows()
