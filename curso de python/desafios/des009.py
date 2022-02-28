co = float(input('Qual o tamanho do cateto oposto? '))
ca = float(input('Qual o tamanho do cateto adjacente? '))
h = (co**2 + ca**2) **(1/2)
print('A hipotenusa vai medir:{:.2f}'.format(h))