print('Calculadora de nota bimestral')
n1 = float(input('Digite a nota 1: '))
n2 = float(input('Digite a nota 2: '))
n3 = float(input('Digite a nota 3: '))
n4 = float(input('Digite a nota 4: '))
media_aritm = (sum([n1, n2, n3, n4])) / 4

if media_aritm >= 5:
    print('Aluno aprovado com média')
else:
    print('Aluno reprovado com média')
print(f'Média: {media_aritm:.2f}')