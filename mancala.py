# -*- coding: latin-1 -*-


from minimax import *

class EstadoMancala:
	def __init__ (self, mancala_propio, mancala_enemigo, hueco_propio, hueco_enemigo):
		self.hueco_propio=hueco_propio
		self.hueco_enemigo=hueco_enemigo
		self.mancala_propio=mancala_propio
		self.mancala_enemigo=mancala_enemigo



class Mancala:
	def __init__ (self, m, n):
		self.estado_inicial = EstadoMancala(0, 0, [n for i in range(0,m)], [n for i in range(0,m)])
		self.movimientos=[i for i in range(0,m)]
		self.min_valor=-n*m*2
		self.max_valor=n*m*2
		self.m=m
	
	def aplica_movimiento (self, movimiento, nodo):
		if nodo.estado.hueco_propio[movimiento]==0 or movimiento>=self.m:
			return False
		else:
			nodo_siguiente = self.siembra(movimiento, nodo)
			ultima_casilla = self.ultima_casilla_siembra(movimiento, nodo)
			if ultima_casilla == "MANCALA":
				return nodo_siguiente
			else:
				if ultima_casilla >= 0 and nodo_siguiente.estado.hueco_propio[ultima_casilla]==1:
					nodo_siguiente = self.captura_casilla(ultima_casilla, nodo_siguiente)
				if nodo.jugador == "MAX":
					return Nodo(self.invierte_estado(nodo_siguiente.estado), "MIN")
				else:
					return Nodo(self.invierte_estado(nodo_siguiente.estado), "MAX")
	
	def invierte_estado (self, estado):
		return EstadoMancala(estado.mancala_enemigo, estado.mancala_propio, [estado.hueco_enemigo[self.m - i -1] for i in range(0,self.m)], [estado.hueco_propio[self.m - i -1] for i in range(0,self.m)])
	

	def siembra (self, movimiento, nodo):
		estado_mancala = EstadoMancala(nodo.estado.mancala_propio, nodo.estado.mancala_enemigo, [nodo.estado.hueco_propio[i] for i in range(0,self.m)], [nodo.estado.hueco_enemigo[i] for i in range(0,self.m)])
		incremento = nodo.estado.hueco_propio[movimiento] / (self.m * 2 + 1)
		resto = nodo.estado.hueco_propio[movimiento] % (self.m * 2 + 1)
		estado_mancala.hueco_propio[movimiento]=0
		for i in range(0,self.m):
			estado_mancala.hueco_propio[i]+=incremento
		estado_mancala.mancala_propio+=incremento
		for i in range(0,self.m):
			estado_mancala.hueco_enemigo[i]+=incremento
		for i in range(movimiento + 1, movimiento + resto+1):
			if i < self.m:		
				estado_mancala.hueco_propio[i]+=1
			elif i == self.m:
				estado_mancala.mancala_propio+=1
			elif i > (self.m * 2):
				estado_mancala.hueco_propio[i - self.m * 2 - 1] +=1
			else:
				estado_mancala.hueco_enemigo[self.m*2 - i]+=1
		return Nodo(estado_mancala, nodo.jugador)
		

	def ultima_casilla_siembra (self, movimiento, nodo):
		incremento = nodo.estado.hueco_propio[movimiento] % (self.m * 2 + 1)
		if (incremento + movimiento) < self.m:
			return movimiento + incremento
		elif (incremento + movimiento) == self.m:
			return "MANCALA"
		else:
			return -1

	def captura_casilla (self, casilla, nodo):
		mancala_propio = nodo.estado.hueco_propio[casilla] + nodo.estado.hueco_enemigo[casilla] + nodo.estado.mancala_propio
		nodo.estado.hueco_enemigo[casilla] = 0
		nodo.estado.hueco_propio[casilla] = 0
		estado_mancala = EstadoMancala(mancala_propio, nodo.estado.mancala_enemigo, nodo.estado.hueco_propio, nodo.estado.hueco_enemigo)
		return Nodo(estado_mancala, nodo.jugador)
		
		
	def es_estado_final (self, estado):
		return sum(estado.hueco_propio)==0 or sum(estado.hueco_enemigo)==0
	

	def f_e_estatica (self, estado, jugador):
		if jugador == "MAX":
			return estado.mancala_propio + sum(estado.hueco_propio) - estado.mancala_enemigo - sum(estado.hueco_enemigo)
		else:
			return estado.mancala_enemigo - estado.mancala_propio
	
	
	def imprime_movimiento (self, movimiento):
		return "Sembrar el hueco %d." % movimiento
	
	
	def es_estado_ganador (self, nodo, turno):
		if nodo.jugador == turno:
			return (nodo.estado.mancala_propio + sum(nodo.estado.hueco_propio)) > (nodo.estado.mancala_enemigo + sum(nodo.estado.hueco_enemigo))
		else:
			return (nodo.estado.mancala_enemigo + sum(nodo.estado.hueco_enemigo)) > (nodo.estado.mancala_propio + sum(nodo.estado.hueco_propio))
			

	def imprime_estado (self, estado):
		cadena = "-------"
		for i in range(0,self.m):
			cadena+="----"
		cadena+="-------\n|     |"
		for i in range(0,self.m):
			if estado.hueco_enemigo[i]>9:
				cadena+="|%d|" % estado.hueco_enemigo[i]
			else:
				cadena+="| %d|" % estado.hueco_enemigo[i]
		cadena+= "|     |\n"
		if estado.mancala_enemigo > 9:
			cadena+= "|  %d |" % estado.mancala_enemigo
		else:		
			cadena+= "|  %d  |" % estado.mancala_enemigo
		for i in range(0,self.m):
			cadena+="----"
		if estado.mancala_propio > 9:
			cadena+= "|  %d |\n" % estado.mancala_propio
		else:		
			cadena+= "|  %d  |\n" % estado.mancala_propio
		cadena+= "|     |"
		for i in range(0,self.m):
			if estado.hueco_propio[i]>9:
				cadena+="|%d|" % estado.hueco_propio[i]
			else:
				cadena+="| %d|" % estado.hueco_propio[i]
		cadena+= "|     |\n-------"
		for i in range(0,self.m):
			cadena+="----"
		cadena+="-------\n\n"
		return cadena



