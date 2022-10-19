# lin = 3
# col = 4
# matriz = []
#
# for l in range(lin):
#     linmatriz = []
#
#     for c in range(col):
#         linmatriz.append((c+1)*l)
#     matriz.append(linmatriz)
#
# # matriz[2][1] = 13 # adicionar números a matriz de forma substituta
#
# # for i in matriz: # exibir a matriz de forma lin e col
# #     print(i)
#
# for i in range(len(matriz)): # imprimir a matriz sem colchete
#     print()
#     for j in range(len(matriz[i])):
#         print(matriz [i][j], end='')
import random
# import random
#
# def gera():
#     return random.randint(1, 6)
#
# def repete(n):
#     test1 = test2 = test3 = \
#         test4 = test5 = test6 = 0
#     for val in range(n):
#         test = gera()
#
#         if (test == 1):
#             test1 += 1
#         elif (test == 2):
#             test2 += 1
#         elif (test == 3):
#             test3 += 1
#         elif (test == 4):
#             test4 += 1
#         elif (test == 5):
#             test5 += 1
#         else:
#             test6 += 1
#
#     print("Numero 1 saiu ", test1, " vezes = ", (test1 / n) * 100, " %")
#     print("Numero 2 saiu ", test2, " vezes = ", (test2 / n) * 100, " %")
#     print("Numero 3 saiu ", test3, " vezes = ", (test3 / n) * 100, " %")
#     print("Numero 4 saiu ", test4, " vezes = ", (test4 / n) * 100, " %")
#     print("Numero 5 saiu ", test5, " vezes = ", (test5 / n) * 100, " %")
#     print("Numero 6 saiu ", test6, " vezes = ", (test6 / n) * 100, " %")
#
# def menu():
#     n = int(input('Quantos lançamentos de dado? '))
#     repete(n)
#
# menu()

import random # not finished!

def gera():
    return random.randint(1, 6)

def repete(lan):
    lan1 = lan2 = lan3 = lan4 = lan5 = lan6 = 0
    for num in range(lan):
        lanca = gera()

        if lanca == 1:
            lan1 += 1
        if lanca == 2:
            lan2 += 1
        if lanca == 3:
            lan3 += 1
        if lanca == 4:
            lan4 += 1
        if lanca == 5:
            lan5 += 1
        else:
            lan6 += 1

    print(lan1)
    print(lan2)
    print(lan3)
    print(lan4)
    print(lan5)
    print(lan6)

def roll():
    lan = int(input('Quantos lançamentos de dado? '))
    repete(lan)

roll()