# custo de viagem
dist = float(input('Qual a distancia da viagem? '))
if dist <= 200:
    pas = dist * 0.50
    print('O valor da passagem sera de R${:.2f}'.format(pas))
else:
    pas = dist * 0.45
    print('O valor da passagem sera de R${:.2f}'.format(pas))