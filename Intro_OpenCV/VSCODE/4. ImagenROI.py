import cv2

img = cv2.imread('3.jpg',-1)

cv2.imshow('Imagen', img)

# Definimos imagen ROI
y0 = 12
y1 = 100
x0 = 180
x1 = 350

ROI = img[y0:y1,x0:x1]  # y,x

print(ROI.shape)


# Mostramos imagen ROI
cv2.imshow('ROI', ROI)

k = cv2.waitKey(0)

if k: # Si se pulsa cualquier tecla
    # Destruir todas las ventanas creadas
    cv2.destroyAllWindows()

