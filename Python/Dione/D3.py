# Implemente um programa em Python que tenha uma função que receba como parâmetro uma String contendo o nome de uma pessoa e retorna outra String contendo as iniciais do nome.


def main():
    user_input = input('Insira seu nome: ')
    converte_string(user_input)


def converte_string(user_input):
    x = user_input.upper().split()
    for i in x:
        print('As iniciais do seu nome são:', i[0].replace('D', ''))


main()