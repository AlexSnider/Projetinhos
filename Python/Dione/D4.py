# Faça um programa que, a partir de um texto digitado pelo usuário, conte o número de caracteres total e o número de palavras (palavra é definida por qualquer sequência de caracteres delimitada por espaços em branco, virgula ou ponto) e exiba o resultado.

def main():
    user_input = input('Digite um texto qualquer: ')
    count_caract(user_input)
    count_words(user_input)


def count_caract(user_input):
    count = 0
    contador = len(user_input)
    count += contador
    print('O número de total de caracteres é de:', count)


def count_words(user_input):
    count2 = 0
    contador2 = len(user_input.split())

    if contador2 != ',' and '.':
        count2 += contador2

    print('O número de total de palavras é de:', count2)


main()