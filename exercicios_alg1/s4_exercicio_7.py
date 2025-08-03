def trocaPU(lst):
    lst[0], lst[-1] = lst[-1], lst[0]


ingredientes = ['farinha', 'açúcar', 'manteiga', 'maçãs']
trocaPU(ingredientes)
print(ingredientes)
