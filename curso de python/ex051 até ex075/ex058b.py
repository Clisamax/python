from random import randint
com = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que voçê consegue adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == com:
        acertou = True
    else:
        if jogador < com:
            print('Mais... Tente mais uma vez.')
        elif jogador > com:
            print('Menos... Tente mais uma vez.')
            
print('Acertou com {} tentativas. Parabéns!'.format(palpites))   
     