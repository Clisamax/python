a = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'outo', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte' )
num = int(input('digite um numero entre 0 e 20: '))
if num < 0 or num > 20:
    while True:
        num = int(input('Tente novamente. Digite um numero entre 0 e 20: '))
        if  0 <= num and num <= 20:
            break
b = a[num]
print(f'Voçê digitou o número {b}')