#jogo da adivinhaçao 2.0
from random import choice
a = 0
b = 0
com  = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num = int(input('''Sou seu computador...
Acabei de pensar em um numero entre 0 e 10.
Séra que voçê consegue adivinhar qual foi?
Qual é o seu palpite? '''))
escolhido = choice(com)
while num != escolhido:
    if num < escolhido:
        a += 1
        print('Mais... Tente mais uma vez.')
        num = int(input('Qual é o seu palpite: '))
    if num > escolhido:
        b += 1
        print('Menos... Tente mais uma vez.')
        num = int(input('Qual é o seu palpite:'))
if num == escolhido:
    tot = a + b + 1
    print('Acertou com {} tentativas. Parabéns!'.format(tot))