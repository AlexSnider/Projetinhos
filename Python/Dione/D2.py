#2
# Desenvolva um método em Python que retorne uma matriz de m x n posições
# com valores inteiros aleatórios, m e n são recebidos como parâmetro.

# Desenvolva outro método que receba a matriz gerada no método anterior e
# retorne um vetor com os elementos pares e ímpares separados da matriz.

# Sugestão: no início do vetor armazene os elementos pares da matriz e nas posições
# restantes do vetor armazene os elementos da matriz que são ímpares.
# Vetor de retorno: [ 2, 4, 10, 20, 30, 40, 1, 3, 3, 5, 9, 17 ]

import random

lin = int(input('Defina a quantidade de linhas: '))
col = int(input('Defina a quantidade de colunas: '))


def gerar_numeros(m, n):
    m = 1
    n = 10
    return random.randint(m, n)


def gera_matriz(m, n):
    matriz = []
    for i in range(m):
        linMatriz = []
        for j in range(n):
            linMatriz.append(gerar_numeros(m, n))
        matriz.append(linMatriz)
    return matriz



def filtrar(x):
    par = []
    impar = []
    for i in x:
        if i % 2 == 0:
            par.append(i)
        else:
            impar.append(i)
    separate = [par, impar]
    return separate


print(filtrar(gera_matriz(lin, col)))

