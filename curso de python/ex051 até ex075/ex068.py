from random import randint
cont1 = cont2 =cont3 = 0
b = ' '
while True:
    a = int(input('Digite um valor: '))
    while b not in 'PI':
        b = str(input('Par ou Ímpar? [P/I]')).upper().strip()[0]
    n = randint(0, 10)   
    soma = a + n
    if b == 'P':
        if soma % 2 == 0:
            print('Voçê ganhou')
            cont1 += 1
        else:
            print('Voçê perdeu')
            break
    if b == 'I':
        if soma % 2 == 0:
            print('Voçê perdeu')
            break
        else:
            print('Voçê ganhou')
            cont2 += 1
print(f'Voçê escolheu {a} e o computador escolheu {n}', end = ' ' ) 
print(f' = {soma} DEU PAR' if soma % 2 == 0 else 'DEU ÌMPAR')
cont3 = cont1 + cont2
print(f'Game Over! Você venceu {cont3} vezes.')
