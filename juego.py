# -*- coding: latin-1 -*-


from minimax import *


class Juego:

	def __init__ (self, juego, profundidad):
		self.juego=juego
		self.minimax = Minimax (juego, profundidad)
		
		
	def jugar (self):	
		print "-----------Empieza el juego-----------\n"
		jugador = ''
		while jugador not in ['m','h']:
			jugador = raw_input("Quien empieza? Escriba 'm' si desea que empiece la maquina o 'h' si desea que empiece el humano. \n")
		if jugador == 'm':
			jugador = "MAX"
		else:
			jugador = "MIN"
		nodo_juego = Nodo(self.juego.estado_inicial, jugador)
		while not self.juego.es_estado_final(nodo_juego.estado):
			if nodo_juego.jugador == "MIN":
				nodo_juego = self.jugada_humana (nodo_juego)
			else:
				nodo_juego = self.jugada_maquina(nodo_juego)
		self.analiza_final(nodo_juego)
		
	def jugada_humana (self, nodo):
		print "-----------Turno del jugador-----------\n"
		print "El estado actual es: \n"
		print self.juego.imprime_estado(nodo.estado)
		print "Esta es la lista de movimientos permitido:\n"
		i=1
		movimientos=[0]
		for movimiento in self.movimientos_permitidos(nodo):
			print "Movimiento %d: %s \n" % (i,self.juego.imprime_movimiento(movimiento))
			movimientos.append(movimiento)
			i+=1
		movimiento=-1
		while movimiento not in range(1,i):
			try:
				movimiento=int(raw_input("Seleccione el movimiento deseado escribiendo el indice del movimiento:\n"))
			except ValueError:
				movimiento=None
		print "El movimiento elegido es: %s" % self.juego.imprime_movimiento(movimiento)
		return self.juego.aplica_movimiento(movimientos[movimiento], nodo)
		
		
	def movimientos_permitidos (self, nodo):
		res=[]
		for movimiento in self.juego.movimientos:
			if self.juego.aplica_movimiento(movimiento, nodo):
				res.append(movimiento)
		return res

	
	def jugada_maquina (self, nodo):
		print "-----------Turno de la maquina-----------\n"
		print "El estado actual es: \n"
		print self.juego.imprime_estado(nodo.estado)
		return self.minimax.decision_minimax(nodo)
		
		

	def analiza_final (self, nodo):
		print "-----------Juego Terminado-----------\n"
		print self.juego.imprime_estado(nodo.estado)
		if self.juego.es_estado_ganador(nodo, "MAX"):
			print "La maquina ha ganado. \n"
		elif self.juego.es_estado_ganador(nodo, "MIN"):
			print "El humano ha ganado. \n"
		else:
			print "Tablas.\n"
		

