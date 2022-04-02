while True:  
    print('-' * 30)    
    num = int(input('Quer ver a tabuada de qual valor? ')) 
    print('-' * 30)    
    if num < 0:
        break     
    for c in range(1,11):
        tot = num*c        
        print(f'{num} x {c}  = {tot}')  
print('-' * 30)    
print('Programa encerado com sucesso')     
print('-' * 30)    
  
        
    