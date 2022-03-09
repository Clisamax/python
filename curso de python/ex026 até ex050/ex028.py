# Jogo da advinhação
from random import choice
from time import sleep
a = int(input('Escolha um numero de 0 a 5: '))
b = [0, 1, 2, 3, 4, 5]
escolhido = choice(b)
print('Você escolheu o numero:{}'.format(a))
print('Processando...')
sleep(3)
print('O numero sorteado foi:{}'.format(escolhido))
if a >= 6:
    print('Numero Inválido')
elif a == escolhido:
    print('Você Venceu')
elif escolhido != a:
    print('Você Perdeu')

