from datetime import date
ano_atual = date.today().year
total_maior = 0
total_menor = 0

for contador in range(1, 8):
    ano_nascimento = int(input('Em que ano a {}° pessoa nasceu: '.format(contador)))
    idade = ano_atual - ano_nascimento 
    
    if idade >= 18:
        total_maior += 1 
        
    else:
        total_menor += 1 
        
print('Ao todo tivemos {} pessoas maiores de idade'.format(total_maior))
print('E também  tivemos {} pessoas menores de idade'.format(total_menor))
