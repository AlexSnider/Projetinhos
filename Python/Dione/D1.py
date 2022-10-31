# Escrever um programa que gere valores aleatórios para uma matriz de inteiros.
# Após, exiba para cada linha, o percentual de valores pares e o percentual de valores ímpares.

import random

lin = int(input('Defina a quantidade de linhas: '))
col = int(input('Defina a quantidade de colunas: '))


def gerar_numeros(m, n):
    m = 10
    n = 50
    return random.randint(m, n)


def gerar_matriz(m, n):
    matriz = []
    for i in range(m):
        linMatriz = []
        for j in range(n):
            linMatriz.append(gerar_numeros(m, n))
        matriz.append(linMatriz)
    return matriz

print(gerar_matriz(lin, col))

