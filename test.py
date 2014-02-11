# -*- coding: latin-1 -*-

from juego import *
from nim import *
from mancala import *

print "\n\n----------- PRIMERA PRUEBA - NIM - 15 FICHAS -----------\n\n"

nim=Nim(15)
juego=Juego(nim,3)
juego.jugar()


print "\n\n----------- SEGUNDA PRUEBA - MANCALA - 6 CASILLAS, 4 SEMILLAS -----------\n\n"

mancala=Mancala(6,4)
juego=Juego(mancala,7)
juego.jugar()


print "\n\n----------- FIN PRUEBAS -----------\n\n"
raw_input("Presione cualquier tecla para salir.")
