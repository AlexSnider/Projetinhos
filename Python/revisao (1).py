def estruturas():
    inteiro = 10  # int
    print("\n", inteiro, type(inteiro))

    decimal = 10.52  # float
    print("\n", decimal, type(decimal))

    lista = [6, 12, 'palavras']  # lista (mutável)
    print("\n", lista, type(lista))

    tupla = (1, 2, 3, True, 'unoeste')  # tupla (imutável)
    print("\n", tupla, type(tupla))

    dicionario = {'nome': 'Unoeste', 'ano': 2022}  # cada valor possui uma chave associada
    print("\n dicionário[ano]: ", dicionario['ano'])

    # pilhas: o último elemento adicionado é o primeiro a ser retirado
    lista.append(100)
    lista.append('aula')
    lista.append('algoritmos')
    lista.append(2022)
    lista.append('unoeste')
    print("\n", lista)
    lista.pop()
    print("\n lista.pop() > A pilha retira o último elemento. \n Nova lista: ", lista)

    # filas: o primeiro elemento adicionado é o primeiro a ser retirado
    import queue
    fila = queue.Queue()
    fila.put(100)
    fila.put('aula')
    fila.put('algoritmos')
    fila.put(2022)
    fila.put('unoeste')
    print("\n Fila: ", list(fila.queue))
    fila.get()
    print("\n o comando .get() retira o primeiro elemento. \n Nova fila", list(fila.queue))

    # matriz
    matriz = [ # 0, 1, 2 >> colunas
                [1, 2, 3], #0 >> linhas
                [4, 5, 6], #1
                [7, 8, 9], #2
                [10, 11, 12] #3
            ]
            # [[1,2,3], [1,5,10], [5,6,6]]
            # [['unoeste algoritmos'], ['10 50 2 2022'], [10, 50, 2022]]

    print("\n", "matriz: ")
    for linha in matriz:
        for elemento in linha:
            print(elemento)

    print("\n", "matriz: ")
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j])

    # conversões
    num = int('10')
    print("\n", num, type(num))

    string = str(num)
    print("\n", string, type(string))

    dec = float(string)
    print("\n", dec, type(dec))


def strings():
    frase = "estudar algoritmos é muito legal"
    print("\n", ".split()", frase.split())  # divide a frase conforme o parâmetro informado, o padrão é 'espaço'
    print("\n", ".replace()", frase.replace(' ', '*'))  # substitui o primeiro caractere informado pelo segundo
    print("\n", ".count()", frase.count('m'))  # conta quantas vezes o caractere passado como parâmetro aparece na string
    print("\n", "[ : : -1]", frase[::-1])  # string[ comeco : fim : passo] o comando [ : : -1] exibe a string de trás para frente
    print("\n", "[ : : 2]", frase[::2])  # exibe a string a cada dois caracteres


def funcoes(parametros):
    print("\n", "Função executada:", parametros)
    return True


def arquivos():
    arq = open('novo-arquivo-revisao.txt', 'w+')  # w = write
    texto = "unoeste algoritmos e \nestruturas de dados \nprofessora cassia"
    arq.write(texto)
    arq.close()
    # arq.seek(0, 0) >> retorna o cursor de leitura para a posição inicial

    arq = open('novo-arquivo-revisao.txt', 'r')   # r = read, a = append "permite a adição de conteúdo"
    # string = arq.read()  # lê o conteúdo do arquivo como uma string única
    lista_de_linhas = arq.readlines()  # lê o conteúdo do arquivo colocando cada linha numa posição da lista

    for i in range(len(lista_de_linhas)):
        lista_de_palavras = lista_de_linhas[i].split()  # lista_de_linhas[i] retorna uma string, a qual é dividida em palavras com o método split()
        print("\nlista de palavras", lista_de_palavras)

        for palavra in lista_de_palavras:  # exibe cada palavra da lista de palavras
            print("palavra:", palavra)

    arq.close()


def principal():
    estruturas()
    strings()

    p = 'parametros'
    resultado = funcoes(p)
    print("\n", "resultado", resultado)

    arquivos()


principal()
