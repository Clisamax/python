'''c = 1
while c < 10:
    print(c, end = ' ')
    c = c + 1
print('fim')'''

'''r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] ')).upper()
print('Fim')'''
 
n = 1
par = 0
ímpar = 0
while n != 0:
  n = int(input('digite um valor: '))
  if n % 2 == 0: #excluir o [ 0 ]  da contagem de pares
    if n % 2 == 0:
        par += 1
    else:
        ímpar += 1
print('Voçê digitou {} números pares e {} números ímpares!'.format(par, ímpar))

