#!/usr/bin/env python3

import tic_tac_toe as triqui

"""
El juego siempre inicia con el movimiento del jugador X

Se solicita al usuario que ingrese un número entre 1 y 9 para indicar el movimiento 
en la casilla deseada.

El programa indica si hay un ganador o queda en empate.

Se implementa GUI con CV2

bug: Es necesario siempre enfocar la ventana de la imagen y teclear, para que el juego continue
"""


tablero = triqui.CreateBoard()
triqui.DisplayBoard(tablero)
triqui.DisplayBoardCv2(tablero)
while True:
    tablero = triqui.EnterMoveCv2(tablero, "X")
    triqui.DisplayBoard(tablero)
    triqui.DisplayBoardCv2(tablero)
    print("cell: ", triqui.VictoryForCv2(tablero, "X")[1])
    # #     # si es empate sale del ciclo
    # # if triqui.VictoryFor(tablero, "O") == "tie":
    if triqui.VictoryForCv2(tablero, "X")[1] == "tie":
        #     or triqui.VictoryForCv2(tablero, "O")[1] == "tie"
        # ):
        print("===============")
        print("   Empate !!!")
        print("===============")
        triqui.DrawVictoryCv2(
            tablero,
            triqui.VictoryForCv2(tablero, "X")[1],
            triqui.VictoryForCv2(tablero, "X")[0],
        )
        break
    else:
        # siga jugando
        print("siga jugando")
    if triqui.VictoryForCv2(tablero, "X")[1] not in [None, "tie"]:
        print("====================")
        print("   Gana jugador X")
        print("====================")
        triqui.DrawVictoryCv2(
            tablero,
            triqui.VictoryForCv2(tablero, "X")[1],
            triqui.VictoryForCv2(tablero, "X")[0],
        )
        break
    tablero = triqui.EnterMoveCv2(tablero, "O")
    triqui.DisplayBoard(tablero)
    triqui.DisplayBoardCv2(tablero)
    # # if triqui.VictoryFor(tablero, "X") == "X":
    if triqui.VictoryForCv2(tablero, "O")[1] not in [None, "tie"]:
        print("====================")
        print("   Gana jugador O")
        print("====================")
        triqui.DrawVictoryCv2(
            tablero,
            triqui.VictoryForCv2(tablero, "O")[1],
            triqui.VictoryForCv2(tablero, "O")[0],
        )
        break
# triqui.DestroyBoardCv2(tablero)
print("FIN")
