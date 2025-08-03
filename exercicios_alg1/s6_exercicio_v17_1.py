str_list = ['João', 'Roberto', 'Rafael']
vogais = []
for palavra in str_list:
    for letra in palavra:
        if letra in 'aeiou':
            vogais.append(letra)
print(vogais)