sequencia = input('Digite a lista de palavras: ')
lista = sequencia.split()

for palavra in lista:
    if len(palavra) != 4:
        continue
    else:
        print(palavra)
