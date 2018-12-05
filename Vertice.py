# -*- coding: utf-8 -*-

from Aresta import *
from random import randint

class Vertice():
    def __init__(self, id):
        self.id = id
        self.arestasVizinhos = [] # Lista de arestas dos Vizinhos
        self.visitado = False

    def setVisitado(self, visitado):
        self.visitado = visitado

    def getVisitado(self):
        return self.visitado

    def novoVizinho(self, vizinho, peso, bidirecional=False):

        if vizinho.__class__.__name__ != "Vertice":
            print("ERRO: Entre com um objeto <Vertice>")
            quit()
        else:
            aresta = Aresta(self, vizinho, peso)
            self.arestasVizinhos.append(aresta)
            print(aresta.log())

            if bidirecional:
                aresta2 = Aresta(vizinho, self, peso)
                vizinho.arestasVizinhos.append(aresta2)
                print(aresta2.log()+"\n")


    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id

    def getVizinhosPesos(self): # Retorna um dic com os pesos de cada vizinho
        dic = dict((k,None) for k in map(lambda x: x.getDestino().getId(), self.arestasVizinhos))
        for v in dic.keys():
            for a in  self.arestasVizinhos:
                buff = a
                if buff.getDestino().getId() == v:
                    dic[v] = buff.getPeso()

        return dic

    def getVizinhos(self):
        return map(lambda x: x.getDestino(), self.arestasVizinhos)

    def getArestas(self):
        return self.arestasVizinhos

    def melhorVertice(self):
        aux = []
        for aresta in self.getArestas():
            if aresta.getDestino().getVisitado() == False:
                aux = aux + aresta.getProb()
        return aux[randint(0,len(aux) - 1)] # Sorteia uma posição da lista de arestas vizinhas 

    