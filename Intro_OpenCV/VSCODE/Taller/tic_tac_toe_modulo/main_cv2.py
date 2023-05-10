#!/usr/bin/env python3

import tic_tac_toe as triqui

"""
El juego siempre inicia con el movimiento de la máquina en el centro del tablero.

Se solicita al usuario que ingrese un número entre 1 y 9 para indicar el movimiento 
en la casilla deseada.

El programa indica si hay un ganador o queda en empate.
Se impemplementa GUI con CV2
"""


tablero = triqui.CreateBoard()
triqui.DisplayBoard(tablero)
triqui.DisplayBoardCv2(tablero)

# while True:
tablero = triqui.EnterMove(tablero)
triqui.DisplayBoard(tablero)
triqui.DisplayBoardCv2(tablero)
#     if triqui.VictoryForCv2(tablero, "O")[0] == "O":
#         print("==============")
#         print(" Gana humano")
#         print("==============")
#         triqui.DrawVictoryCv2(tablero, triqui.VictoryForCv2(tablero, "O")[1],triqui.VictoryForCv2(tablero, "O")[0] == "O")
#         break
#     tablero = triqui.DrawMove(tablero)
#     triqui.DisplayBoard(tablero)
#     # triqui.DestroyBoardCv2(tablero)
#     if triqui.VictoryFor(tablero, "X") == "X":
#         print("===============")
#         print(" Gana máquina")
#         print("===============")
#         break
#     # si es empate sale del ciclo
#     if triqui.VictoryFor(tablero, "O") == "tie":
#         print("===============")
#         print("   Empate !!!")
#         print("===============")
#         break
#     # else:
#     #     print(triqui.VictoryFor(tablero, "O"))
# # print("FIN")
