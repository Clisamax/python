# analizador completo
somaidade = 0
médiaidade = 0
maioridadeDeHomen = 0
nomeVelho = ' '
totMulher20 = 0
for c in range(1, 5):
    print('------{}° PESSOA-------'.format(c))
    nome = str(input(' nome: ')).upper()
    idade = float(input(' idade: '))
    sexo = str(input(''' sexo: [M] masculino [F] feminino: ''')).upper()
    somaidade += idade
    if c == 1 and sexo == 'M':
        maioridadeDeHomen = idade
        nomeVelho = nome
    if sexo == 'M' and idade > maioridadeDeHomen:
        maioridadeDeHomen = idade
        nomeVelho = nome
    if sexo in 'Ff' and idade < 20:
        totMulher20 += 1
médiaidade = somaidade / 4
print('A média de idade do grupo é de {} anos'.format(médiaidade))
print('O homen mais velho tem {} anos  e se chama {}'.format(maioridadeDeHomen, nomeVelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totMulher20))
