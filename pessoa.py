from datetime import datetime

class Pessoa:
    def __init__(self, cpf, rg, nome, nascimento):
        self.cpf = cpf
        self.rg = rg
        self.nome = nome
        self.nascimento = nascimento    
        
    def from_date(pessoaInfo, cpf, rg, nome, ano, mes, dia, nascimento):
        nascimento=datetime(dia, mes, ano)
        return pessoaInfo(cpf, rg, nome, nascimento)
    
    
    def __str__(self):
        return f"Nome: '{pessoa.nome}'\n" f"RG: {pessoa.rg}\n" f"Data Nascimento: {pessoa.nascimento.strftime('%d/%m/%Y')}\n" f"CPF: {pessoa.cpf}\n" 

pessoa = Pessoa(12345678901, 987654,"João", datetime(1990, 5, 15))
print(pessoa)