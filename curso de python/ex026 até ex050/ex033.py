# Maior e Menor
a = input('Digite o primeiro valor: ')
b = input('Digite o segundo valor: ')
c = input('Digite o terceiro valor: ')
# verificando o Menor 
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# verificando o maior 
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c 
# imprimindo valores
print('O maior valor digitado foi {}'.format(maior))
print('O menor valor digitado foi {}'.format(menor))



