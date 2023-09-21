class Nodo:
	def __init__(self,chave=None):
		self.chave = chave
		self.filho_esquerda = None
		self.filho_direita = None
		self.pai = None 
		self.altura = 1 # altura do nodo na árvore (distância máxima até a folha)

class ArvoreAVL:
	def __init__(self):
		self.raiz = None

	def __repr__(self):
		if self.raiz == None: return ''
		
		output = '\n'
		nodos_atuais = [self.raiz] # todos os nodos no nível atual
		altura_atual = self.raiz.altura # altura dos nodos no nível atual
		separador = ' ' * (2 ** (altura_atual - 1)) # separador de tamanho variável entre elementos
		
		while True:
			altura_atual += -1
			
			if len(nodos_atuais) == 0: break
			linha_atual = ' '
			proxima_linha = ''
			proximos_nodos = []

			if all(nodo is None for nodo in nodos_atuais):
				break

			for nodo in nodos_atuais:
				if nodo == None:
					linha_atual += '   ' + separador
					proxima_linha+='   ' + separador
					proximos_nodos.extend([None,None])
					
					continue

				if nodo.chave != None:       
					buf = ' ' * int((5 - len(str(nodo.chave)))/2)
					linha_atual += '%s%s%s'%(buf,str(nodo.chave), buf) + separador
					
				else:
					linha_atual += ' ' * 5 + separador

				if nodo.filho_esquerda != None:  
					proximos_nodos.append(nodo.filho_esquerda)
					proxima_linha += ' /' + separador
				else:
					proxima_linha += '  ' + separador
					proximos_nodos.append(None)

				if nodo.filho_direita != None: 
					proximos_nodos.append(nodo.filho_direita)
					proxima_linha += '\ ' + separador
					
				else:
					proxima_linha += '  ' + separador
					proximos_nodos.append(None)

			output += (altura_atual * '   ' + linha_atual + '\n' + altura_atual * '   ' + proxima_linha + '\n')
			nodos_atuais = proximos_nodos
			separador = ' ' * int(len(separador) / 2)
			
		return output

	def inserir(self, chave):
		if self.raiz == None:
			self.raiz = Nodo(chave)
			
		else:
			self._inserir(chave, self.raiz)

	def _inserir(self, chave, nodo_atual):
		if chave < nodo_atual.chave:
			if nodo_atual.filho_esquerda == None:
				nodo_atual.filho_esquerda = Nodo(chave)
				nodo_atual.filho_esquerda.pai = nodo_atual
				self.inspecionar_insercao(nodo_atual.filho_esquerda)
				
			else:
				self._inserir(chave,nodo_atual.filho_esquerda)
				
		elif chave > nodo_atual.chave:
			if nodo_atual.filho_direita == None:
				nodo_atual.filho_direita = Nodo(chave)
				nodo_atual.filho_direita.pai = nodo_atual 
				self.inspecionar_insercao(nodo_atual.filho_direita)
				
			else:
				self._inserir(chave, nodo_atual.filho_direita)
				
		else:
			print("Chave já se encontra na árvore!")

	def info(self):
		if self.raiz != None:
			self._info(self.raiz)

	def _info(self, nodo_atual):
		if nodo_atual != None:
			self._info(nodo_atual.filho_esquerda)
			print ('%s, h=%d'%(str(nodo_atual.chave), nodo_atual.altura))
			self._info(nodo_atual.filho_direita)

	def altura(self):
		if self.raiz != None:
			return self._altura(self.raiz, 0)
		
		else:
			return 0

	def _altura(self, nodo_atual, altura_atual):
		if nodo_atual == None: return altura_atual
		
		altura_esquerda = self._altura(nodo_atual.filho_esquerda, altura_atual + 1)
		altura_direita = self._altura(nodo_atual.filho_direita, altura_atual + 1)
		
		return max(altura_esquerda, altura_direita)

	def encontrar(self, chave):
		if self.raiz != None:
			return self._encontrar(chave, self.raiz)
		
		else:
			return None

	def _encontrar(self, chave, nodo_atual):
		if chave ==nodo_atual.chave:
			return nodo_atual
		
		elif chave < nodo_atual.chave and nodo_atual.filho_esquerda != None:
			return self._encontrar(chave, nodo_atual.filho_esquerda)
		
		elif chave > nodo_atual.chave and nodo_atual.filho_direita != None:
			return self._encontrar(chave ,nodo_atual.filho_direita)

	def deletar_valor(self, chave):
		return self.deletar_nodo(self.encontrar(chave))

	def deletar_nodo(self, nodo):
		# Protege contra a exclusão de um nodo não encontrado
		if nodo == None or self.encontrar(nodo.chave) == None:
			print("Chave a ser excluído não encontrado!")
			
			return None 

		# Retorna o nodo com valor mínimo na árvore com raiz no nodo de entrada
		def nodo_chave_minima(nodo):
			atual = nodo
			
			while atual.filho_esquerda != None:
				atual = atual.filho_esquerda
				
			return atual

		# Retorna o número de filhos do nodo especificado
		def numero_filhos(nodo):
			numero_filhos = 0
			
			if nodo.filho_esquerda != None: numero_filhos += 1
			if nodo.filho_direita != None: numero_filhos += 1
			
			return numero_filhos

		# Obter o pai do nodo a ser excluído
		nodo_pai = nodo.pai

		# Obter o número de filhos do nodo a ser excluído
		nodo_filhos = numero_filhos(nodo)

		# Caso 1 (nodo não possui filhos)
		if nodo_filhos == 0:
			if nodo_pai != None:
				# Remove a referência ao nodo do pai
				if nodo_pai.filho_esquerda == nodo:
					nodo_pai.filho_esquerda = None
					
				else:
					nodo_pai.filho_direita=None
					
			else:
				self.raiz = None

		# Caso 2 (nodo tem um filho)
		if nodo_filhos == 1:
			# Obter o nodo filho único
			if nodo.filho_esquerda != None:
				filho = nodo.filho_esquerda
				
			else:
				filho = nodo.filho_direita

			if nodo_pai != None:
				# Substitui o nodo a ser excluído por seu filho
				if nodo_pai.filho_esquerda == nodo:
					nodo_pai.filho_esquerda = filho
				else:
					nodo_pai.filho_direita = filho
					
			else:
				self.raiz = filho

			# Corrige o ponteiro pai no nodo
			filho.pai = nodo_pai

		# Caso 3 (nodo têm dois filhos)
		if nodo_filhos == 2:

			# Obtém o sucessor em ordem do nodo excluído
			sucessor = nodo_chave_minima(nodo.filho_direita)

			# Copia o valor do sucessor em ordem para o nodo anterior
            # mantendo o valor que desejamos deletar
			nodo.chave = sucessor.chave

			# Exclui o sucessor em ordem agora que seu valor era
            # copiado para outro nodo
			self.deletar_nodo(sucessor)

			# Função de saída para não chamarmos inspecionar_delecao 2x
			return

		if nodo_pai != None:
			# Corrige a altura do pai do nodo atual
			nodo_pai.altura = 1 + max(self.get_altura(nodo_pai.filho_esquerda), self.get_altura(nodo_pai.filho_direita))

			# Sobe de volta na árvore verificando se há
            # quaisquer seções que agora invalidam as regras de equilíbrio
			self.inspecionar_delecao(nodo_pai)

	def procurar(self, chave):
		if self.raiz != None:
			return self._procurar(chave, self.raiz)
		
		else:
			return False

	def _procurar(self, chave, nodo_atual):
		if chave == nodo_atual.chave:
			return True
		
		elif chave < nodo_atual.chave and nodo_atual.filho_esquerda != None:
			return self._procurar(chave,nodo_atual.filho_esquerda)
		
		elif chave > nodo_atual.chave and nodo_atual.filho_direita != None:
			return self._procurar(chave,nodo_atual.filho_direita)
		
		return False 

	def inspecionar_insercao(self, nodo_atual, caminho=[]):
		if nodo_atual.pai == None: return

		caminho = [nodo_atual] + caminho
 
		altura_esquerda = self.get_altura(nodo_atual.pai.filho_esquerda)
		altura_direita = self.get_altura(nodo_atual.pai.filho_direita)

		if abs(altura_esquerda - altura_direita) > 1:
			caminho = [nodo_atual.pai] + caminho
			self.rebalancear_nodo(caminho[0], caminho[1], caminho[2])

			return

		nova_altura = 1 + nodo_atual.altura

		if nova_altura > nodo_atual.pai.altura:
			nodo_atual.pai.altura = nova_altura

		self.inspecionar_insercao(nodo_atual.pai, caminho)

	def inspecionar_delecao(self,nodo_atual):
		if nodo_atual == None: return

		altura_esquerda = self.get_altura(nodo_atual.filho_esquerda)
		altura_direita =self.get_altura(nodo_atual.filho_direita)

		if abs(altura_esquerda - altura_direita) > 1:
			y = self.filho_mais_alto(nodo_atual)
			x = self.filho_mais_alto(y)
			self.rebalancear_nodo(nodo_atual, y, x)

		self.inspecionar_delecao(nodo_atual.pai)

	def rebalancear_nodo(self, z, y, x):
		if y == z.filho_esquerda and x == y.filho_esquerda:
			self.rotacao_direita(z)

		elif y == z.filho_esquerda and x == y.filho_direita:
			self.rotacao_esquerda(y)
			self.rotacao_direita(z)

		elif y == z.filho_direita and x == y.filho_direita:
			self.rotacao_esquerda(z)

		elif y == z.filho_direita and x == y.filho_esquerda:
			self.rotacao_direita(y)
			self.rotacao_esquerda(z)

		else:
			raise Exception('_rebalancear_nodo: z,y,x configuração do nodo não reconhecida!')

	def rotacao_direita(self, z):
		sub_raiz = z.pai 
		y = z.filho_esquerda
		t3 = y.filho_direita
		y.filho_direita = z
		z.pai = y
		z.filho_esquerda = t3

		if t3 != None: t3.pai = z

		y.pai=sub_raiz

		if y.pai == None:
				self.raiz = y

		else:
			if y.pai.filho_esquerda == z:
				y.pai.filho_esquerda = y

			else:
				y.pai.filho_direita = y	
					
		z.altura = 1 + max(self.get_altura(z.filho_esquerda), self.get_altura(z.filho_direita))
		y.altura = 1 + max(self.get_altura(y.filho_esquerda), self.get_altura(y.filho_direita))

	def rotacao_esquerda(self, z):
		sub_raiz = z.pai 
		y = z.filho_direita
		t2 = y.filho_esquerda
		y.filho_esquerda = z
		z.pai = y
		z.filho_direita = t2
		
		if t2 != None: t2.pai = z

		y.pai = sub_raiz

		if y.pai == None: 
			self.raiz = y

		else:
			if y.pai.filho_esquerda == z:
				y.pai.filho_esquerda = y

			else:
				y.pai.filho_direita = y

		z.altura = 1 + max(self.get_altura(z.filho_esquerda), self.get_altura(z.filho_direita))
		y.altura = 1 + max(self.get_altura(y.filho_esquerda), self.get_altura(y.filho_direita))

	def get_altura(self, nodo_atual):
		if nodo_atual == None: return 0

		return nodo_atual.altura

	def filho_mais_alto(self, nodo_atual):
		esquerda = self.get_altura(nodo_atual.filho_esquerda)
		direita = self.get_altura(nodo_atual.filho_direita)

		return nodo_atual.filho_esquerda if esquerda >= direita else nodo_atual.filho_direita

arvore_AVL = ArvoreAVL()

opcao = int(input("Menu\n(1) Inserir chave\n(2) Deletar chave\n(3) Visualizar árvore\n(4) Sair\nDigite uma opção: "))

while True:
    if opcao == 1:
        chaveInserir = input("Chave que deseja inserir: ")

        if chaveInserir.isdigit():
            arvore_AVL.inserir(chaveInserir)

        else:
            print("A chave deve ser do tipo inteiro!")

    elif opcao == 2:
        chaveDeletar = input("Chave que deseja deletar: ")

        if chaveDeletar.isdigit():
            arvore_AVL.deletar_valor(chaveDeletar)

        else:
            print("A chave deve ser do tipo inteiro!")

    elif opcao == 3:
        print(arvore_AVL.__repr__())
		
    else:
        break

    opcao = int(input("\nMenu\n(1) Inserir chave\n(2) Deletar chave\n(3) Visualizar árvore\n(4) Sair\nDigite uma opção: "))