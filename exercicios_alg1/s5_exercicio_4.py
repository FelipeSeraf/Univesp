def meuIMC(altura, peso):
    res = peso / (altura ** 2)
    return res

altura = float(input('Digite sua altura em metros:'))
peso = float(input('Digite seu peso em quilos:'))

IMC = meuIMC(altura, peso)

if IMC < 25 and IMC >= 18.5:
    print('Normal')
elif IMC >= 25:
    print('Sobrepeso')
else:
    print('Abaixo do peso')

