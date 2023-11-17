from datetime import datetime

class Pessoa:
    def __init__(self, cpf, rg, nome, nascimento, cidade):
        self.cpf = cpf
        self.rg = rg
        self.nome = nome
        self.cidade = cidade
        self.nascimento = nascimento    
    
    def __str__(self):
        return f"CPF: {self.__getattribute__('cpf')}\n" f"RG: {self.__getattribute__('rg')}\n" f"Nome: {self.__getattribute__('nome')}\n" f"Cidade: {self.__getattribute__('cidade')}\n" f"Data Nascimento: {self.__getattribute__('nascimento')}"