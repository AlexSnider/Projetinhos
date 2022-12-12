import random


def inicio():
    user_input = input('Olá, caro amigo! Vamos jogar dados!? '
                       '(Digite "S" para SIM ou "N" para Não)\n').upper()
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
    print('*' * 18)
    print('Regras do jogo!!!')
    print('*' * 18)
    print('Iremos rolar 2 dados e somar seus pontos para poder prosseguir.')
    print('Se na primeira jogada você tirar [7 ou 11], você vence!')
    print('Se você tirar [2, 3 ou 12], você perde!')
    print('Se na primeira jogada você tirar [4, 5, 6, 8, 9 ou 10], esse é o seu [PONTO]!')
    print('Seu objetivo de agora em diante é tirar novamente esse [PONTO] '
          'e se tirar um 7 antes desse ponto, você perde!')
    print('*' * 109)


def game():
    ganha = [7, 11]
    perde = [2, 3, 12]
    pontoFeito = [4, 5, 6, 8, 9, 10]

    while True:
        input('Aperte ENTER para rolar os dados pela primeira vez!')
        dados = soma(gera_num(), gera_num())
        print('*' * 51)
        print("Dados lançados e o valor deu a soma:", '[', dados, ']', 'e esse é o seu [PONTO].')
        if dados in ganha:
            print('*' * 69)
            print('É isso aí! Você venceu porque tirou:', dados)
            print('*' * 38)
            break
        if dados in perde:
            print('*' * 27)
            print('Você perdeu por que tirou:', dados)
            print('*' * 27)
            break
        if dados in pontoFeito:
            print('*' * 62)
            input('Aperte ENTER para continuar!')
            print('*' * 30)
            ponto = dados
            dado = 0
            while dado not in [ponto, 7]:
                dado = soma(gera_num(), gera_num())
                print('O lançamento dos dados resultou em:', '[', dado, ']')
                print('*' * 30)
                input('Aperte ENTER para continuar!')
                print('*' * 30)
            if dado == 7:
                print("Você perdeu porque tirou: [7] antes de tirar seu [PONTO]")
                print('*' * 30)
                inicio()
                break
            else:
                print('Você venceu porque tirou novamente o seu [PONTO] que foi:', '[', dado, ']',
                      'antes de tirar [7].')
                print('*' * 30)
                inicio()
                break


def gera_num():
    numAleatorio = random.randint(1, 6)
    return numAleatorio


def soma(*valores):
    r = 0
    for i in valores:
        r += i
    return r


inicio()
