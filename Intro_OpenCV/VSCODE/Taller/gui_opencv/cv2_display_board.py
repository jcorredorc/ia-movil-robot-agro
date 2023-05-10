import cv2
import numpy as np

item = 0
board = [[0 for x in range(3)] for y in range(3)]
# print(board)
for r in range(3):
    for c in range(3):
        item += 1
        board[r][c] = item

print(board)


board[0][0] = "X"
board[0][1] = "O"
board[0][2] = "X"
board[1][0] = "X"
board[1][1] = "X"
board[1][2] = "O"
board[2][0] = "O"
board[2][1] = "X"
board[2][2] = "X"

coord_texto = [
    (31, 70),
    (31, 170),
    (31, 270),
    (131, 70),
    (131, 170),
    (131, 270),
    (231, 70),
    (231, 170),
    (231, 270),
]

dic_board = [
    {"texto": board[0][1], "coord": coord_texto[1]},
    {"texto": board[0][0], "coord": coord_texto[0]},
    {"texto": board[0][2], "coord": coord_texto[2]},
    {"texto": board[1][0], "coord": coord_texto[3]},
    {"texto": board[1][1], "coord": coord_texto[4]},
    {"texto": board[1][2], "coord": coord_texto[5]},
    {"texto": board[2][0], "coord": coord_texto[6]},
    {"texto": board[2][1], "coord": coord_texto[7]},
    {"texto": board[2][2], "coord": coord_texto[8]},
]
print(board)


# Creamos una imagen negra
img = np.zeros((300, 300, 3), np.uint8)  # filas,columnas - Alto,ancho
img[:, :, 0] = 197  # B
img[:, :, 1] = 220  # G
img[:, :, 2] = 69  # R

# Dibujamos un rectangulo con un grososr de 10 px
cv2.rectangle(img, (0, 0), (300, 300), (0, 0, 0), 10)  # coord (x,y)
# Dibujamos lineas del triqui con un grosor de 4 px
cv2.line(img, (100, 0), (100, 300), (0, 0, 0), 4)
cv2.line(img, (200, 0), (200, 300), (0, 0, 0), 4)
cv2.line(img, (0, 100), (300, 100), (0, 0, 0), 4)
cv2.line(img, (0, 200), (300, 200), (0, 0, 0), 4)


# Características del texto
texto = "X"
ubicacion = (31, 70)
font = cv2.FONT_HERSHEY_SIMPLEX
tamañoLetra = 2
colorLetra = (0, 0, 0)
grosorLetra = 2

# for borde_x in range(0, 400, 100):
#     for borde_y in range(0, 400, 100):
#         # texto = board[borde_x][borde_y]
#         print((borde_x + 31, borde_y + 70))
#         # Escribir texto
#         cv2.putText(
#             img,
#             texto,
#             (borde_x + 31, borde_y + 70),
#             font,
#             tamañoLetra,
#             colorLetra,
#             grosorLetra,
#         )

for casilla in dic_board:
    cv2.putText(
        img,
        casilla.get("texto"),  # texto
        casilla.get("coord"),  # ubicacion
        font,
        tamañoLetra,
        colorLetra,
        grosorLetra,
    )


cv2.imshow("Tablero", img)


# # row1
# cv2.line(img, (0, 50), (300, 50), (0, 0, 250), 4)
# # row2
# cv2.line(img, (0, 150), (300, 150), (0, 0, 250), 4)
# # row3
# cv2.line(img, (0, 250), (300, 250), (0, 0, 250), 4)
# # col1
# cv2.line(img, (50, 0), (50, 300), (0, 0, 250), 4)
# # col2
# cv2.line(img, (150, 0), (150, 300), (0, 0, 250), 4)
# # col3
# cv2.line(img, (2500, 0), (250, 300), (0, 0, 250), 4)
# # diag1
# cv2.line(img, (0, 0), (300, 300), (0, 0, 250), 4)
# # diag2
# cv2.line(img, (0, 300), (300, 0), (0, 0, 250), 4)


line_coord = [
    {"name": "row1", "coord": [(0, 50), (300, 50)]},
    {"name": "row2", "coord": [(0, 150), (300, 150)]},
    {"name": "row3", "coord": [(0, 250), (300, 250)]},
    {"name": "col1", "coord": [(50, 0), (50, 300)]},
    {"name": "col2", "coord": [(150, 0), (150, 300)]},
    {"name": "col3", "coord": [(250, 0), (250, 300)]},
    {"name": "diag1", "coord": [(0, 0), (300, 300)]},
    {"name": "diag2", "coord": [(0, 300), (300, 0)]},
]

# print(line_coord.index({"name": "row1"}))

test="col1"
for position_check in line_coord:
        if position_check["name"] == test:
            print("dibuje: %s en %s" % (position_check["name"], position_check["coord"]))
            line_data = position_check["coord"]

cv2.line(img, line_data[0], line_data[1], (0, 0, 250), 4)

cv2.imshow("Tablero", img)

k = cv2.waitKey(0)

if k:  # Si se pulsa cualquier tecla
    # Destruir todas las ventanas creadas
    cv2.destroyAllWindows()
