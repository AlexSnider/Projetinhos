totalp = totalfsim = totalhnao = totals = totaln = 0
while True:
    idade = int(input('Qual a sua idade? '))
    sexo = ' '
    resp = ' '
    while sexo not in 'MF':
        sexo = input('Qual seu Sexo?: [M/F]: ').upper()
    while resp not in 'SNI':
        resp = input('Qual sua resposta sobre a empresa?: [S/N/I]: ').upper()
    if idade >= 1:
        totalp += 1
    else:
        print('=============================================================')
        print('Idade Inválida! Sua participação não será contabilizada.')
    if sexo == 'M' and resp == 'N' and idade >= 1:
        totalhnao += 1
    if sexo == 'F' and resp == 'S' and idade >= 1:
        totalfsim += 1
    if resp == 'S' and idade >= 1:
        totals += 1
    if resp == 'N' and idade >= 1:
        totaln += 1

    print('=============================================================')
    print('Total de participantes: ', totalp)
    print('A quantidade de Mulheres que disseram SIM foi de: ', totalfsim)
    print('A quantidade de Homens que disseram NÃO foi de: ', totalhnao)
    print('Total de pessoas que disseram SIM: ', totals)
    print('Total de pessoas que disseram NÃO: ', totaln)
    print('=============================================================')

    parar = input('Continuar a coleta de dados? (Digite SIM ou PARAR): ')
    if parar == 'sim':
        parar.upper()
        pass
    else:
        break
