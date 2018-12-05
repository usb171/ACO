# -*- coding: utf-8 -*-

import operator
from Vertice import *
from random import randint

def getDics(grafo):
	tabFeromonio = {}
	dicGrafo = {}

	for vertice in grafo:
		for vizinho in vertice.getVizinhos():
			dic = dict((k.getId(),0) for k in grafo)
			dic['(1-O)*Txy'] = 0
			dic['total'] = 0

			tabFeromonio[vertice.getId() + vizinho.getId()] = dic
			'''
			if vizinho.getId() + vertice.getId() not in tabFeromonio:
				tabFeromonio[vertice.getId() + vizinho.getId()] = dic
			'''

		dicGrafo[vertice.getId()] = {'obj':vertice, 'rota':[], 'custo': 0}

	return tabFeromonio, dicGrafo

def resetGrafo(grafo):
	for vertice in grafo:
		vertice.setVisitado(False)

def roleta(totalNos, dicGrafo, vertice, rota):
	
	rota.append(vertice.getId())
	vertice.setVisitado(True)
	melhorVertice = dicGrafo[vertice.melhorVertice()]['obj']

	totalNos = totalNos - 1
	
	if totalNos > 1:
		rota = roleta(totalNos, dicGrafo, melhorVertice, rota)
	else:
		return rota.append(melhorVertice.getId())


if __name__ == '__main__':	



	Ni0 = 0.1
	Q = 10
	sigma = 0.01
	interacaoMax = 20


	
	A = Vertice("A")
	B = Vertice("B")
	C = Vertice("C")
	D = Vertice("D")
	E = Vertice("E")



	A.novoVizinho(B, 22, True)
	A.novoVizinho(C, 50, True)
	A.novoVizinho(D, 48, True)
	A.novoVizinho(E, 29, True)

	B.novoVizinho(C, 30, True)
	B.novoVizinho(D, 34, True)
	B.novoVizinho(E, 32, True)

	C.novoVizinho(D, 22, True)
	C.novoVizinho(E, 23, True)

	D.novoVizinho(E, 25,True)

	grafo = [A,B,C,D,E]

	tabFeromonio, dicGrafo = getDics(grafo) # Monta a tabela de feromonio e o dicionário com as principais variáveis do grafo
	

	verticeSize = len(grafo)
	dicPxyp = {}
	for i in range(verticeSize): dicPxyp[grafo[i].getId()] = None # Cria a estrutura do dicionário global da probabilidade das rotas para a roleta 





	#if interacao == 0: 	Nxy = [Ni0 for x in range(verticeSize - 1)] # Cria uma lista com todos os elementos iguais a Nxy OBS(Feromônio inicial)
	
	for interacao in range(interacaoMax):


		print "interacao: ", interacao, '\n'

		for formiga in range(len(grafo)):  # Para cada formiga 

			Nxy = []
			nomeRotas = map(lambda x: x.getId(), grafo[formiga].getVizinhos())
			pesosRotas = map(lambda x: x.getPeso(), grafo[formiga].getArestas())		
			Txy = map(lambda x: 1 / float(x), pesosRotas)


			if interacao == 0: 
				Nxy = [Ni0 for x in range(verticeSize - 1)] # Cria uma lista com todos os elementos iguais a Nxy OBS(Feromônio inicial)
			else: # atualiza o feromônio
				for rota in map(lambda r: grafo[formiga].getId() + r ,nomeRotas):				
					Nxy.append(tabFeromonio[rota]['total'])

			#print "aqui:", Nxy

			TxyNxy = map(lambda t,n: t * n ,Txy, Nxy)


			soma  = reduce(operator.add, TxyNxy)
			Pxy = map(lambda x: float(float(x) / float(soma)) ,TxyNxy) 
			Pxyp = map(lambda x: x*100 ,Pxy)
			
			print "*******************************************************************************************"
			print "Formiga: ", formiga, " ", grafo[formiga].getId()
			print "Rotas: ", nomeRotas
			print "Pesos: ", pesosRotas
			print "Txy: ", Txy
			print "Nxy: ", Nxy, " ", map(lambda r: grafo[formiga].getId() + r ,nomeRotas)
			print "TxyNxy: ", TxyNxy
			print "Pxy: ", Pxy
			print "Pxyp: ", Pxyp


			for aresta, cont in zip(grafo[formiga].getArestas(), range(len(grafo[formiga].getArestas()))):
				aresta.setProb([aresta.getDestino().getId() for i in range(int(Pxyp[cont]))])
				print len(aresta.getProb()), ": ", aresta.getProb()
			print "*******************************************************************************************"
			print "\n"


		# Para cada ponto( formiga ou vertice) monte seu percurso
		for vertice in grafo:
			print "Saindo de ", vertice.getId()
			try:
				roleta(len(grafo), dicGrafo ,vertice, dicGrafo[vertice.getId()]['rota']) # (quantDeVertice, dicGrafo, listaDeRotas)
			except ValueError:
				pass
			dicGrafo[vertice.getId()]['rota'].append(vertice.getId()) # adiciona na lista de rotas como vertice de chegada o vertice de saída 
			resetGrafo(grafo)

			rota = dicGrafo[vertice.getId()]['rota'] # Rota montada pela roleta
			print rota

			# Soma dos pesos da rota descoberta		
			for v in rota[:len(rota) - 1]:
				partida = v
				destino = rota[rota.index(v) + 1]
				print partida, "---", dicGrafo[partida]["obj"].getVizinhosPesos()[destino], "--->", destino 
				dicGrafo[vertice.getId()]["custo"] = dicGrafo[vertice.getId()]["custo"] + dicGrafo[partida]["obj"].getVizinhosPesos()[destino] # Soma de cada custo de cada vertice visitado

			print "Custo da rota: ", dicGrafo[vertice.getId()]["custo"]


		# Atualizar tabela de feromonio

		print

		for r in tabFeromonio.keys():

			tabFeromonio[r]['(1-O)*Txy'] = ((1 - sigma) * Ni0)
			
			somaTotalFeromonio = 0

			for f in dicGrafo.keys():
				sumRota = reduce(operator.add, dicGrafo[f]['rota'])
				sumRotaInverter = reduce(operator.add,list(reversed(sumRota)))

				if r in sumRota or r in sumRotaInverter:
					tabFeromonio[r][f] = float(Q / float(dicGrafo[f]['custo']))
					somaTotalFeromonio = somaTotalFeromonio + tabFeromonio[r][f] # Soma do total de feromônio em cada rota r

			tabFeromonio[r]['total'] = somaTotalFeromonio

		for r in tabFeromonio.keys():
			print r, " ", tabFeromonio[r]['total']

		void, dicGrafo = getDics(grafo)
		 