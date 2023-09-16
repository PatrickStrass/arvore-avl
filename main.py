class Arvore_AVL:
    def __init__(self):
        self.nodos = []

    def inserir(self, chave):
        self.nodos.append(Nodo(chave))

    def visualizar(self):
        for node in self.nodos:
            print(node.get_chave())

class Nodo:
    def __init__(self, chave, nodo_maior=None, nodo_menor=None):
        self.chave = chave
        self.nodo_maior = None
        self.nodo_menor = None

    #def __repr__(self):
     #   return '%s -> %s' % (self.dado, self.proximo)

arvore_avl = Arvore_AVL() 

opcao = int(input("Menu\n(1) Inserir número\n(2) Deletar número\n(3) Visualizar árvore\n(4) Sair\nDigite uma opção: "))

while(opcao != 4):
    if(opcao == 1):
        numeroInserir = int(input("Número que deseja inserir: "))
        arvore_avl.inserir(numeroInserir)

    elif(opcao == 2):
        print("Deletando...")

    elif(opcao == 3):
        print(arvore_avl.visualizar())

    else:
        break

    opcao = int(input("\nMenu\n(1) Inserir número\n(2) Deletar número\n(3) Visualizar árvore\n(4) Sair\nDigite uma opção: "))

"""
switch(opcao):
        case(1):
            numeroInserir = input(int("Número que deseja inserir: "))
            arvore_avl.inserir(numeroInserir)
            break
        
        case(2):
            print("Deletando...")
            break

        case(3):
            print("Opção 2...")
            break
"""