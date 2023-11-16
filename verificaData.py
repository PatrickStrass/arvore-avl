from datetime import datetime

#usada para validar se uma string de data está no formato 'dia/mês/ano'.
def formato_data_correto(data):
  try:
    datetime.strptime(data, '%d/%m/%Y')

    return True
  
  except ValueError:
    return False
