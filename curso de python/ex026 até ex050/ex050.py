soma = 0
cont = 0
for c in range (1, 7):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Voçê informou {} números pares e a soma deles foi {}'.format(cont, soma))