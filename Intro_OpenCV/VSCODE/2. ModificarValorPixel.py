import cv2

# img = cv2.imread('1.jpg')
dir = "Intro_OpenCV/VSCODE/"
img = cv2.imread(dir + "1.jpg")

# Acceder a valor de pixel en las coordenadas (x,y)=(50,100)
px = img[100, 50]
print(px)

# Modificar valor de pixel
img[100, 50] = [0, 0, 255]
px = img[100, 50]
print(px)

# Modificar Region de pixeles
img[0:100, 0:50] = [255, 0, 0]

# Mostramos imagen en ventana
cv2.imshow("Imagen", img)

k = cv2.waitKey(0)

# if k:  # Si se pulsa cualquier tecla
#     # Destruir todas las ventanas creadas
#     cv2.destroyAllWindows()

# print(cv2.getWindowProperty("Imagen", cv2.WND_PROP_VISIBLE))

# if cv2.getWindowProperty("Imagen", cv2.WND_PROP_VISIBLE) < 1:
#     print("ALL WINDOWS ARE CLOSED")
# # cv2.waitKey(1)


if not cv2.getWindowProperty("Imagen", cv2.WND_PROP_VISIBLE):
    print("Operation Cancelled")

if k:  # Key code for ESC
    cv2.destroyAllWindows()
