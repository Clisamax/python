num = [2,5,9,1]
num[2]=3
num.append(7)
num.insert(2,0)
print(num)
print(f'Essa lista tem {len(num)} elementos.')
# apresentar valor e posição
# c == posição, v == valor
for c, v in enumerate(num):
    print(f'Na posição {c} encontrei o valor {v}!')
# digitar 5 valores a partir do comando input 
valores = list()
for cont in range(0,5):
    valores.append(int(input('Digite um valor: ')))
# cria uma ligação entre A e B
a = [2, 3, 4, 7]
b = a
print(f'Lista A: {a}')
print(f'Lista B: {b}')
# cria uma cópia sem ligação entre A e B
a = [2, 3, 4, 7]
b = a[:]
print(f'Lista A: {a}')
print(f'Lista B: {b}')