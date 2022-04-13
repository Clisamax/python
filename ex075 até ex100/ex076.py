lista = ('Lápis', 1.75, 'Borracha', 2, 'Carderno', 15.90, 'Estojo', 25, 'Trasferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90 )
print('-' * 40)
# mostrando com 40 espaços alinhado ao centro ( ^ ).
print(f'{"Listagem de preços":^40}')
print('-' * 40)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end=' ')
# ( < ) alinhado a esquerda.( > ) alinhado a direita.
    else:
# 7 espaços alinhado a direita ( >7 ) formatado com 2 casas decimais ( .2f ).
        print(f'R${lista[pos] : >7.2f}')

