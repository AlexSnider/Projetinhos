def main():
    # user_input = int(input('Digite o número correspondente as ações dispostas a eles: '))
    inserir_palavras()
    carregar_arq()


def menu():
    ins_palavras = '1'
    carr_arq = '2'
    apagar = '3'
    iniciar_game = '4'
    encerrar = '5'


def inserir_palavras():
    print('Digite "0" e aperte ENTER para encerrar ou apenas dê um ENTER para continuar: ')
    user_input = str(input('Insira palavras para serem usadas no game da forca: '))

    palavras_arq = open('palavras.txt', 'w', encoding='utf-8')

    while user_input != '0':
        palavras_arq.write(user_input)
        palavras_arq.write('\n')
        user_input = str(input('Insira palavras para serem usadas no game da forca: '))


def carregar_arq():
    arq = open('palavras.txt', 'r', encoding='utf-8')
    arq.read()
    arq.seek(0, 0)
    l_arq = arq.readlines()

    for i in l_arq:
        if len(i) < 10:
            print('Você não digitou 10 palavras ainda. Continue até atingir 10!')
            user_input = str(input('Insira palavras para serem usadas no game da forca: '))
            l2_arq = open('palavras.txt', 'a', encoding='utf-8')
            l2_arq.write(user_input)
            l2_arq.write('\n')
            print(

                arq=open('palavras.txt', 'r', encoding='utf-8')
            arq.read()
            arq.seek(0, 0)
            l2_arq = arq.readlines()

            l_palavras = []

            for x in range(len(l2_arq)):
                l_palavras.append(l2_arq[x].split())
            print(l_palavras)

main()
