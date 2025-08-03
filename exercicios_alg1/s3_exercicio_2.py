notas = [9, 7, 7, 10, 3, 9, 6, 6, 2]

a = notas.count(7)
print(f'a = {a}')

notas[-1] = 4
print(notas)

notas_ordenadas = sorted(notas)
print(notas_ordenadas[-1])

print(notas_ordenadas)

media_notas = (sum(notas)/len(notas))
print(f'{media_notas:.2f}')