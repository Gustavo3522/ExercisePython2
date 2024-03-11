print('=' * 20)
print('10 TERMOS DE UMA PA')
print('=' * 20)

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
contador = 1
total = 0
mais = 10

while mais != 0:
    total = total + mais 
    while contador <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        contador += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais: '))
    
print('FIM')