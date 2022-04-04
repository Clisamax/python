print('-' * 20)
print('LOJAS MKAGOMES')
print('-' * 20)
resp = prod = ' '
prec = tot = prodMB = 0
while True:
    prod = str(input('Nome do produto: '))    
    prec = float(input('Preço: '))
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
