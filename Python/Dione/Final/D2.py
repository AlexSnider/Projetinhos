# Escreva a função “repetido” que recebe uma String por parâmetro e retorna false caso a String não possua caracteres repetidos (que aparece mais de uma vez, independente da posição) ou true caso algum caracter esteja repetido.
# Monte também um trecho de código para testar a função.

def main():
    string = inserir()
    if repetido(string):
        print('Existe caractere repetido em:', inserir())
    else:
        print('Não existe caractere repetido em:', inserir())


def inserir():
    return input('Isira um texto qualquer: ')


def repetido(inserir):
    for x in inserir:
        if inserir.count(x) > 1:
            return True
    return False


main()
