soma_idade = 0
media = 0
maior_idade_homem = 0
nome_velho = ''
total_mulher20 = 0

for pessoa in range(1, 5):
    print('---------- {}° PESSOA ----------'.format(pessoa))
    
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    soma_idade += idade 
    
    
    if pessoa == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_velho = nome
        
    if sexo in 'Mm' and idade > maior_idade_homem:
            maior_idade_homem = idade 
            nome_velho = nome
            
    if sexo in 'Ff' and idade < 20:
                total_mulher20 += 1
                
media = soma_idade / 4
print('A média de idade do grupo é de {} anos'.format(media))
print('A idade do homem mais velho é {} e seu nome é {}.'.format(maior_idade_homem, nome_velho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(total_mulher20))
