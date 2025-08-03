def media(n1, n2):
    'Esta função calcula média com peso 0,4 para n1, e peso 0,6 para n2.'
    res = (0.4 * n1) + (0.6 * n2)
    return res

n1 = float(input('Digite o valor da nota n1 para cálculo de média:'))
n2 = float(input('Digite o valor da nota n2 para cálculo de média:'))

media_final = media(n1, n2)

if media_final >= 5.0:
    print(f'Parabéns, aluno aprovado, com media {media_final:.2f}')
else:
    print(f'Que pena, aluno reprovado, com media {media_final:.2f}')


