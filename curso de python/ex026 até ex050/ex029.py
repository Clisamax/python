# radar eletronico
vel = int(input('Velocidade apurada: '))
if vel > 80:
    print('Voçê foi multado por velocidade superior a permitida de 80 Km/h')
    a = (vel - 80) * 7
    print('Você foi multado em R${:.2f}'.format(a))
else:
    print('Tenha um bom dia dirija com segurança! ')

