print('=' * 20)
print('10 TERMOS DE UMA PA')
print('=' * 20)
termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
décimo = termo + (10 - 1) * razao
for contador in range (termo, décimo + razao, razao):
    print(contador, end=' -> ')
print('ACABOU')
