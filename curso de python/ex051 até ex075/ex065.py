resp = 's'
soma = média = quant = menor = maior = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
média = soma / quant
print('Voçê digitou {} números e a média foi {}'.format(quant, média))
print('O maior número foi {} e o menor foi {}.'.format(maior, menor))