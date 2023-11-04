import csv
from pessoa import Pessoa

class ReaderCSV:
    def __init__(self):
        with open('pessoas.csv', newline='') as f:
            reader = csv.DictReader(f, delimiter=';')

            dados = []

            for row in reader:
                dado = Pessoa(row['cpf'], row['rg'], row['nome'], row['nascimento'], row['cidade'])
                dados.append(dado)

            self.dados = dados

        # Teste print pessoas
        # for pessoa in pessoas:
        #     print(pessoa)

    def getDados(self):
        return self.dados