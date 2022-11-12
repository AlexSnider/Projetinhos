# Desenvolva um jogo em que o jogador tenha que adivinhar uma palavra que será mostrada na tela com as letras
# embaralhadas. No programa deverá possuir funções para:
# - preencher uma lista de palavras (contendo no mínimo 10
# palavras!)
# - escolher uma das palavras da lista aleatoriamente (função recebe uma lista e retorna o índice da
# palavra selecionada na lista para o jogador adivinhar);
# - embaralhar uma palavra passada por parâmetro – o critério
# de embaralhar deve ser criado pelo desenvolvedor (a função recebe a palavra que foi escolhida com a grafia correta
# e retorna a palavra embaralhada);
# - jogar, onde o jogador terá seis tentativas para adivinhar a palavra (recebe a
# palavra escolhida com a grafia correta por parâmetro e retorna o resultado true (se o jogador venceu) ou false (se
# o jogador perdeu)).
# Quando iniciar o jogo, o programa escolherá uma das palavras da lista (aletoriamente) e a exibirá embaralhada ao
# jogador. O jogador terá seis tentativas para adivinhar a palavra. Ao final, a palavra com a grafia correta deve ser
# mostrada na tela, informando se o jogador ganhou ou perdeu o jogo.

import random


def inicio():
    user_input = input('Vamos jogar? (Digite "S" para SIM ou "N" para Não): ').upper()
    while True:
        if user_input == 'N':
            print('Terminamos por aqui! Até mais!')
            break
        elif user_input == 'S':
            continua()
            break
        else:
            inicio()
            break


def continua():
    print('-=' * 30)
    print('Olá!, Bem vindo ao jogo de adivinhação de palavras.')
    print('Você tem 6 tentativas para adivinhar qual é!')
    print('Você precisa inserir 10 palavras...')
    palavra_certa = escolhe_palavra(palavras())
    palavra_grafia_certa = palavra_certa
    embaralha(palavra_grafia_certa)
    if game(palavra_grafia_certa) == True:
        print('Você acertou! A palavra era:', '>', palavra_grafia_certa, '<')
        print('-=' * 30)
        inicio()
    else:
        print('Você perdeu! A palavra era:', palavra_grafia_certa)
        print('-=' * 30)
        inicio()


def palavras():
    cont = 1
    list_words = []
    while cont <= 10:
        user_input = input('Insira a palavra: ')
        print('Você inseriu a palavra número:', cont)
        cont += 1
        list_words.append(user_input)
    return list_words


def escolhe_palavra(list_words):
    word = random.choice(list_words)
    return word


def embaralha(word):
    mixed_word = ''.join(random.sample(word, len(word)))
    print('-=' * 30)
    print('A palavra a ser adivinhada é:', mixed_word)
    print('-=' * 30)
    return mixed_word


def game(palavra_grafia_certa):
    tentativas = 0
    while True:
        user_input = input('Digite a palavra que você acha ser: ')
        if user_input not in palavra_grafia_certa:
            tentativas += 1
            print('Essa foi a sua', tentativas, 'tentativa.')
        if tentativas >= 6:
            return False
        if user_input == palavra_grafia_certa:
            return True


inicio()
