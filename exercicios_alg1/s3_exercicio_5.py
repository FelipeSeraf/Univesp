import math

def hipotenusa(a, b):
    res = math.sqrt((a ** 2)+(b ** 2))
    return res

hipotenusa(a,b) == 5

def area_circulo(raio):
    res = math.pi * (raio ** 2)
    return res

def conferir(x,y,a,b,r):
    res = ((x - a) ** 2) + ((y - b) ** 2) <= r ** 2
    return res




