import random

def gerar_numeros():
    return random.randint(10, 50)

def gerar_matriz():
    lin = int(input('Defina a quantidade de linhas: '))
    col = int(input('Defina a quantidade de colunas: '))
    matriz = []

    for i in range(lin):
        linMatriz = []
        for c in range(col):
            linMatriz.append((gerar_numeros()))
        matriz.append(linMatriz)
    print(matriz)


gerar_matriz()

