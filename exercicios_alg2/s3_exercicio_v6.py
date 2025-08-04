def maior_rec(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        restante = maior_rec(lista[1:])

        if lista[0] > restante:
            return lista[0]
        else:
            return restante

def soma_rec(l):
    if len(l) == 1:
        return l[0]
    else:
        resto = soma_rec(l[1:])
        soma = l[0] + resto
        return soma