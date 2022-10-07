listacars = []
listakm = []
dist = 500
kml = 4.90

while True:
    qtde = int(input('Quantos carros você quer calcular? ''\n'))
    for i in range(qtde):
        cars = input('Digite o nome do(s) carro(s): ''\n')
        listacars.append(cars)

    for x in range(qtde):
        print('Digite quantos quilometros o carro', listacars[x], 'faz por litro: ')
        km = int(input())
        listakm.append(km)

    print()
    print('Calculando para 500KMs...')
    print('========================================================')

    for x in range(qtde):
        print('Carro ', (x+1), ": ", listacars[x], '\nKM por litro: ', listakm[x], "\n", sep="")
    print('========================================================')

    for x in range(qtde):
        litros = dist / listakm[x]
        preco = litros * kml
        preco = float("{:.2f}".format(preco))
        print(listacars[x], ' - ', listakm[x], ' - ', round(litros), ' litros - R$ ', preco, "\n")

    parar = input('Continuar? (Digite SIM ou PARAR): ')
    if parar == 'sim':
        parar.upper()
        pass
    else:
        break
