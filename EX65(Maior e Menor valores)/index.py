resposta = "S"
soma = quant = media = maior_num = menor_num = 0

while resposta in 'Ss':
    
    numero = int(input('Digite um número: '))
    soma += numero 
    quant += 1
    
    if quant == 1:
        maior_num = menor_num = numero
    else:
        if numero > maior_num:
            maior_num = numero
            
        if numero < menor_num:
            menor_num = numero 
            
    resposta = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]  

media = soma / quant     

# print('Você digitou {} números'.format(contador))
# print('A soma desses números deu {}'.format(soma))
# print('A media desses números é de {:.2f}'.format(media))
# print('O maior número foi {}'.format(maior_num))
# print('O menor número foi {}'.format(menor_num))

print('Você digitou {} números e a media entre eles foi de {:.2f}'.format(quant, media))
print('O maior valor foi {} e o menor valor foi {} '.format(maior_num, menor_num))
print('FIM')
