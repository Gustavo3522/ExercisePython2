from random import randint
computador = randint(0, 10)
tentativas = 0 
print('Sou seu computador...')
print('Acabei de pensar em um número de 0 a 10, tente adivinhar.')
palpite = int(input('Qual e seu palpite ?  '))
while palpite is not computador :
    palpite = int(input('Tente mais uma vez '))
    tentativas += 1 
    if palpite == computador:
        print('PARABÉNS!, Você acertou ')
        print('Você presisou de {} tentativas'.format(tentativas))
        