from datetime import datetime

def formato_data_correto(data):
  try:
    datetime.strptime(data, '%d/%m/%Y')

    return True
  
  except ValueError:
    return False