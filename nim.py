# -*- coding: latin-1 -*-


from minimax import *

class Nim:
	def __init__ (self, numero_fichas_inicial):
		self.estado_inicial=numero_fichas_inicial
		self.movimientos=[i for i in range(1,4)]
		self.min_valor=-1
		self.max_valor=1
	
	def aplica_movimiento (self, movimiento, nodo):
		if movimiento > nodo.estado:
			return False
		else:
			if nodo.jugador=="MAX":
				return Nodo(nodo.estado - movimiento, "MIN")
			else:
				return Nodo(nodo.estado - movimiento, "MAX")

	def es_estado_final (self, estado):
		return estado == 0
	
	
	def f_e_estatica (self, estado, jugador):
		if jugador == "MAX":
			if (estado % 4) == 1:
				return self.min_valor
			else:
				return self.max_valor
		else:
			if (estado % 4) == 1:
				return self.max_valor
			else:
				return self.min_valor

	def imprime_movimiento (self, movimiento):
		return "Tomar %d fichas.\n" % movimiento
	

	def es_estado_ganador (self, nodo, turno):
		return nodo.jugador == turno
	
	def imprime_estado (self, estado):
		return "Quedan %d fichas.\n" % estado



