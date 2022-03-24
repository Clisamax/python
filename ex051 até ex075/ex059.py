# criando menu de opções
from time import sleep
res = 0
maior = 0
menor = 0
esc = 0
num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
while esc !=5:
    esc = int(input('''
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do pograma
    >>> Qual sua opção? '''))
    print('==' * 20)
    if esc == 1:
        res = num1 + num2
        print(res)
    elif esc == 2:
        res = num1 * num2
        print(res)
    elif esc == 3:
        if num1 == num2:
            print('Os numeros são iguais.')
            print('==' * 20)
        elif num1 < num2:
            menor = num1 
            maior = num2
            print('O menor é {} e maior o  é {}'.format(menor, maior))
            print('==' * 20)
        else:
            menor = num2
            maior = num1
            print('O menor é {} e maior o  é {}'.format(menor, maior))
            print('==' * 20)
    elif esc == 4:
            num1 = int(input('Primeiro valor: '))
            num2 = int(input('Segundo valor: '))
    elif esc == 5: 
        print('Finalizando...')
        sleep(2)
        print('Programa encerado com sucesso')
        print('==' * 20)
    else:
        print('Escolha inválida, Tende denovo')
        print('==' * 20)
        

     