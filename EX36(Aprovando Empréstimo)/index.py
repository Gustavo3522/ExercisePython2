casa = int(input('Qual o valor da casa ? '))
salario = int(input('Qual o seu salario ? '))
anos = int(input('Em quantos anos você quer pagar ? '))
prestação = casa / (anos * 12)
porcentagem = 30 * salario / 100
print('Para pagar a casa de R${:.2f} em {} anos a prestação será de R${:.2F}.'.format(casa, anos, prestação))
if prestação >= porcentagem:
    print('Empréstimo NEGADO !')
else:
    print('Emprestimo CONCEDIDO !')