# Implemente um programa em Python que tenha uma função que receba como parâmetro uma String contendo o nome de uma pessoa e retorna outra String contendo as iniciais do nome.


def main():
    user_input = input('Insira seu nome: ')
    user_input2 = user_input.split()
    j = ['de', 'di', 'do', 'e', 'dos', 'das', 'du']
    compara(user_input2, j)

def compara(user_input2, j):
    x = ''
    for i in range(len(user_input2)):
        if user_input2[i] not in j:
            x += (user_input2[i][0].upper())
    print('Seu nome é:', *user_input2, 'e suas iniciais são:', x)


main()
