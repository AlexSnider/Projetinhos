# Escreva a função “repetido” que recebe uma String por parâmetro e retorna false caso a String não possua caracteres repetidos (que aparece mais de uma vez, independente da posição) ou true caso algum caracter esteja repetido.
# Monte também um trecho de código para testar a função.

def main():
    user_input = input('Insira um texto qualquer: ')
    if repetido(user_input):
        print('Existe caractere repetido em:', user_input)
    else:
        print('Não existe caractere repetido em:', user_input)


def repetido(user_input):
    for k in user_input:
        if user_input.count(k) > 1:
            return True
    else:
        return False


main()
