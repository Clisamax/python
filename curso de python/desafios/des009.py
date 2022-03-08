'''co= float(input('Qual o tamanho do cateto oposto? ')) 
ca = float(input('Qual o tamanho do cateto adjacente? '))
h = (co**2 + ca**2) **(1/2)
print('A hipotenusa vai medir:{:.2f}'.format(h))'''

import math
ca= float(input('Qual é o tamanho do cateto adjacente? '))
co= float(input('Qual é o tamanho do cateto oposto? '))
hi= math.hypot(co, ca)
print('A hipotenusa vai medir:{:.2f}'.format(hi))