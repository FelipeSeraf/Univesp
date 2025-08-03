import fractions
resposta = 0
while resposta != 1 and resposta != 2:
    print('Olá, esse código foi feito para converter temperaturas de Celsius para Fahrenheit, e vice-versa.')
    print('Converter de Fahrenheit para Celsius: Digite 1')
    print('Converter de Celsius para Fahrenheit: Digite 2')
    resposta = int(input())
    if resposta == 1:
        F = float(input('Digite a temperatura em Fahrenheit para ser convertida em Celsius: '))
        C = (F-32) * fractions.Fraction(5, 9)
        print(f'A temperatura em Fahrenheit de {F}° em Celsius é de: {C}°')
    if resposta == 2:
        C = float(input('Digite a temperatura em Celsius para ser convertida em Fahrenheit: '))
        F = ((C * 9)/ 5) + 32
        print(f'A temperatura em Celsius de {C}° em Fahrenheit é de: {F}°')
    else:
        print('Número inválido, tente novamente.')
        resposta = int(input())

