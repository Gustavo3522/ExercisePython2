from random import randint
from time import sleep
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=') 
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')

escolha = int(input('Qual é a sua jogada ? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')

print('-=' * 11) 
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[escolha]))
print('-=' * 11) 

if computador == 0:
    if escolha == 0:
        print('EMPATE')
    elif escolha == 1:
        print('JOGADOR VENCEU')
    elif escolha == 2:
        print('COMPUTADOR VENCEU')
    else:
        print('JOGADA INVÁLIDA!')       
elif computador == 1:
    if escolha == 0:
        print('COMPUTADOR VENCEU')
    elif escolha == 1:
        print('EMPATE')
    elif escolha == 2:
        print('JOGADOR VENCEU')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2:
    if escolha == 0:
        print('JOGADOR VENCEU')
    elif escolha == 1:
        print('COMPUTADOR VENCEU')
    elif escolha == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA!')
