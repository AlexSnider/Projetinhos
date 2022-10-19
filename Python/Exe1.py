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

###########################################################################################

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
