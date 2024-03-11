contador = 0 
numero = 0
soma = 0 
numero = int(input('Digite um valor [999 PARA PARAR O PROGAMA ]: '))
while numero != 999: 
    soma += numero
    contador += 1 
    numero = int(input('Digite um valor [999 PARA PARAR O PROGAMA ]: '))
print('Você digitou {} números e a soma deles é {}'.format(contador, soma))
print('FIM')