a = []
mai = 0
men = 0
for i in range(0,5):
    a.append(int(input(f'Digite um valor para a posição {i}: ')))
    print(a)
    if i == 0:
        mai = men = a[0]
    else:
        if a[i] > mai:
            mai = a[i]
        if a[i] < men:
            men = a[i]
           
print(f'Voçê digitou os valores {a}')
print(f'O maior número digitado foi{mai} nas posições ', end = ' ')
for i , v in enumerate(a):
    if v == mai:
        print(f'{i}...', end = ' ')
print()
   
print(f'O menor número digitado foi {men} nas posições ', end = ' ')
for i , v in enumerate(a):
    if v == men:
        print(f'{i}...', end = ' ') 
print()
