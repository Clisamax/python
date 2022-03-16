# alistamento militar
from datetime import date
anoNasc = int(input('Digite seu ano de nascimento: '))
sexo = int(input('escolha masc [1] ou fen [2]:  '))
anoAtual = date.today().year
idade = anoAtual - anoNasc
if sexo == 1:
    if idade < 18:
        a = 18 - idade 
        b = anoAtual + a
        print('Ainda faltam {} anos para o alistamento'.format(a))
        print('voçê se alistará em {}'.format(b))
    elif idade > 18:
        a = idade - 18
        b = anoAtual - a 
        print('Voçê já deveria ter se alistado há {} anos'.format(a))
        print('Seu alistamento foi em {}'.format(b)) 
    else:    
        print('Voçê deve se alistar IMEDIATAMENTE! ')  
if sexo == 2:
    print('Voçê é mulher e o alistamento não é OBRIGATÓRIO. ')  
 