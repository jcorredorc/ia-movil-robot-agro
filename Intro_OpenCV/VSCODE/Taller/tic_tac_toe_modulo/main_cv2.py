#!/usr/bin/env python3

import tic_tac_toe as triqui

"""
El juego siempre inicia con el movimiento de la máquina en el centro del tablero.

Se solicita al usuario que ingrese un número entre 1 y 9 para indicar el movimiento 
en la casilla deseada.

El programa indica si hay un ganador o queda en empate.
Se implementa GUI con CV2
"""


tablero = triqui.CreateBoard()
triqui.DisplayBoard(tablero)
triqui.DisplayBoardCv2(tablero)
while True:
    tablero = triqui.EnterMove(tablero)
    triqui.DisplayBoard(tablero)
    triqui.DisplayBoardCv2(tablero)
    print("cell: ",triqui.VictoryForCv2(tablero, "O")[1])
    if triqui.VictoryForCv2(tablero, "O")[1] not in [None, "tie"]:
        print("==============")
        print(" Gana humano")
        print("==============")
        triqui.DrawVictoryCv2(tablero, triqui.VictoryForCv2(tablero, "O")[1],triqui.VictoryForCv2(tablero, "O")[0])
        break
    tablero = triqui.DrawMove(tablero)
    triqui.DisplayBoard(tablero)
    triqui.DisplayBoardCv2(tablero)
    # triqui.DestroyBoardCv2(tablero)
    # if triqui.VictoryFor(tablero, "X") == "X":
    if triqui.VictoryForCv2(tablero, "X")[1] not in [None, "tie"]:   
        print("===============")
        print(" Gana máquina")
        print("===============")
        triqui.DrawVictoryCv2(tablero, triqui.VictoryForCv2(tablero, "X")[1],triqui.VictoryForCv2(tablero, "X")[0])
        break
#     # si es empate sale del ciclo
    # if triqui.VictoryFor(tablero, "O") == "tie":
    if triqui.VictoryForCv2(tablero, "X")[1] == "tie":
        print("===============")
        print("   Empate !!!")
        print("===============")
        break
    else:
    #     siga jugando
        print("siga jugando")
# print("FIN")
