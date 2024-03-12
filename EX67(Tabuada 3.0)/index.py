print('-----PROGAMA DA TABUADA-----')
while True:
    
    print('-='*20)
    núm = int(input('Digite um valor para ver a sua tabuada: '))
    print('-='*20)
    
    if núm < 0:
        break
    
    for contador in range (1, 11):
        print(f'{núm} x {contador} = {núm*contador}')
    
print('FIM DO PROGAMA DA TABUADA, VOLTE SEMPRE ')
