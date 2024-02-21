peso = float(input('Qual o seu peso ? (KG) '))
altura = float(input('Qual a sua altura ? (M) '))
imc = peso / (altura * altura )
print('O IMC dessa pessoa é {:.2f}'.format(imc))

if imc <= 18.5:
    print('Baixo peso!')

elif imc > 18.5 and imc <= 25:
    print('Peso adequado!')

elif imc > 25 and imc <= 30:
    print('Sobrepeso!')

else:
    print('Obesidade')
