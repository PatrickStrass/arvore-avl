from datetime import datetime

class Pessoa:
    def __init__(self, cpf, rg, nome, cidade, nascimento):
        self.cpf = cpf
        self.rg = rg
        self.nome = nome
        self.cidade = cidade
        self.nascimento = nascimento    
        
    def from_date(pessoaInfo, cpf, rg, nome, cidade, ano, mes, dia, nascimento):
        nascimento=datetime(dia, mes, ano)
        return pessoaInfo(cpf, rg, nome, cidade, nascimento)
    
    def __str__(self):
        return f"CPF: {self.__getattribute__('cpf')}\n" f"RG: {self.__getattribute__('rg')}\n" f"Nome: {self.__getattribute__('nome')}\n" f"Cidade: {self.__getattribute__('cidade')}\n" f"Data Nascimento: {self.__getattribute__('nascimento')}\n"

# Criando e printando pessoa
#pessoa = Pessoa(12345678901, 9876543210, "João", "Brasil", datetime(1990, 5, 15))
#print(pessoa)