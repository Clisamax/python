# Analizando triangulos
print('-='*20)
print('Analizador de Triângulos')
print('-='*20)
r1 = float(input('Primeiro Segmento: '))
r2 = float(input('Segundo Segmento: '))
r3 = float(input('Terceiro Segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos acima PODEM FORMAR triângulo! ')
else:
    print('Os seguimentos acima NÃO PODEM FORMAR triângulos!')
