""""Lista, tuplas e operadores"""

pets = ['cão', 'gato', 'peixe']
pets

I = [1, 'ab', [], [1, 2]]
I

"""
Operadores"""

pets[0]                                 # irá retornar 'cão'
I[-1]                                   # irá retornar [1, 2]

"""
Outros operadores: in, not in, +, *, len(), min(), max(), sum()."""

"""
Mutabilidade str vs []"""

str = 'abc'
str[0] = 'x'
print(str)                              # str = abc (imutável)

l=[1, 2, 3]
l[0] = 4
print(l)                                # l = 4, 2, 3 (mutável)

#Tuplas são iguais a listas, mas imutáveis. Usamos () ao invés de colchetes [] para criá-los

dias = ('seg', 'ter', 'qua')
dia

#dias[2] = 'qui'                        # (imutável) tem a imutabilidade de str, mas usada como lista
#retornará ERRO!

"""
Método"""

pets.append('cão')
pets                                    # pets = ['cão', 'gato', 'peixe', 'cão']

x.append(y)         # adiciona y como último elemento da lista x.
x.count(y)          # conta quantos elementos y tem na lista x.
x.index(y)          # retorna o índice de y, na lista x.
x.insert(z, y)      # adiciona o elemento y, no índice z, na lista x.
x.pop()             # retorna o último elemento da lista x, e o remove
x.remove(y)         # remove o elemento y da lista x.
x.reverse()         # inverte a ordem dos elementos na lista x.
x.sort()            # ordena em ordem alfabética ou numérica a lista x.

"""
Tipos de dados"""

type(2)             # retorna <class 'int'>

type('Olá')         # retorna <class 'str'>

type([1, 2, 3])     # retorna <class 'list'>

