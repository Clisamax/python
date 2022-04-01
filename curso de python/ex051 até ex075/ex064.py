'''num = 0
soma = -999
cont = -1
while num != 999:
    num = int(input('Digite um Número [999 para parar]: '))
    soma += num
    cont += 1
print('Voçê digitou {} números e a soma entre eles foi {}'.format(cont, soma))'''

num = soma = cont = 0
num = int(input('Digite um Número [999 para parar]: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um Número [999 para parar]: '))
print('Voçê digitou {} números e a soma entre eles foi {}'.format(cont, soma))