"""Expressões arítméticas: + - * / // % **"""

print(f"3 + 2 = {3 + 2}")
print(f"3 - 2 = {3 - 2}")
print(f"3 * 2 = {3 * 2}")
print(f"3 / 2 = {3 / 2}")   #divisão comum, resultando em número float
print(f"3 // 2 = {3 // 2}") #divisão inteira, ignora valor "quebrado", resultando em int
print(f"9 % 2 = {9 % 2}")   #resto de uma divisão inteira
print(f"3 ** 2 = {3 ** 2}") #faz o primeiro elemento ter a potência do segundo número

"""
Tipos de dados: int (número inteiro), float (número flutuante/"quebrado")
Funções matemáticas: abs(), min(), max()."""

exemplo_1 = [2, 4, -5, 3.2]
exemplo_2 = -5

print(f"abs(exemplo_2) = {abs(exemplo_2)}")       #Transforma o valor em seu "valor absoluto", tornando-o positivo
print(f"min(exemplo_1) = {min(exemplo_1)}")       #Responde com o menor valor da lista
print(f"max(exemplo_1) = {max(exemplo_1)}")      #Responde com o maior valor da lista

"""
Expressões lógicas são expressões onde os operadores são lógicos ou relacionais
Operadores relacionais: ==, !=, <, >, <=, >="""

print(f"3 == 2 é {3 == 2}")
print(f"3 != 2 é {3 != 2}")
print(f"3 < 2 é {3 < 2}")
print(f"3 > 2 é {3 > 2}")
print(f"3 <= 2 é {3 <= 2}")
print(f"3 >= 2 é {3 >= 2}")

"""
Operadores lógicos: and, not e or """

print(f"3 == 2 and 3 != 2 = {3 == 2 and 3 != 2}")           #"and" (e): só é V se ambas forem V
print(f"3 == 2 or 3 != 2 = {3 == 2 or 3 != 2}")             #"or" (ou inclusivo): V se ao menos uma for V
print(f"not (3 == 2 or 3 != 2) = {not(3 == 2 or 3 != 2)}")  #"not" (não): inverte valor lógico da expressão

"""
Outros operadores lógicos: in, not in """

print(f"3 in [1, 2, 3] = {3 in [1, 2, 3]}")                 #"ín" (em): V se o primeiro estiver contido no segundo
print(f"3 not in [1, 2, 3] = {3 not in [1, 2, 3]}")         #"not in" (não em): inversão do valor lógico da anterior

"""
Outros operadores lógicos: is, not is """

print(f"3 is 2 = {3 is 2}")                                 #"ís" (é): V se o primeiro é o mesmo que o segundo
print(f"3 is not 2 = {3 is not 2}")                         #"is not" (não é): inversão do valor lógico da anterior

# OBSERVAÇÃO: "==" e "is" são coisas distintas, == vê o valor, enquanto is confere a identidade do objeto.

"""
Variáveis é o nome atribuído a um objeto
"""
x = 3
print(f"x = {x}")

"""
Strings: variável usada para representar e manipular texto ou ouma sequência de caracteres, 
incluindo espaço em branco, e símbolos diferentes. 

Uma string é criada com uma sequência de caracteres envolvidos por aspas (simples ou duplas)
"""
aula = 'Alg I'
print(f"aula = {aula}")

"""
Strings com operadores
"""

s = "abc"
print(f"s == 'abc' = {s == "abc"}")

t = "def"
print(f"s < t = {s < t}")       #Caso comparação é de texto, parâmetro de maior ou menor é por ordem alfabética
print(f"s + t = {s + t}")

"""
Operadores que não funcionam com str: -, /, //, %, **.

Operadores importantes: len(), []
"""

palavra = "palavrinha"
print(f"len(palavra) = {len(palavra)}")     #len(): retorna o tamanho do str
print(palavra[0])                           #retorna com valor mencionado na indexação, no caso de "palavrinha", p = 0/-10
                                            # e último a = 9/-1 (contagem começa no p pelo zero, ou pelo fim com -1)
"""
É possível acessar substrings por meio de indexação:
"""
s = "abcd"
print(f"s[0:2] = {s[0:2]}")                 #Indexação tem fim não inclusivo, ou seja, mesmo mencionando [0:2], só são
                                            #retornados, os caracteres de 0 a 1.

print(f"s[:3] = {s[:3]}")                   #[:3]: caso a indexação deixe o começo "oculto", considere "desde o início"
print(f"s[-1:] = {s[-1:]}")                 #[:3]: caso a indexação deixe o fim "oculto", considere "até o fim"

"""
Métodos de manipulaçãoo de strings em Python:
s.find(p)       -> Responde como índice no qual a sub-str 'p' se encontra em 's'
s.count(p)      -> Responde como a frequência na qual a sub-str 'p' se encontra em 's'
s.replace(p, q) -> Substitui a sub-str 'p' pela sub-str 'q' em 's' 
s.capitalize()  -> Torna o primeiro caractere de 's' em maiúscula
s.upper()       -> Torna toda a string 's' em maiúscula
s.lower()       -> Torna toda a string 's' em minúscula
s.strip()       -> Remove espaços em branco excessivos
"""
