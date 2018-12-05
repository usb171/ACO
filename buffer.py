'''
	dicPxyp[grafo[formiga].getId()] = roleta
	print dicPxyp

	dicPxypCopy = []



	for vertice in dicPxyp.keys():  #para cada vertice, descubra seu melhor caminho
		
		dicPxypCopy = dicPxyp.copy()
		del dicPxypCopy[vertice]
		out = [vertice]


		for vertice_roleta in dicPxypCopy.keys():
			print vertice_roleta
			melhorVertice = dicPxypCopy[vertice_roleta][randint(0, len(roleta) - 1)] # Sorteia o vértice com maior probabilidade
			out.append(melhorVertice) # Salva o vertice sorteado
			print out
			print dicPxypCopy[vertice_roleta]



		print "\n"

		out = [vertice]
		roleta = dicPxyp[vertice]
		melhorVertice = roleta[randint(0, len(roleta) - 1)]



		roleta = dicPxypCopy[vertice]
		melhorVertice = roleta[randint(0, len(roleta) - 1)]		
		print vertice
		print roleta
		print melhorVertice, "\n"
	'''


	'''	
	rotaSorteada = []
	for i in range(verticeSize - 1):
		melhorVertice = roleta[randint(0,len(roleta) - 1)]
		print roleta
		print melhorVertice
		roleta = filter(lambda x: x != melhorVertice, roleta)
		rotaSorteada.append(melhorVertice)

	print rotaSorteada


	print dicPxyp
		'''
















'''
	v1 = Vertice("Acai Concept")
	v2 = Vertice("Acai do Grau")
	v3 = Vertice("Puro Acai")
	v4 = Vertice("Point do Acai")
	v5 = Vertice("+Sabor do Acai")

	grafo = [v1, v2, v3, v4, v5]

	v1.novoVizinho(v2, 1.7, True) 
	v1.novoVizinho(v3, 0.85, True)
	v1.novoVizinho(v4, 2.9, True)
	v1.novoVizinho(v5, 3.0, True)

	v2.novoVizinho(v3, 0.8, True)
	v2.novoVizinho(v4, 1.2, True)
	v2.novoVizinho(v5, 2.0, True)

	v3.novoVizinho(v4, 2.0, True)
	v3.novoVizinho(v5, 2.2, True)

	v4.novoVizinho(v5, 1.1, True)
	'''










	'''
		PxypLetra = []
		for r in range(len(nomeRotas)):	PxypLetra = PxypLetra + [nomeRotas[r] for i in range(int(Pxyp[r]))] # Cria em letras a quantidade de Pxyp

		#dicPxyp[grafo[formiga].getId()] = PxypLetra




def remove(dic, elemento):
	del dic[elemento]
	for i in dic.keys():dic[i] = filter(lambda x: x != elemento, dic[i])
	return dic

		'''













		'''
	v1 = Vertice("V1")
	v2 = Vertice("V2")
	v3 = Vertice("V3")
	v4 = Vertice("V4")
	v5 = Vertice("V5")

	dicGrafo = {'v1': v1, 'v2': v2, 'v3': v3, 'v4': v4, 'v5': v5}
	grafo = [v1, v2, v3, v4, v5]

	v1.novoVizinho(v2, 1.7, True) 
	v1.novoVizinho(v3, 0.85, True)
	v1.novoVizinho(v4, 2.9, True)
	v1.novoVizinho(v5, 3.0, True)

	v2.novoVizinho(v3, 0.8, True)
	v2.novoVizinho(v4, 1.2, True)
	v2.novoVizinho(v5, 2.0, True)

	v3.novoVizinho(v4, 2.0, True)
	v3.novoVizinho(v5, 2.2, True)

	v4.novoVizinho(v5, 1.1, True)
	'''








	A = Vertice("A")
	B = Vertice("B")
	C = Vertice("C")
	D = Vertice("D")
	E = Vertice("E")

	dicGrafo = {'A': A, 'B': B, 'C': C, 'D': D, 'E': E}
	grafo = [A,B,C,D,E]

	
	A.novoVizinho(B, 22, True)
	A.novoVizinho(C, 50, True)
	A.novoVizinho(D, 48, True)
	A.novoVizinho(E, 29, True)

	B.novoVizinho(C, 30, True)
	B.novoVizinho(D, 34, True)
	B.novoVizinho(E, 32, True)

	C.novoVizinho(D, 22, True)
	C.novoVizinho(E, 23, True)

	E.novoVizinho(D, 25,True)




	A.novoVizinho(B, 1.7, True) 
	A.novoVizinho(C, 0.85, True)
	A.novoVizinho(D, 2.9, True)
	A.novoVizinho(E, 3.0, True)

	B.novoVizinho(C, 0.8, True)
	B.novoVizinho(D, 1.2, True)
	B.novoVizinho(E, 2.0, True)

	C.novoVizinho(D, 2.0, True)
	C.novoVizinho(E, 2.2, True)

	D.novoVizinho(E, 1.1, True)
	
	

	


	dicGrafo = {
			'A': {'obj':A, 'rota':[], 'custo': 0}, 
			'B': {'obj':B, 'rota':[], 'custo': 0}, 
			'C': {'obj':C, 'rota':[], 'custo': 0}, 
			'D': {'obj':D, 'rota':[], 'custo': 0}, 
			'E': {'obj':E, 'rota':[], 'custo': 0}
			}	


	tabFeromonio = {
				'AB': {'A': None, 'C': None, 'B': None, 'E': None, 'D': None, '(1-O)*Txy': 0}
				'AC': {'A': None, 'C': None, 'B': None, 'E': None, 'D': None, '(1-O)*Txy': 0}
				'AD': {'A': None, 'C': None, 'B': None, 'E': None, 'D': None, '(1-O)*Txy': 0}
				'AE': {'A': None, 'C': None, 'B': None, 'E': None, 'D': None, '(1-O)*Txy': 0}
				'BC': {'A': None, 'C': None, 'B': None, 'E': None, 'D': None, '(1-O)*Txy': 0}
				....				
	}

	'''