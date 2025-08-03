a = abs(float(input('Digite valor A do triângulo:')))
b = abs(float(input('Digite valor B do triângulo:')))
c = abs(float(input('Digite valor C do triângulo:')))

valores = [a, b, c]
valores.sort()

if valores[-1] >= valores[0] + valores[1]:
    print('Não é um triângulo')
elif a == b and a == c and b == c:
    print('É um triângulo equilátero')
elif a != b and a != c and b != c:
    print('É um triângulo escaleno')
else:
    print('É um triângulo isósceles')
