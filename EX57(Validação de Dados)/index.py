sexo = str(input('Digite o seu sexo [M/F]: ')).upper().strip()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados invalidos. Por favor, informe seu sexo: ')).upper().strip()[0]
print('Sexo {} foi registrado com sucesso'.format(sexo))
