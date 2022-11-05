# Desenvolva um jogo em que o jogador tenha que adivinhar uma palavra que será mostrada na tela com as letras embaralhadas.
# No programa deverá possuir funções para:
# - preencher uma lista de palavras (contendo no mínimo 10 palavras!)
# - escolher uma das palavras da lista aleatoriamente (função recebe uma lista e retorna o índice da palavra selecionada na lista para o jogador adivinhar);
# - embaralhar uma palavra passada por parâmetro – o critério de embaralhar deve ser criado pelo desenvolvedor (a função recebe a palavra que foi escolhida com a grafia correta e retorna a palavra embaralhada);
# - jogar, onde o jogador terá seis tentativas para adivinhar a palavra (recebe a palavra escolhida com a grafia correta por parâmetro e retorna o resultado true (se o jogador venceu) ou false (se o jogador perdeu)).
#
# Quando iniciar o jogo, o programa escolherá uma das palavras da lista (aletoriamente) e a exibirá embaralhada ao jogador. O jogador terá seis tentativas para adivinhar a palavra. Ao final, a palavra com a grafia correta deve ser mostrada na tela, informando se o jogador ganhou ou perdeu o jogo.



list_words = ['Venezuela', 'Protesto', 'Guerra', 'Brasil', 'Livre', 'Maracutaia', 'Corrupção',
                'Insegurança', 'Inflação', 'CiroGomes']




import random

def main():
    words = palavras()
    word = escolhe_palavra(words)
    print(escolhe_palavra(word))

def palavras():
    list = ['']
    list_words = ['Venezuela', 'Protesto', 'Guerra', 'Brasil', 'Livre', 'Maracutaia', 'Corrupção',
                'Insegurança', 'Inflação', 'CiroGomes']


def escolhe_palavra(words):
    x = ['']
    chosen = random.choice(words)
    x.append(chosen)
    return x

def embaralha(word):
    woords = word
    n = max([len(w) for w in woords])
    newWords = ['']*n
    for i in range(n):
        for j in woords:
            if i < len(j):
                newWords[i] += j[i]
    result = ' '.join(newWords)
    print(result)


main()

