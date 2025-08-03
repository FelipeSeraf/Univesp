def average(x, y):
    """Ajuda sobre a função média no módulo __main__:
    média(x, y)
     retorna a média de x e y"""
    res = (x + y) / 2
    return res

media = average(2, 3.5)
print(media)

def negatives(x):
    """Ajuda sobre a função negativos no módulo __main__:
    negativos(list[])
     imprimi apenas os números negativos, em sequência"""
    for n in x:
        if n < 0:
            print(n)


lista = [4, 0, -1, -3, 6, -9]
negatives(lista)

help(average)
help(negatives)