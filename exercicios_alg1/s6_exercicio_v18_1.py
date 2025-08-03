registro = []
while True:
    nome = str(input('Digite os nomes a serem registrado, para finalizar, pressione Enter:'))
    if nome == '':
        print('Registro finalizado.')
        break
    else:
        registro.append(nome)
        print(f'Nome {nome} registrado!')

print(registro)
