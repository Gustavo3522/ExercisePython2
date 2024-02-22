print('========== LOJA DO GUSTAVO ==========')
preço = float(input('Preço das compras: '))
opção_pagamento = int(input('''FORMA DE PAGAMENTO
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão
Qual é a sua opção: '''))

if opção_pagamento == 1:
    total = preço - (preço * 10 / 100)

elif opção_pagamento == 2: 
     total = preço - (preço * 5 / 100)

elif opção_pagamento == 3:
     total = preço
     parcela = preço / 2
     print('Sua compra será parcelada em 2x no cartão de {:.2f} e ficara {:.2f} SEM JUROS'.format(parcela, preço))

elif opção_pagamento == 4:
     total_parcelas = int(input('Quantas parcelas ? '))
     total = preço + (preço * 20 / 100)
     parcela = total / total_parcelas
     print('Sua compra será parcelada em {:.2f} no cartão e ficara {:.2f}'.format(total_parcelas, parcela))
else:
     total = preço
     print('OPÇÃO INVÁLIDA de pagamento. tente novamente!')

print('Sua compra de {:.2f} vai custar {:.2f} no final.'.format(preço, total))
