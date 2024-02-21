from datetime import date
ano_nascimento = int(input('Ano de nascimento do atleta de Judô: '))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento

print('O atleta tem {} anos.'.format(idade))

if idade <= 10:
     print('Classificação: INFANTIL')

elif idade >= 11 and idade <=12:
    print('Classificação: SUB 13')

elif idade >= 13 and idade <= 14:
    print('Classificação: SUB 15')

elif idade >= 15 and idade <= 17:
    print('Classificação: SUB 18')

elif idade >= 18 and idade <= 20:
    print('Classificação: SUB 21')

elif idade >= 21 and idade <= 22:
    print('Classificação: SUB 23')

else:
     print('Classificação: SENIOR')
