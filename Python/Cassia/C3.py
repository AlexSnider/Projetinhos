# jose 10 5 2 3 4
# pedro 3 6 9 2
# suzana 8 2 7 4 3 7 4 1 2 9 1 7
# gisela 2 8 2 5 6 7
# joao 4 3 5 7 6

# módulo que imprime o nome dos estudantes que têm mais de cinco notas;
# módulo que calcula a média das notas de cada estudante e imprime o nome e a média de cada um;
# módulo que calcula a nota maior de cada estudante e imprima o nome junto com a sua maior nota.

meuArq = open('aquivo.txt', 'w+', encoding='utf-8')
meuArq.write('jose 10 5 2 3 4')
meuArq.write('pedro 3 6 9 2')
meuArq.write('suzana 8 2 7 4 3 7 4 1 2 9 1 7')
meuArq.write('gisela 2 8 2 5 6 7')
meuArq.write('joao 4 3 5 7 6')
meuArq.close()


