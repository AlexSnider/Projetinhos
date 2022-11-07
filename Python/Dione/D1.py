# Escrever um programa que gere valores aleatórios para uma matriz de inteiros.
# Após, exiba para cada linha, o percentual de valores pares e o percentual de valores ímpares.

import random


def main():
    print('Insira o tamanho da matriz.\n')
    lin = int(input('Defina a quantidade de linhas: '))
    col = int(input('Defina a quantidade de colunas: '))
    input('Aperte ENTER para gerar os dados da Matriz e seus percentuais.')
    matriz = gerar_matriz(lin, col)
    imprime_matriz(matriz, lin, col)
    percentual(matriz, lin, col)


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


def imprime_matriz(matriz, m, n):
    count = 0
    for i in range(m):
        linha = ''
        count += 1
        for j in range(n):
            linha += str(matriz[i][j])
            linha += ' | '
        print('Linha:', count, '= |', linha)


def percentual(matriz, m, n,):
    count = 0
    total = n
    for i in range(m):
        count += 1
        totalPar = 0
        totalImpar = 0
        for j in range(n):
            if matriz[i][j] % 2 == 0:
                totalPar += 1
            else:
                totalImpar += 1
        print()
        print("Porcentagem de números pares na linha:", count, ('= %.2f' % (totalPar / total * 100.0)), '%')
        print("Porcentagem de números ímpares na linha:", count, ('= %.2f' % (totalImpar / total * 100.0)), '%\n')


main()
