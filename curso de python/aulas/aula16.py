# TUPLAS
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Batata Frita' )

for comiuda in lanche:
    print(f'Eu vou comer {comida} ')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {comida} na posição {cont}')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
    
# metodos de tuplas

# organiza a tupla, mostra a tupla em ordem
print(sorted(lanche))

a = (2, 5, 4)
b = (5, 8, 1, 2, )
c = b + a
print(len(c))
# quantas vezes aparece o (5)
print(c.count(5))
# em que posição está (5)
print(c.index(5))
# em que posição está o (5) depois da posição (1)
print(c.index(5, 1))