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


def main():
    print('Olá!, Bem vindo ao jogo de adivinhação de palavras.')
    print('Você tem 6 tentativas para adivinhar qual é!')
    palavra_certa = escolhe_palavra(palavras())
    palavra_grafia_certa = palavra_certa
    embaralha(palavra_grafia_certa)
    game(palavra_grafia_certa)


def palavras():
    list_words = ['Venezuela', 'Protesto', 'Guerra', 'Brasil', 'Livre', 'Maracutaia', 'Corrupção',
                  'Insegurança', 'Inflação', 'CiroGomes']
    print('A palavra é alguma dessas:', list_words)
    return list_words


def escolhe_palavra(list_words):
    word = random.choice(list_words)
    return word


def embaralha(word):
    mixed_word = ''.join(random.sample(word, len(word)))
    print('A palavra a ser adivinhada é:', mixed_word)
    return mixed_word


def game(palavra_grafia_certa):
    tentativas = 0
    while True:
        user_input = input('Digita a palavra: ')
        if user_input not in palavra_grafia_certa:
            tentativas += 1
            print('Essa foi a sua', tentativas, 'tentativa. Continue tentando!')
        elif tentativas == 6:
            print('Você não acertou. A palavra era', palavra_grafia_certa)
            break
        elif user_input == palavra_grafia_certa:
            print('Você acertou! A palavra era:', '|', palavra_grafia_certa, '|')
            break



        # tentativas = 0
        # user_input = input('Digite a primeira tentativa: ')
        # while user_input not in palavra_grafia_certa:
        #     tentativas += 1
        #     print('Tentativa:', tentativas)
        #     user_input = input('Ainda não acertou. Continue tentando: ')
        #     if tentativas == 6:
        #         print('Você não acertou. A palavra era', palavra_grafia_certa)
        #         break
        #     if user_input == palavra_grafia_certa:
        #         print('Você acertou! A palavra era:', palavra_grafia_certa)
        #         break


main()
