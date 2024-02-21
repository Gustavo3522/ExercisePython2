nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
print('A média da escola e de 7.0, tirando {:.1f} e {:.1f} sua média foi de {:.1f}'.format(nota1, nota2, media))

if media >=5.0 and media < 7 :
    print('Aluno de recuperação!')

elif media >= 7: 
    print('Aluno aprovado, PARABÉNS!')

else:
    print('Aluno reprovado!')
