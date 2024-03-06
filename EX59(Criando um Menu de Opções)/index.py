valor1 = int(input('Primeiro valor: '))
valor2 = int(input('Segundo valor: '))

opção = 0

while opção != 5:
    print('''
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR 
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGAMA''')
    
    opção = int(input('Qual é a sua escolha ? '))
    
    if opção == 1:
        print('{} + {} = {}'.format(valor1, valor2, valor1 + valor2))
        print('='*20)
        
    elif opção == 2:
        print('{} x {} = {}'.format(valor1, valor2, valor1 * valor2))
        print('='*20)
        
    elif opção == 3:
        if valor1 > valor2:
            print('O número {} é maior'.format(valor1))
            
        elif valor1 < valor2:
            print('O número {} é maior'.format(valor2))
            
        else: 
            print('Os números são iguais ')
        print('='*20)
        
    if opção == 4:
        valor1 = int(input('Primeiro valor: '))
        valor2 = int(input('Segundo valor: '))
        
print('Fim do progama, volte sempre !')
