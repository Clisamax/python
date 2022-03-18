# gerenciador de pagamentos
print('{:=^40}'.format('LOJAS MKAGOMES'))  
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
elif opção == 3:
    parcela = preço / 2
    total = preço 
    print('Sua compra será parcelada em 2x de {:.2f}'.format(parcela))
elif opção == 4:
    total = preço + (preço * 30 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de {:.2f}'.format(totparc, parcela))
else:
    total = preço 
    print('OPÇÃO INVÁLIDA, TENTE NOVAMENTE!')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, total))  
