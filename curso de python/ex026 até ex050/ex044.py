preço = float(input('Preço das compras: R$'))
print(''' Formas de pagamentos 
[1] à vista dinheiro/ cheque 
[2] à vista cartão 
[3] 2x no cartão 
[4] 3x ou mais no cartão ''')
opção = int(input('Qual é a opção: '))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
     total = preço + (preço * 5 / 100)
     
print(a)