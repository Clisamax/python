print('-' * 20)
print('LOJAS MKAGOMES')
print('-' * 20)
total = preço = totMil = menor = cont = 0 
barato = ' '
while True:
    prod = str(input('Nome do produto: '))    
    preço = float(input('Preço: '))
    cont += 1
    total += preço
    resp = prod = ' '
    if preço > 1000:
        totMil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = prod
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'O total da compra foi R${total:.2f}')
print(f' Temos {totMil} produtos custando mais de R$1000.00')
print(f'O produto mais barato custa R${menor:.2f}')