
class Aresta():
	def __init__(self,origem,destino,peso = 0):
		self.origem = origem
		self.destino = destino
		self.peso = peso
		self.prob = None
				
	def getProb(self):
		return self.prob
		
	def setProb(self, prob):
		self.prob = prob

	def getOrigem(self):
		return self.origem
		
	def getDestino(self):
		return self.destino
	
	def setpeso(self,peso):
		self.peso = peso
		
	def	getPeso(self):
		return self.peso
		
	def setOrigem(self,vertice):
		self.origem = vertice
		
	def setDestino(self,vertice):
		self.destino = vertice

	def log(self):
		return "%s----%i---->%s" % (self.origem.getId(),self.peso,self.destino.getId())

		