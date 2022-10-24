#Jogo de dados

import random
import time

def entrada():
    user_input = input('Olá, caro amigo! Vamos jogar dados!? (Digite "S" para SIM ou "N" para Não)\n').upper()
    if user_input == 'N':
        print('Terminamos por aqui! Até mais!')
    elif user_input == 'S':
        instrucoes()
        pass
    else:
        entrada()
def instrucoes():
    print('Regras do jogo!!!')
    print('Se na primeira jogada você tirar 7 ou 11, você vence!')
    time.sleep(3)
    print('Se você tirar 2, 3 ou 12, você perde!')
    time.sleep(3)
    print('Se na primeira jogada você tirou 4, 5, 6, 8, 9 ou 10, esse é o seu [PONTO]!')
    time.sleep(4)
    print('Seu objetivo de agora em diante é tirar novamente esse [PONTO] '
          'e se tirar um 7 antes desse ponto, você perde!')
    time.sleep(4)
    print('Vamos lá! Aperte ENTER para jogar os dados!')

def gerador():
    return random.randint(2, 12)

entrada()
