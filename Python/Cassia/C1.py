#Jogo de dados

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
            game()
            break
        else:
            inicio()

def instrucoes():
    print('Regras do jogo!!!')
    print('Iremos rolar 2 dados e somar seus pontos para pode prosseguir.')
    print('Se na primeira jogada você tirar 7 ou 11, você vence!')
    time.sleep(0)
    print('Se você tirar 2, 3 ou 12, você perde!')
    time.sleep(0)
    print('Se na primeira jogada você tirou 4, 5, 6, 8, 9 ou 10, esse é o seu [PONTO]!')
    time.sleep(0)
    print('Seu objetivo de agora em diante é tirar novamente esse [PONTO] '
          'e se tirar um 7 antes desse ponto, você perde!')
    time.sleep(0)

def game():
    while True:
        iniciar = input('Aperte ENTER para iniciar. '
                        'Se você não ganhar ou perder, o jogo continuará até você conseguir o seu [PONTO].')
        if iniciar == iniciar:
            jogada = roll() + roll()
            if jogada == 7:
                print('Tirou:', jogada, 'Ganhou!')
                break
            elif jogada == 11:
                print('Tirou:', jogada, 'Ganhou!')
                break
            else:
                print('*******************************')
                print('Somando os dados, você tirou:', jogada)
                print('*******************************')

def roll():
    return random.randint(1, 6)

inicio()
