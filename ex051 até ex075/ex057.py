# validação de dados
# while sexo not in 'MmFf':
sexo = str(input('Informe seu sexo: [M/F]')).strip().upper()[0]
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).upper()
print('Sexo {} resgistrado com sucesso'.format(sexo))