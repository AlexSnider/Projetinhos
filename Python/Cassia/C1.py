import random
import time

def inicio():
    user_input = input('Olá, caro amigo! Vamos jogar dados!? (Digite "S" para SIM ou "N" para Não)\n').upper()
    while True:
        if user_input == 'N':
            print('Terminamos por aqui! Até mais!')
            break
        elif user_input == 'S':
            instrucoes()
            primeira_rodada()
            break
        else:
            inicio()

def instrucoes():
    print('Regras do jogo!!!')
    print('Iremos rolar 2 dados e somar seus pontos para poder prosseguir.')
    print('Se na primeira jogada você tirar [7 ou 11], você vence!')
    time.sleep(0)
    print('Se você tirar [2, 3 ou 12], você perde!')
    time.sleep(0)
    print('Se na primeira jogada você tirar [4, 5, 6, 8, 9 ou 10], esse é o seu [PONTO]!')
    time.sleep(0)
    print('Seu objetivo de agora em diante é tirar novamente esse [PONTO] '
          'e se tirar um 7 antes desse ponto, você perde!')
    time.sleep(0)

def primeira_rodada():
    input('Aperte ENTER para iniciar.')

    r1 = gera_num()
    r2 = gera_num()

    print('Sua primeira rodada de dados resultou em:', r1, '+', r2, '=', soma(r1, r2))

    p1 = soma(r1, r2)

    ganha = [7, 11]
    perde = [2, 3, 12]
    continua = [4, 5, 6, 8, 9, 10]
    perde2 = [7]

    for x in ganha:
        if x == soma(r1, r2):
            print('Você ganhou!')
            break

    for i in perde:
        if i == soma(r1, r2):
            print('Você perdeu!')
            break
   # Travei!

def gera_num():
    return random.randint(1, 6)

def soma(*valores):
    r = 0
    for i in valores:
        r += i
    return r

inicio()
