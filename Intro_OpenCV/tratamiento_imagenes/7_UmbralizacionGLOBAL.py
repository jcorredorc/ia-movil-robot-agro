import cv2

dir = "Intro_OpenCV/tratamiento_imagenes/"
image = cv2.imread(dir + "7.jpg")

# Convertimos a escala de grises
grises = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Umbral experimental del paso anterior
umbral = 50

# Umbral Binario
# mayor a umbral se coloca como maxVal=255
# retVal, dst = cv2.threshold(grises, umbral, 255, cv2.THRESH_BINARY)

# Umbral Binario Invertido
#
# retVal, dst = cv2.threshold(grises, umbral, 255, cv2.THRESH_BINARY_INV)

# Umbral Truncar
# Si se cumple umbral (>=) se trunca a ese valor y si es menor lo deja con el original
# retVal, dst = cv2.threshold(grises, umbral, 255, cv2.THRESH_TRUNC)

# Umbral Ajustar a Cero
# Si <= umbral se pone 0, de lo contrario se coloca el original
# retVal, dst = cv2.threshold(grises, umbral, 255, cv2.THRESH_TOZERO)

# Umbral Ajustar a Cero Invertido
retVal, dst = cv2.threshold(grises, umbral, 255, cv2.THRESH_TOZERO_INV)

cv2.imshow("umbral", image)
cv2.imshow("grises", grises)
cv2.imshow("resultado", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
