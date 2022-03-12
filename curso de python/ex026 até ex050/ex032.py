# Ano bissexto
ano = int(input('digite o ano quer analizar: '))
if ano % 4 == 0 and ano % 100 !=0 or ano % 400 ==0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} não é BISSEXTO'.format(ano))
