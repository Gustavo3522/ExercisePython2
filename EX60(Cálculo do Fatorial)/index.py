from math import factorial

numero = int(input('Digite um número para calcular o seu fatorial: '))
f = factorial(numero)
c = numero

print('Calculando {}! = '.format(numero), end='')

while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    c -= 1
    
print('{}'.format(f))
