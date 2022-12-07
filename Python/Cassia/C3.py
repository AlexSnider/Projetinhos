# módulo que imprime o nome dos estudantes que têm mais de cinco notas;
# módulo que calcula a média das notas de cada estudante e imprime o nome e a média de cada um;
# módulo que calcula a nota maior de cada estudante e imprima o nome junto com a sua maior nota.

meuArq = open('aquivo.txt', 'w', encoding='utf-8')
meuArq.write('jose 10 5 2 3 4 5 9 10 7\n')
meuArq.write('pedro 3 6 9 2 6 9 3 4\n')
meuArq.write('suzana 8 2 7\n')
meuArq.write('gisela 2 8 2 5 6 7\n')
meuArq.write('joao 4 3 5 7 6 9 5\n')
meuArq.write('gabriel 2 3 4 5 6 7 0')


def main():
    try:
        meuarq = open('aquivo.txt', 'r', encoding='utf-8')
        meuarq.read()
        meuarq.seek(0, 0)
        listaArquivo = meuarq.readlines()
        meuarq.close()

        list_nomes = []
        list_notas = []

        for x in range(len(listaArquivo)):
            list_nomes.append(listaArquivo[x].split()[0])

        for x in range(len(listaArquivo)):
            list_notas.append(listaArquivo[x].split()[1:])

        imprime_mais_notas(listaArquivo)
        media(list_notas, list_nomes)
        maior_nota(list_notas, list_nomes)
    except FileNotFoundError:
        print('Arquivo não encontrado! Por favor, observe o nome digitado.')


def imprime_mais_notas(listaArquivo):
    print('Apenas esses alunos possuem mais de cinco notas:')
    for i in range(len(listaArquivo)):
        linha = listaArquivo[i].split(' ')
        if len(linha) > 6:
            print(linha[0])
    else:
        print('Os demais não possuem mais de cinco notas.')
        print('-=' * 30)


def media(list_notas, list_nomes):
    print('Média dos alunos.')
    for i in range(len(list_notas)):
        linha = list_notas[i]
        soma = 0
        med = 0
        for x in range(len(linha)):
            soma += int(linha[x])
            med = soma / len(list_notas[i])
        print(list_nomes[i], 'obteve média de:', '%.2f' % med)
    print('-=' * 30)


def maior_nota(list_notas, list_nomes):
    print('Maiores notas por aluno.')
    for i in range(len(list_notas)):
        linha = list_notas[i]
        list_int = []
        for x in range(len(linha)):
            list_int.append(int(linha[x]))
        print('A maior nota de', list_nomes[i], 'é:', max(list_int))


meuArq.close()

main()
