class Minimax:

	def __init__ (self,juego,profundidad):
		self.juego=juego
		self.profundidad=profundidad
		
		
	def decision_minimax(self,actual):
		alfa=self.juego.min_valor
		max_nodo=None
		for nodo in self.sucesores(actual):
			valor_actual=self.valor_minimax(nodo, self.profundidad - 1, alfa, self.juego.max_valor)
			if valor_actual > alfa:
				alfa=valor_actual
				max_nodo=nodo
			if alfa >= self.juego.max_valor:
				break
		if not max_nodo:
			max_nodo = self.sucesores(actual)[0]
		return max_nodo
	
	def valor_minimax(self, nodo, profundidad, alfa, beta):
		if self.juego.es_estado_final(nodo.estado) or profundidad==0 or not self.sucesores(nodo):
			return self.juego.f_e_estatica(nodo.estado,nodo.jugador)
		elif nodo.jugador == "MAX":
			return self.maximizador(self.sucesores(nodo), profundidad - 1, alfa, beta)
		else:
			return self.minimizador(self.sucesores(nodo), profundidad - 1, alfa, beta)
	
	
	def sucesor(self, nodo, movimiento):
		nodo_sucesor = self.juego.aplica_movimiento(movimiento, nodo)
		if not nodo_sucesor:
			return False
		else:
			return nodo_sucesor
		
	def sucesores(self, nodo):
		sucesores = []
		for movimiento in self.juego.movimientos:
			sucesor = self.sucesor (nodo, movimiento)
			if sucesor:
				sucesores.append(sucesor)
		return sucesores
		
		
	def maximizador(self, sucesores, profundidad, alfa, beta):
		for nodo in sucesores:
			valor_actual = self.valor_minimax(nodo, profundidad, alfa, beta)
			if valor_actual > alfa:
				alfa=valor_actual
			if alfa>=beta:
				break
		return alfa
		
	def minimizador(self, sucesores, profundidad, alfa, beta):
		for nodo in sucesores:
			valor_actual = self.valor_minimax (nodo, profundidad, alfa, beta)
			if valor_actual < beta:
				beta = valor_actual
			if alfa>=beta:
				break
		return beta
		
		
		
class Nodo:
	def __init__ (self, estado, jugador):
		self.estado=estado
		self.jugador=jugador
		

