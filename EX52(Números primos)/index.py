numero = int(input('Digite um número: '))
total = 0
for contador in range(1, numero + 1):
    if numero % contador == 0:
        
        print('\033[33m', end='')
        total = total + 1 #total += 1
        
    else:
        print('\033[31m', end='')
    print('{}'.format(contador), end=' ')
print('\n \033[m O número {} foi divisível {} vezes'.format(numero, total))

if total == 2:
    print('E por isso ele é PRIMO!')
    
else:
    print('E por isso ele NÃO É PRIMO!')
    