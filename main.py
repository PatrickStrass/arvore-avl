class Arvore_AVL:
    def __init__(self):
        self.raiz = None

    #def __repr__(self):

    def inserir(self, chave):
        if self.raiz == None:
            self.raiz = Nodo(chave)

        else:
            self._inserir(chave, self.raiz)

    def _inserir(self, chave, nodo_atual):
        if chave < nodo_atual.chave:
            if nodo_atual.filho_esquerda == None:
                nodo_atual.filho_esquerda = Nodo(chave)
                nodo.atual.filho_esquerda.pai = nodo_atual

            else:
                self._insert(chave, nodo_atual.filho_esquerda)

        elif chave > nodo_atual:
            if nodo_atual.filho_direita == None:
                

        """
        novaChave = Nodo(chave)

        self.nodos.append(novaChave)

        if (self.nodos.len != 0):
            novaChave.pai = self.nodos.index(len - 1)
        """

    def deletar(self, chave):
        self.nodos.remove(chave);  

    def visualizar(self):
        for node in self.nodos:
            print(node.chave)

class Nodo:
    def __init__(self, chave):
        self.chave = chave
        self.filho_esquerda = None
        self.filho_direita = None
        self.pai = None
        self.altura = 0

    def fator_balanceamento():
        altura_esq, altura_dir = 0

        fator_balanceamento(self.Nodo.nodo.menor)

        return 0

arvore_avl = Arvore_AVL() 

opcao = int(input("Menu\n(1) Inserir chave\n(2) Deletar chave\n(3) Visualizar árvore\n(4) Sair\nDigite uma opção: "))

while (True):
    if opcao == 1:
        chaveInserir = input("Chave que deseja inserir: ")

        if chaveInserir.isdigit():
            chaveExiste = False

            for nodo in arvore_avl.nodos:
                if nodo.chave == chaveInserir:
                    chaveExiste = True

            if chaveExiste:
                print("Chave já existe!")

            else:
                arvore_avl.inserir(chaveInserir)

        else:
            print("A chave deve ser do tipo inteiro!")

    elif opcao == 2:
        chaveDeletar = input("Chave que deseja deletar: ")

        if chaveDeletar.isdigit():
            if arvore_avl.nodos.count(chaveDeletar):   
                arvore_avl.deletar()
            
            else:
                print("Chave não existe!")

        else: 
            print("A chave deve ser do tipo inteiro!")

    elif opcao == 3:
        print(arvore_avl.visualizar())

    else:
        break

    opcao = int(input("\nMenu\n(1) Inserir chave\n(2) Deletar chave\n(3) Visualizar árvore\n(4) Sair\nDigite uma opção: "))