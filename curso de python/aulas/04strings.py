#strings
frase = 'Curso em Vídeo Python'
# fatiamento
frase[9]
frase[9:13] # começa no 9 e vai até o 12
frase[9:21:2] # do 9 ao 20 pulando de dois em dois
frase[:5] # começar do 0 até o 4
frase[0: ] # começa no 0 e vai até o final
frase[9::3] # começa no 9 vai até o final pulando de dois em dois
len(frase) # tamanho de frase
frase.count('o') # quantos 'o' existe na frase
frase.conut('o',0,13) # quantos ''o existem entre 0 e 12
frase.find('deo') # em que posição ele encontrou 'deo' 
frase.find('Android') # quando a busca não se encontra na frase. retorna o valor -1 
'curso' in frase # existe 'curso' em frase

# transformação de strings

frase.replace('Python', 'Android')# trocar python por android
frase.upper() # transformar em maiuscula
frase.lower() # transforma em minuscula
frase.capitalize() # só a primeira letra da frase em maiuscula
frase.title() # todas as primeiras letras da frase em maiuscula
frase.strip() # remove espaços inúteis na frase
frase.rstrip() # remove espaços inúteis na direita
frase.lstrip() # remove espaços inúteis na esquerda

'-'.join(frase) # junta adicionando - no lugar dos espaços



