#Primeiro e ultimo nome de uma pessoa
n = str(input('Digite seu nome completo: '))
nome = n.split()
print('Muito prazer em conhecer! ')
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))
