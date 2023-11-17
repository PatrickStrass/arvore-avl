from datetime import datetime
from readerCSV import ReaderCSV
from verificaData import formato_data_correto

class Nodo:
	def __init__(self, objeto, chave):
		self.objeto = objeto
		self.chave = chave
		self.filho_esquerda = None
		self.filho_direita = None
		self.pai = None
		self.altura = 1

	def get_pai(self):
		if self.pai is None: return "None"
			
		return self.pai.chave
	
	def get_filho_esquerdo(self):
		if self.filho_esquerda is None: return "None"

		return self.filho_esquerda.chave
	
	def get_filho_direito(self):
		if self.filho_direita is None: return "None"

		return self.filho_direita.chave

class ArvoreAVL:
	def __init__(self):
		self.raiz = None

	def __repr__(self):
		if self.raiz == None: return 'A árvore está vazia!'

		output = '\n'
		nodos_atuais = [self.raiz] 
		altura_atual = self.raiz.altura 
		separador = ' ' * ( 2 ** (altura_atual - 1))

		while True:
			altura_atual += -1
			if len(nodos_atuais) == 0: break

			linha_atual = ' '
			proxima_linha = ''
			proximos_nodos = []

			if all(nodo == None for nodo in nodos_atuais):
				break

			for nodo in nodos_atuais:

				if nodo == None:
					linha_atual += '   ' + separador
					proxima_linha += '   ' + separador
					proximos_nodos.extend([None, None])

					continue

				if nodo.chave != None:        
					buf = ' ' * int((5 - len(str(nodo.chave))) / 2)
					linha_atual += '%s%s%s' % (buf, str(nodo.chave), buf) + separador

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

	def inserir_data(self, chave, nodo_atual, objeto):
		if self.raiz == None:
			self.raiz = Nodo(objeto, chave)

		else:
			chave_data = datetime.strptime(chave, '%d/%m/%Y')
			nodo_atual_data = datetime.strptime(nodo_atual.chave, '%d/%m/%Y')

			if chave_data.date() < nodo_atual_data.date():
				if nodo_atual.filho_esquerda == None:
					nodo_atual.filho_esquerda = Nodo(objeto, chave)
					nodo_atual.filho_esquerda.pai = nodo_atual

					self.inspecionar_insercao(nodo_atual.filho_esquerda)

				else:
					self.inserir_data(chave, nodo_atual.filho_esquerda, objeto)

			elif chave_data.date() > nodo_atual_data.date():
				if nodo_atual.filho_direita == None:
					nodo_atual.filho_direita = Nodo(objeto, chave)
					nodo_atual.filho_direita.pai = nodo_atual

					self.inspecionar_insercao(nodo_atual.filho_direita)

				else: 
					self.inserir_data(chave, nodo_atual.filho_direita, objeto)

			else:
				print("Chave já está na árvore!")

	def inserir(self, chave, nodo_atual, objeto):
		if self.raiz == None:
			self.raiz = Nodo(objeto, chave)

		else:
			if chave < nodo_atual.chave:
				if nodo_atual.filho_esquerda == None:
					nodo_atual.filho_esquerda = Nodo(objeto, chave)
					nodo_atual.filho_esquerda.pai = nodo_atual

					self.inspecionar_insercao(nodo_atual.filho_esquerda)

				else:
					self.inserir(chave, nodo_atual.filho_esquerda, objeto)

			elif chave > nodo_atual.chave:
				if nodo_atual.filho_direita == None:
					nodo_atual.filho_direita = Nodo(objeto, chave)
					nodo_atual.filho_direita.pai = nodo_atual

					self.inspecionar_insercao(nodo_atual.filho_direita)

				else: 
					self.inserir(chave, nodo_atual.filho_direita, objeto)

			else:
				print("Chave já está na árvore!")

	def info(self, nodo_atual):
		if self.raiz != None:
			if nodo_atual != None:
				self.info(nodo_atual.filho_esquerda)
				print('Chave: %s, altura: %d, pai: %s, filho à esquerda: %s, filho à direita: %s' % (str(nodo_atual.chave), nodo_atual.altura, str(nodo_atual.get_pai()), str(nodo_atual.get_filho_esquerdo()), str(nodo_atual.get_filho_direito())))
				self.info(nodo_atual.filho_direita)

		else:
			print("Informação indisponível!")

	def get_objeto_por_data_menor_igual_a(self, data, nodo_atual):
		if self.raiz != None:
			if nodo_atual != None:
				data_nodo = datetime.strptime(nodo_atual.objeto.nascimento, '%d/%m/%Y')
				data_input = datetime.strptime(data, '%d/%m/%Y')

				if data_nodo.date() <= data_input.date():
					print(f'\n{nodo_atual.objeto}')

					self.get_objeto_por_data_menor_igual_a(data, nodo_atual.filho_esquerda)
					self.get_objeto_por_data_menor_igual_a(data, nodo_atual.filho_direita)

				else:
					self.get_objeto_por_data_menor_igual_a(data, nodo_atual.filho_esquerda)

		else:
			print("Árvore AVL está vazia!")

	def get_objeto_por_iniciais(self, iniciais, nodo_atual):
		if self.raiz != None:
			if nodo_atual != None:
				if iniciais.lower() in nodo_atual.objeto.nome.lower():
					print(f'\n{nodo_atual.objeto}')

				self.get_objeto_por_iniciais(iniciais, nodo_atual.filho_esquerda)
				self.get_objeto_por_iniciais(iniciais, nodo_atual.filho_direita)

		else:
			print("Pessoas com as iniciais informadas não encontradas!")

	def encontrar(self, chave, nodo_atual):
		if self.raiz != None:
			if chave == nodo_atual.chave:
				return nodo_atual
			
			elif chave < nodo_atual.chave and nodo_atual.filho_esquerda != None:
				return self.encontrar(chave, nodo_atual.filho_esquerda)
			
			elif chave > nodo_atual.chave and nodo_atual.filho_direita != None:
				return self.encontrar(chave, nodo_atual.filho_direita)
		
		return None
 
	def deletar(self, chave):
		return self._deletar(self.encontrar(chave, self.raiz))

	def _deletar(self, nodo):
		if nodo == None or self.encontrar(nodo.chave, self.raiz) == None:
			print("Chave a ser excluída não encontrada na árvore!")

			return None 

		def nodo_chave_minima(nodo):
			atual = nodo

			while atual.filho_esquerda != None: 
				atual = atual.filho_esquerda

			return atual

		def numero_filhos(nodo):
			numero_filhos = 0

			if nodo.filho_esquerda != None: numero_filhos += 1 
			if nodo.filho_direita != None: numero_filhos += 1 

			return numero_filhos

		nodo_pai = nodo.pai
		nodos_filhos = numero_filhos(nodo)

		# Caso 1 (nodo não possui filhos)
		if nodos_filhos == 0:
			if nodo_pai != None: 
				if nodo_pai.filho_esquerda == nodo:
					nodo_pai.filho_esquerda = None

				else:
					nodo_pai.filho_direita = None

			else:
				self.raiz = None

		# Caso 2 (nodo possui 1 filho)
		if nodos_filhos == 1:
			if nodo.filho_esquerda != None: 
				filho = nodo.filho_esquerda

			else:
				filho = nodo.filho_direita

			if nodo_pai != None: 
				if nodo_pai.filho_esquerda == nodo:
					nodo_pai.filho_esquerda = filho

				else:
					nodo_pai.filho_direita = filho

			else:
				self.raiz = filho

			filho.pai = nodo_pai

		# Caso 3 (nodo possui 2 filhos)
		if nodos_filhos == 2:
			sucessor = nodo_chave_minima(nodo.filho_direita)
			nodo.chave = sucessor.chave
			self._deletar(sucessor)

			return

		if nodo_pai != None: 
			nodo_pai.altura = 1 + max(self.get_altura(nodo_pai.filho_esquerda), self.get_altura(nodo_pai.filho_direita))

			# Percorre a árvore de volta verificando se existe qualquer desbalanceamento na árvore
			self.inspecionar_exclusao(nodo_pai)

	def inspecionar_insercao(self, nodo_atual, caminho=[]):
		if nodo_atual.pai == None: return

		caminho = [nodo_atual] + caminho

		altura_esquerda = self.get_altura(nodo_atual.pai.filho_esquerda)
		altura_direita = self.get_altura(nodo_atual.pai.filho_direita)

		if abs(altura_esquerda - altura_direita) > 1:
			caminho = [nodo_atual.pai] + caminho
			self.rebalancear(caminho[0], caminho[1], caminho[2])

			return

		nova_altura = 1 + nodo_atual.altura 
		
		if nova_altura > nodo_atual.pai.altura:
			nodo_atual.pai.altura = nova_altura

		self.inspecionar_insercao(nodo_atual.pai, caminho)

	def inspecionar_exclusao(self, nodo_atual):
		if nodo_atual == None: return

		altura_esquerda = self.get_altura(nodo_atual.filho_esquerda)
		altura_direita = self.get_altura(nodo_atual.filho_direita)

		if abs(altura_esquerda - altura_direita) > 1:
			y = self.filho_mais_alto(nodo_atual)
			x = self.filho_mais_alto(y)
			self.rebalancear(nodo_atual, y, x)

		self.inspecionar_exclusao(nodo_atual.pai)

	def rebalancear(self, z, y, x):
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
			raise Exception('Configuração de rebalanceamento não reconhecida!')

	def rotacao_direita(self, z):
		sub_raiz = z.pai 
		y = z.filho_esquerda
		t3 = y.filho_direita
		y.filho_direita = z
		z.pai = y
		z.filho_esquerda = t3

		if t3 != None: t3.pai = z 

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

		return nodo_atual.filho_esquerda if esquerda>=direita else nodo_atual.filho_direita
		
dadosPessoas = ReaderCSV().getDados()

arvore_AVL_por_CPF = ArvoreAVL()
arvore_AVL_por_nome = ArvoreAVL()
arvore_AVL_por_nascimento = ArvoreAVL()

for pessoa in dadosPessoas:
	arvore_AVL_por_CPF.inserir(pessoa.cpf, arvore_AVL_por_CPF.__getattribute__("raiz"), pessoa)
	arvore_AVL_por_nome.inserir(pessoa.nome, arvore_AVL_por_nome.__getattribute__("raiz"), pessoa)
	arvore_AVL_por_nascimento.inserir_data(pessoa.nascimento, arvore_AVL_por_nascimento.__getattribute__("raiz"), pessoa)

opcao = input("\nMenu\n(1) Consultar pessoa por CPF\n(2) Consultar pessoas por string inicial de nome\n(3) Consultar pessoas por data de nascimento menor ou igual\nDigite outra tecla para sair\nDigite uma opção: ")

while opcao.isdigit():
	if int(opcao) == 1:
		cpfInserir = input("CPF que deseja procurar: ")

		if cpfInserir.isdigit():
			print(f'\n{arvore_AVL_por_CPF.encontrar(cpfInserir, arvore_AVL_por_CPF.__getattribute__("raiz")).objeto}')

		else:
			print("O CPF deve ser do tipo numérico!")

	elif int(opcao) == 2:
		iniciais = input("String inicial para nome: ")
		
		if not iniciais.isdigit():
			arvore_AVL_por_nome.get_objeto_por_iniciais(iniciais, arvore_AVL_por_nome.__getattribute__("raiz"))

		else:
			print("Formato de string inválido!")

	elif int(opcao) == 3:
		dataNascimento = input("Data de nascimento menor ou igual a (DD/MM/AAAA): ")

		if formato_data_correto(dataNascimento):
			arvore_AVL_por_nascimento.get_objeto_por_data_menor_igual_a(dataNascimento, arvore_AVL_por_nascimento.__getattribute__("raiz"))

		else:
			print("Formato de data inválido!")

	else: 
		break

	opcao = input("\nMenu\n(1) Consultar pessoa por CPF\n(2) Consultar pessoas por string inicial de nome\n(3) Consultar pessoas por data de nascimento menor ou igual\nDigite outra tecla para sair\nDigite uma opção: ")