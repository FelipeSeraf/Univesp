def transpostar(m):
    'Recebe uma matriz bidimensional e retorna sua correspondente transposta'
    n_linhas = len(m)
    n_colunas = len(m[0])
    transposta = []

    for j in range(n_colunas):
        nova_linha = []
        for i in range(n_linhas):
            nova_linha.append(m[i][j])
        transposta.append(nova_linha)
    return transposta

matriz_original = [[1, 2, 3], [4, 5, 6]]
print(transpostar(matriz_original))