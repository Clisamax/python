'''val1 = int(input('digite um valor: '))
val2 = int(input('digite outro valor: '))
val3 = int(input('digite mais um valor: '))
val4 = int(input('digite o último valor: '))
tot = (val1, val2, val3, val4)
print(f'O valor {9} apareceu {tot.count(9)}vezes')
if 3 in tot:
    print(f'o valor {3} apareceu na {tot.index(3)+1}° posição')
else:
    print('O valor 3 não foi digitado em nunhuma posição')
print('Os valores pares digitados foram', end = ' ')
for n in tot:
    if n % 2 == 0:
        print(n, end = ' ')'''
        
val = int(input('digite um valor: ')), int(input('digite outro valor: ')), int(input('digite mais um valor: ')), int(input('digite o último valor: '))
print(f'O valor {9} apareceu {val.count(9)}vezes')
if 3 in val:
    print(f'o valor {3} apareceu na {val.index(3)+1}° posição')
else:
    print('O valor 3 não foi digitado em nunhuma posição')
print('Os valores pares digitados foram', end = ' ')
for n in val:
    if n % 2 == 0:
        print(n, end = ' ')
        
        