from datetime import datetime

from verificaData import formato_data_correto

class Pessoa:

    def __init__(self, cpf, rg, nome, nascimento, cidade):
        self.cpf = cpf
        self.rg = rg
        self.nome = nome   
        self.nascimento = nascimento
        self.cidade = cidade
         
    @classmethod
    def from_date(cls, cpf, rg, nome, cidade, dia, mes, ano):
        data_str = f"{dia}/{mes}/{ano}"  # Cria uma string no formato 'dd/mm/yyyy'
        if formato_data_correto(data_str):
            nascimento = datetime.strptime(data_str, '%d/%m/%Y')
            return cls(cpf, rg, nome, nascimento, cidade)
        else:
            raise ValueError(f"A data {data_str} não está no formato correto.")

    def __str__(self):
        return (
            f"CPF: {self.cpf}\n"
            f"RG: {self.rg}\n"
            f"Nome: {self.nome}\n"
            f"Data Nascimento: {self.nascimento}\n"
            f"Cidade: {self.cidade}"
        )
# Criando e printando pessoa
#pessoa = Pessoa(12345678901, 9876543210, "João", "Brasil", datetime(1990, 5, 15))
#print(pessoa)