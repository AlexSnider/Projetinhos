# módulo que imprime o nome dos estudantes que têm mais de cinco notas;
# módulo que calcula a média das notas de cada estudante e imprime o nome e a média de cada um;
# módulo que calcula a nota maior de cada estudante e imprima o nome junto com a sua maior nota.

# meuArq = open('aquivo.txt', 'w', encoding='utf-8')
# meuArq.write('jose 10 5 2 3 4\n')
# meuArq.write('pedro 3 6 9 2\n')
# meuArq.write('suzana 8 2 7 4 3 7 4 1 2 9 1 7\n')
# meuArq.write('gisela 2 8 2 5 6 7\n')
# meuArq.write('joao 4 3 5 7 6')
# meuArq.close()

def main():
    try:
        meuarq = open('aquivo.txt', 'r', encoding='utf-8')
        dadosArq1 = meuarq.read()
        meuarq.seek(0, 0)

        listaArquivo = meuarq.readlines()
        p1 = listaArquivo[0].split()
        p2 = listaArquivo[1].split()
        p3 = listaArquivo[2].split()
        p4 = listaArquivo[3].split()
        p5 = listaArquivo[4].split()

        p1_nome = p1[0]
        p2_nome = p2[0]
        p3_nome = p3[0]
        p4_nome = p4[0]
        p5_nome = p5[0]

        p1_nota = p1[1:]
        p2_nota = p2[1:]
        p3_nota = p3[1:]
        p4_nota = p4[1:]
        p5_nota = p5[1:]

        imprime_mais_notas(p1_nome, p1_nota, p2_nome, p2_nota, p3_nome, p3_nota, p4_nome, p4_nota, p5_nome, p5_nota)
        media(p1_nome, p1_nota, p2_nome, p2_nota, p3_nome, p3_nota, p4_nome, p4_nota, p5_nome, p5_nota)
        maior_nota(p1_nome, p1_nota, p2_nome, p2_nota, p3_nome, p3_nota, p4_nome, p4_nota, p5_nome, p5_nota)
    except FileNotFoundError:
        print('Arquivo não encontrado! Por favor, observe o nome digitado.')


def imprime_mais_notas(p1_nome, p1_nota, p2_nome, p2_nota, p3_nome, p3_nota, p4_nome, p4_nota, p5_nome, p5_nota):
    print('Apenas esses alunos possuem mais de cinco notas:')
    if len(p1_nota) > 5:
        print(p1_nome)
    if len(p2_nota) > 5:
        print(p2_nome)
    if len(p3_nota) > 5:
        print(p3_nome)
    if len(p4_nota) > 5:
        print(p4_nome)
    if len(p5_nota) > 5:
        print(p5_nome)
    else:
        print('Os demais não possuem mais de cinco notas.')
        print('-=' * 30)


def media(p1_nome, p1_nota, p2_nome, p2_nota, p3_nome, p3_nota, p4_nome, p4_nota, p5_nome, p5_nota):
    n1 = []
    n2 = []
    n3 = []
    n4 = []
    n5 = []

    s1m = 0
    s2m = 0
    s3m = 0
    s4m = 0
    s5m = 0

    for i in p1_nota:
        n1.append(int(i))
    for x in n1:
        x += x - x
        s1m += x / len(p1_nota)
    print('Média dos alunos.')
    print(p1_nome, ':', 'obteve média de:', s1m)

    for i in p2_nota:
        n2.append(int(i))
    for x in n2:
        x += x - x
        s2m += x / len(p2_nota)
    print(p2_nome, ':', 'obteve média de:', s2m)

    for i in p3_nota:
        n3.append(int(i))
    for x in n3:
        x += x - x
        s3m += x / len(p3_nota)
    print(p3_nome, ':', 'obteve média de:', s3m)

    for i in p4_nota:
        n4.append(int(i))
    for x in n4:
        x += x - x
        s4m += x / len(p4_nota)
    print(p4_nome, ':', 'obteve média de:', s4m)

    for i in p5_nota:
        n5.append(int(i))
    for x in n5:
        x += x - x
        s5m += x / len(p5_nota)
    print(p5_nome, ':', 'obteve média de:', s5m)
    print('-=' * 30)


def maior_nota(p1_nome, p1_nota, p2_nome, p2_nota, p3_nome, p3_nota, p4_nome, p4_nota, p5_nome, p5_nota):
    n1 = []
    n2 = []
    n3 = []
    n4 = []
    n5 = []

    for i in p1_nota:
        n1.append(int(i))
    for i in p2_nota:
        n2.append(int(i))
    for i in p3_nota:
        n3.append(int(i))
    for i in p4_nota:
        n4.append(int(i))
    for i in p5_nota:
        n5.append(int(i))
    print('Maior nota por aluno.')
    print('A maior nota de', p1_nome, 'é:', max(n1))
    print('A maior nota de', p2_nome, 'é:', max(n2))
    print('A maior nota de', p3_nome, 'é:', max(n3))
    print('A maior nota de', p4_nome, 'é:', max(n4))
    print('A maior nota de', p5_nome, 'é:', max(n5))


main()
