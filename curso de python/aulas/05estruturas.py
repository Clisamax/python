# Condições 

# FOR

i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('fim')

# IF e ELSE

nome = input('Qual é o seu nome? ')
if nome == 'Gustavo':
    print('Que nome lindo você tem! ')
else:
    print('Seu nome é tão normal! ')
print('Bom dia, {}!'.format(nome))

# ELIF

nome = str(input('Qual seu nome? '))
if nome == 'Max' :
     print('Que nome bonito! ')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo' :
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Claudia Jéssica Juliana' :
    print('Belo nome Feminino ')
else:
    print('Seu nome é bem normal. ')
print('Tenha um bom dia, {}!'.format(nome))

# WHILE
cont = 1
while True:
    print(cont, '->' , end = ' ')
    cont += 1
    if cont == 9:
        break
print('acabou')

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