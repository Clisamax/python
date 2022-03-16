# calculando emprestimo
a = float(input('Qual o valor do imovel R$: '))
b = float(input('qual a sua renda R$: '))
c = int(input('Em quantos anos deseja pagar R$: '))
d = a / (c * 12)
if d <= (b * 30 / 100):
    print('Valor mensal sera de R${:.3f}'.format(d))
else:
    print('Infelimente o valor de R${:.3f} é superior a'.format(d), '30%', 'da sua renda')