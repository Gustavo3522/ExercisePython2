from datetime import date

print('''Escolha uma opção
[1] HOMEM
[2] MULHER''')
opção = int(input('Sua opção: '))

if opção == 1:
    ano_nascimento = int(input('Ano de nascimento: '))
    idade = date.today().year - ano_nascimento
    tempo_restante = 18 - idade
    tempo_passado = idade - 18
    print('Quem nasceu em {} tem {} anos em {}.'.format(ano_nascimento, idade, date.today().year))

    if idade < 18:
       print('Ainda faltam {} anos para o alistamento'.format(tempo_restante))
    
    elif idade == 18:
       print('Seu alistamento é nesse ano')

    elif idade > 18:
       print('Você deveria ter se alistado a {} anos '.format(tempo_passado))

else:
   print('Você não é obrigada a se alistar !')
