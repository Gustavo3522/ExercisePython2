soma = 0
for contador in range(1, 7):
    numeros = int(input('Digite um número: '))
    if  numeros % 2 == 0:
        soma = soma + numeros 
print('A soma dos números pares é {}'.format(soma))

    