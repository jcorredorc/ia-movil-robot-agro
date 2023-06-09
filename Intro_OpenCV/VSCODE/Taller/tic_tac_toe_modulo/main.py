#!/usr/bin/env python3

import tic_tac_toe as triqui

"""
El juego siempre inicia con el movimiento de la máquina en el centro del tablero.

Se solicita al usuario que ingrese un número entre 1 y 9 para indicar el movimiento 
en la casilla deseada.

El programa indica si hay un ganador o queda en empate.
"""


tablero = triqui.CreateBoard()
triqui.DisplayBoard(tablero)

while True:
    tablero = triqui.EnterMove(tablero)
    triqui.DisplayBoard(tablero)
    if triqui.VictoryFor(tablero, "O") == "O":
        print("==============")
        print(" Gana humano")
        print("==============")
        break
    tablero = triqui.DrawMove(tablero)
    triqui.DisplayBoard(tablero)
    if triqui.VictoryFor(tablero, "X") == "X":
        print("===============")
        print(" Gana máquina")
        print("===============")
        break
    # si es empate sale del ciclo
    if triqui.VictoryFor(tablero, "O") == "tie":
        print("===============")
        print("   Empate !!!")
        print("===============")
        break
    # else:
    #     print(triqui.VictoryFor(tablero, "O"))
# print("FIN")
