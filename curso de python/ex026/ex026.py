# Primeira e a ultima ocorencia de uma string
frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} veses na frase.'.format(frase.count('A')))
print('A primeira  letra A apareceu na posição {}'.format(frase.find('A') + 1))
print('A Última letra A apareceu na posição {}'.format(frase.rfind('A') + 1))


