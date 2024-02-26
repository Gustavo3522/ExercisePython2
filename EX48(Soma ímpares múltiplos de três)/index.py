soma = 0
Contador = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma = soma + c
        Contador = Contador + 1
print('A soma de todos os {} valores solicitados é {}'.format( Contador, soma))
    