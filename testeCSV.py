import csv
import pessoa as pessoa

# file = open("pessoas.csv")
# data = list(csv.reader(file, delimiter=";"))
# file.close()

pessoas = []

with open('pessoas.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        pessoas.append(pessoa(row[0]))

f.close()

print(pessoas)