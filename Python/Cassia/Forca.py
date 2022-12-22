# 1 - create a menu that calls functions and execute it, and after, return to the menu if the game isn't called.
# 2 - create a function that writes random words from the user input and store it in a txt. file
# 3 - create a func. that loads the main file, allows to continue if the txt. file has more >= than 10 words,
#     and if not,
#     keep asking the user to insert new words until it reaches 10 in total but not overwriting the first words
#     already inserted
# 4 - create a func. that erases all the words in the txt. file if the user press the menu key for it
# 5 - create a func. that calls a hangman game using the words in the txt. file

import random
import time


def main():
    menu()


def menu():
    print('-=' * 20)
    print('Welcome! Select a number to start...')
    print('-=' * 20)
    print('Insira o número (1) para inserir palavras em um arquivo que será salvo em txt.')
    print('Insira o número (2) para carregar o arquivo txt na memória.')
    print('Insira o número (3) para limpar o arquivo.')
    print('Insira o número (4) para iniciar o game da forca usando as palavras do arquivo txt.')
    print('Insira o número (5) para encerrar a aplicação.')
    print('-=' * 20)

    try:
        user_input = int(input('Insira um número correspondente a função do menu acima: '))
        if int(user_input) >= 6 or int(user_input) <= 0:
            print('#' * 25)
            print('Digite números de 1 à 5!'.upper())
            print('#' * 25)
            time.sleep(1.5)
            return menu()
        if user_input == 1:
            return insert_words(), load_file(), menu()
        if user_input == 2:
            return load_file(), menu()
        if user_input == 3:
            return clean_file(), menu()
        if user_input == 4:
            return game(), menu()
        if user_input == 5:
            quit('Programa encerrado!')
    except ValueError:
        print('#' * 25)
        print('Digite apenas números...'.upper())
        print('#' * 25)
        time.sleep(1.5)
        return menu()


def insert_words():
    print('Digite palavras aleatórias e aperte ENTER para salvar ou digite (DONE) para encerrar a inserção: ')
    user_input = str(input('Insira palavras para serem usadas no game da forca: '))

    palavras_arq = open('palavras.txt', 'w', encoding='utf-8')

    while user_input != 'done' and user_input != 'Done' and user_input != 'DONE':
        palavras_arq.write(user_input)
        palavras_arq.write('\n')
        user_input = str(input('Insira palavras para serem usadas no game da forca: '))


def load_file():
    with open('palavras.txt', 'r', encoding='utf-8') as arq:
        arq.read()
        arq.seek(0, 0)
        l_arq = arq.readlines()

        lista_arq = []
        if len(l_arq) >= 10:
            for x in range(len(l_arq)):
                lista_arq.append(l_arq[x].split())
            print('-=' * 20)
            print('Arquivo carregado para o jogo.')
            return lista_arq
        elif len(l_arq) < 10:
            need_lines = 10 - len(l_arq)
            print('O arquivo parace não conter aquivos ou menos de 10 (10 é o mínimo para iniciar o game).')
            print('Você ainda precisa de mais:', need_lines, '- Por favor, insira o restante.')
        for word in l_arq:
            lista_arq.append(word.replace('\n', ''))
        if need_lines != 0:
            for i in range(need_lines):
                with open('palavras.txt', 'a') as arq2_app:
                    user_input = input('Insira as palavras restantes: ')
                    while user_input.isnumeric() or user_input == '':
                        print('Digite apenas palavras!')
                        user_input = input('Insira as palavras restantes: ')
                    arq2_app.write(user_input + '\n')
                    lista_arq.append(user_input)
        print('#' * 38)
        print('As palavras foram gravadas no arquivo!'.upper())
        print('#' * 38)


def clean_file():
    with open('palavras.txt', 'w') as arqs:
        arqs.write('')
    print('#' * 12)
    print('File erased!'.upper())
    print('#' * 12)


def game():
    words = load_file()
    chosen = random.choice(words)
    escolhida = str(chosen[0])
    splited_word = []
    for i in range(len(escolhida)):
        splited_word.append(escolhida[i].upper())

    print('-=' * 20)
    print('A palavra escolhida tem', len(splited_word), 'letras.')
    print('-=' * 20)

    lista1 = ['|_|'] * len(splited_word)
    print(*lista1)

    for i in range(8):
        if lista1 == splited_word:
            print('-=' * 20)
            print('Você acertou, a palavra era:', escolhida.upper())
            time.sleep(3)
            break
        user_input = input('Insira uma letra para verificar se a palavra contém alguma: ').upper()
        for x in range(len(splited_word)):
            if splited_word[x] == user_input:
                lista1[x] = user_input.upper()
        if user_input not in splited_word:
            print('-=' * 20)
            print('Você tem mais', 8 - i - 1, 'tentativas!')
            print('-=' * 20)
            time.sleep(1)
        print(*lista1)
        if i == 7:
            print('-=' * 20)
            print('Você perdeu! A palavra era:', escolhida.upper())
            time.sleep(3)


main()
