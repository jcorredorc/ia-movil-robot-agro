#!/usr/bin/env python3

from random import randrange, choice
import numpy as np
import cv2

allowed_fields = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # list(range(1,9))
machine_options = allowed_fields[:]
board_index = {
    "1": (0, 0),
    "2": (0, 1),
    "3": (0, 2),
    "4": (1, 0),
    "5": (1, 1),
    "6": (1, 2),
    "7": (2, 0),
    "8": (2, 1),
    "9": (2, 2),
}

# Creamos el tablero
img = np.zeros((300, 300, 3), np.uint8)  # filas,columnas - Alto,ancho
img[:, :, 0] = 197  # B
img[:, :, 1] = 220  # G
img[:, :, 2] = 69  # R
# cv2.startWindowThread()


# display board terminal
def DisplayBoard(board):
    #
    # la función acepta un parámetro el cual contiene el estado actual del tablero
    # y lo muestra en la consola
    #
    print(
        """
    +-------+-------+-------+
    |       |       |       |
    |   %s   |   %s   |   %s   |
    |       |       |       |
    +-------+-------+-------+
    |       |       |       |
    |   %s   |   %s   |   %s   |
    |       |       |       |
    +-------+-------+-------+
    |       |       |       |
    |   %s   |   %s   |   %s   |
    |       |       |       |
    +-------+-------+-------+"""
        % (
            board[0][0],
            board[0][1],
            board[0][2],
            board[1][0],
            board[1][1],
            board[1][2],
            board[2][0],
            board[2][1],
            board[2][2],
        )
    )


# display board OpenCV
def DisplayBoardCv2(board):
    img[:, :, 0] = 197  # B
    img[:, :, 1] = 220  # G
    img[:, :, 2] = 69  # R
    # Características del texto
    # texto = "X"
    # ubicacion = (31, 70)
    font = cv2.FONT_HERSHEY_SIMPLEX
    tamañoLetra = 2
    colorLetra = (0, 0, 0)
    grosorLetra = 2

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
        {"texto": board[0][0], "coord": coord_texto[0]},
        {"texto": board[0][1], "coord": coord_texto[3]},
        {"texto": board[0][2], "coord": coord_texto[6]},
        {"texto": board[1][0], "coord": coord_texto[1]},
        {"texto": board[1][1], "coord": coord_texto[4]},
        {"texto": board[1][2], "coord": coord_texto[7]},
        {"texto": board[2][0], "coord": coord_texto[2]},
        {"texto": board[2][1], "coord": coord_texto[5]},
        {"texto": board[2][2], "coord": coord_texto[8]},
    ]

    # # Creamos una imagen negra
    # img = np.zeros((300, 300, 3), np.uint8)  # filas,columnas - Alto,ancho
    # img[:, :, 0] = 197  # B
    # img[:, :, 1] = 220  # G
    # img[:, :, 2] = 69  # R
    # ----------------
    # Dibujo tablero
    # ----------------
    # Dibujamos un rectangulo con un grosor de 10 px
    cv2.rectangle(img, (0, 0), (300, 300), (0, 0, 0), 10)  # coord (x,y)
    # Dibujamos lineas del triqui con un grosor de 4 px
    cv2.line(img, (100, 0), (100, 300), (0, 0, 0), 4)
    cv2.line(img, (200, 0), (200, 300), (0, 0, 0), 4)
    cv2.line(img, (0, 100), (300, 100), (0, 0, 0), 4)
    cv2.line(img, (0, 200), (300, 200), (0, 0, 0), 4)

    for casilla in dic_board:
        cv2.putText(
            img,
            # print(casilla.get("texto"))  # texto
            # print(casilla.get("coord"))  # ubicacion
            str(casilla.get("texto")),  # texto
            casilla.get("coord"),  # ubicacion
            font,
            tamañoLetra,
            (0, 0, 255) if casilla.get("texto") == "O" else colorLetra,
            grosorLetra,
        )
    cv2.imshow("Tablero", img)
    k = cv2.waitKey(0)

    if k == 27:  # Si se pulsa cualquier tecla
        # Destruir todas las ventanas creadas
        cv2.destroyAllWindows()
        print("key press :P")
    else:
        print("siga ...")


def DestroyBoardCv2():
    # k = cv2.waitKey(0)

    # if k:  # Si se pulsa cualquier tecla
    # Destruir todas las ventanas creadas
    cv2.destroyAllWindows()


def EnterMove(board):
    #
    # la función acepta el estado actual del tablero y pregunta al usuario
    # acerca de su movimiento,
    # verifica la entrada y actualiza el tablero acorde a la decisión del usuario
    #
    user_move = 0

    while user_move not in allowed_fields:
        try:
            user_move = int(input("ingresa tu movimiento: "))
        except:
            print("no es un número .. :(")
    field_test = board[board_index.get(str(user_move))[0]][
        board_index.get(str(user_move))[1]
    ]
    if field_test not in ["O", "X"]:
        board[board_index.get(str(user_move))[0]][
            board_index.get(str(user_move))[1]
        ] = "O"
        # DisplayBoard(board)
    else:
        print("U: movimiento no permitido, ya ha sido jugado")
        EnterMove(board)
    return board


def EnterMoveCv2(board, sign):
    #
    # la función acepta el estado actual del tablero y el simbolo O o X
    # pregunta al usuario acerca de su movimiento,
    # verifica la entrada y actualiza el tablero acorde a la decisión del usuario
    #
    user_move = 0
    usr_msg = "Ingresa tu movimiento " + sign + ": "
    while user_move not in allowed_fields:
        try:
            user_move = int(input(usr_msg))
        except:
            print("no es un número .. :(, ingresa un número")
    field_test = board[board_index.get(str(user_move))[0]][
        board_index.get(str(user_move))[1]
    ]
    if field_test not in ["O", "X"]:
        board[board_index.get(str(user_move))[0]][
            board_index.get(str(user_move))[1]
        ] = sign
        # DisplayBoard(board)
    else:
        print("U: movimiento no permitido, ya ha sido jugado")
        EnterMoveCv2(board, sign)
    return board


def MakeListOfFreeFields(board):
    #
    # la función examina el tablero y construye una lista de todos los cuadros
    # vacíos
    # la lista esta compuesta por tuplas, cada tupla es un par de números que
    # indican la fila y columna
    #
    free_fields = []
    play_fields = ["X", "O"]
    for r in range(3):
        for c in range(3):
            if board[r][c] not in play_fields:
                free_fields.append((r, c))
    return free_fields


def VictoryForCv2(board, sign):
    #
    # la función analiza el estatus del tablero para verificar si
    # el jugador que utiliza las 'O's o las 'X's ha ganado el juego
    # devuelve la fila, columna o diagonal y el signo que gana el juego
    # o si no hay ganador devuelve "tie", o si no hay ganador "None"
    row1 = (board[0][0], board[0][1], board[0][2])
    row2 = (board[1][0], board[1][1], board[1][2])
    row3 = (board[2][0], board[2][1], board[2][2])
    col1 = (board[0][0], board[1][0], board[2][0])
    col2 = (board[0][1], board[1][1], board[2][1])
    col3 = (board[0][2], board[1][2], board[2][2])
    diag1 = (board[0][0], board[1][1], board[2][2])
    diag2 = (board[0][2], board[1][1], board[2][0])

    victory = [
        {"play": row1, "name": "row1"},
        {"play": row2, "name": "row2"},
        {"play": row3, "name": "row3"},
        {"play": col1, "name": "col1"},
        {"play": col2, "name": "col2"},
        {"play": col3, "name": "col3"},
        {"play": diag1, "name": "diag1"},
        {"play": diag2, "name": "diag2"},
    ]
    if sign == "X":
        test = ("X", "X", "X")
    else:
        test = ("O", "O", "O")
    win_cell = False
    for position_check in victory:
        if position_check["play"] == test:
            print("Gana: %s con %s" % (sign, position_check["name"]))
            win_cell = position_check["name"]

    if win_cell:
        return [sign, win_cell]
    else:
        # """ empate o aun se juega """
        if MakeListOfFreeFields(board) == []:
            # print("Empate: ", MakeListOfFreeFields(board))
            return [sign, "tie"]  # 'empate'
        else:
            # print("no gana", sign, "aun :P")
            return [sign, None]


def DrawVictoryCv2(board, win_cell, sign):
    """
    Graficar las lineas de ganar o
    escribir empate
    """
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
    line_data = [(0, 0), (0, 0)]
    if win_cell not in [None, "tie"]:
        for position_check in line_coord:
            if position_check["name"] == win_cell:
                print(
                    "dibuje: %s en %s"
                    % (position_check["name"], position_check["coord"])
                )
                line_data = position_check["coord"]

        cv2.line(img, line_data[0], line_data[1], (249, 71, 4), 4)
    elif win_cell == "tie":
        texto = "EMPATE "
        ubicacion = (40, 200)
        font = cv2.FONT_HERSHEY_DUPLEX
        tamañoLetra = 2
        colorLetra = (0, 0, 255)
        grosorLetra = 3
        # Escribir texto
        cv2.putText(img, texto, ubicacion, font, tamañoLetra, colorLetra, grosorLetra)

    cv2.imshow("Tablero", img)
    k = cv2.waitKey(0)

    if k == 27:  # Si se pulsa cualquier tecla
        # Destruir todas las ventanas creadas
        cv2.destroyAllWindows()


def VictoryFor(board, sign):
    #
    # la función analiza el estatus del tablero para verificar si
    # el jugador que utiliza las 'O's o las 'X's ha ganado el juego
    #
    row1 = (board[0][0], board[0][1], board[0][2])
    row2 = (board[1][0], board[1][1], board[1][2])
    row3 = (board[2][0], board[2][1], board[2][2])
    col1 = (board[0][0], board[1][0], board[2][0])
    col2 = (board[0][1], board[1][1], board[2][1])
    col3 = (board[0][2], board[1][2], board[2][2])
    diag1 = (board[0][0], board[1][1], board[2][2])
    diag2 = (board[0][2], board[1][1], board[2][0])

    if sign == "X":
        test = ("X", "X", "X")
    else:
        test = ("O", "O", "O")

    if (
        row1 == test
        or row2 == test
        or row3 == test
        or col1 == test
        or col2 == test
        or col3 == test
        or diag1 == test
        or diag2 == test
    ):
        if sign == "X":
            # print("gana la maquina ")
            return "X"
        else:
            # print("ganaste")
            return "O"
    else:
        # """ empate o aun se juega """
        if MakeListOfFreeFields(board) == []:
            # print("Empate: ", MakeListOfFreeFields(board))
            return "tie"  # 'empate'
        else:
            # print("no gana", sign, "aun :P")
            return None


def DrawMove(board):
    #
    # la función dibuja el movimiento de la maquina y actualiza el tablero
    #
    # machine_move = randrange(1, 9)
    global machine_options
    machine_move = choice(machine_options)
    machine_options.pop(machine_options.index(machine_move))
    # print(machine_options)
    field_test = board[board_index.get(str(machine_move))[0]][
        board_index.get(str(machine_move))[1]
    ]
    if field_test not in ["O", "X"]:
        board[board_index.get(str(machine_move))[0]][
            board_index.get(str(machine_move))[1]
        ] = "X"
        # DisplayBoard(board)
    else:
        # print("M: movimiento no permitido, ya ha sido jugado")
        DrawMove(board)
    return board


def CreateBoard():
    item = 0
    board = [[0 for x in range(3)] for y in range(3)]
    # print(board)
    for r in range(3):
        for c in range(3):
            item += 1
            board[r][c] = item
    # juega la maquina al inicio
    # board[1][1] = "X"
    return board


if __name__ == "__main__":
    # item = 0
    # board = [[0 for x in range(3)] for y in range(3)]
    # # print(board)
    # for r in range(3):
    #     for c in range(3):
    #         item += 1
    #         board[r][c] = item
    # # print(board)
    # board[0][0] = "X"
    # board[0][1] = "O"
    # board[0][2] = "X"
    # board[1][0] = "X"
    # board[1][1] = "X"
    # board[1][2] = "O"
    # board[2][0] = "O"
    # board[2][1] = "X"
    # board[2][2] = "X"
    # DisplayBoard(board)
    # for i in range(10):
    #     print(randrange(8))
    # jugada_maquina= randrange(8)
    # print(jugada_maquina)
    # EnterMove(board)
    # DrawMove(board)
    # VictoryFor(board, "X")
    # VictoryFor(board, "O")
    # print("---")
    # print(board)
    # print((board[0][0], board[0][1], board[0][2]))
    # print(board[2][:])
    # print(board[:][2])
    print("------------")
    tablero = CreateBoard()
    print(tablero)
    tablero[0][0] = "X"
    tablero[0][1] = "O"
    tablero[0][2] = "X"
    tablero[1][0] = "X"
    tablero[1][1] = "X"
    tablero[1][2] = "O"
    tablero[2][0] = "O"
    tablero[2][1] = "X"
    tablero[2][2] = "X"
    DisplayBoard(tablero)
    DisplayBoardCv2(tablero)
    [sign, msg] = VictoryForCv2(tablero, "X")
    DrawVictoryCv2(tablero, msg, sign)
