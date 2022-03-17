peso = float(input('Qual é o seu peso? (Kg): '))
alt = float(input('Qual é a sua altura (M): '))
imc = peso / (alt ** 2)
if imc < 18.5:
    input('IMC {:.2f} Abaixo do Peso'.format(imc))
elif imc > 18.5 and imc < 25:
    print('IMC {:.2f} Peso Ideal'.format(imc))
elif imc > 25 and imc < 30:
    print('IMC {:.2f} Sobrepeso'.format(imc))
elif imc > 30 and imc < 40:
    print('IMC {:.2f} Obesidade'.format(imc))
else:
    print('IMC {:.2f} Obesidade Mórbida'.format(imc))