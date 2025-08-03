def soma2D(lista_1, lista_2):
    'aceita duas listas bidimensionais de tamanho igual, e faz a soma de cada item em linhas e colunas iguais'
    n_linhas = len(lista_1)
    n_colunas = len(lista_1[0])

    for i in range(n_linhas):
        linha_somada = []
        for j in range(n_colunas):
            linha_somada.append((lista_1[i][j] + lista_2[i][j]))
        print(linha_somada)


t = [[4, 7, 2, 5], [5, 1, 9, 2], [8, 3, 6, 6]]
s = [[0, 1, 2, 0], [0, 1, 1, 1], [0, 1, 0, 0]]
soma2D(t,s)