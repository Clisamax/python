print('-' * 20)
print('Cadastre uma pessoa')
print('-' * 20)
while True:
    i = int(input('Idade: '))
    s = str(input('Sexo: [M/F]')).upper().strip()
    r = input('Quer continuar? [S/N]').upper().strip()
    if r == 'N':
        break
