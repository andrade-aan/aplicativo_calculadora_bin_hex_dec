
def bin_dec(x):  # funcao de conversao binario para decimal
    a = len(x)  # recebe o valor do tamanho da string usado no for_range
    res_1 = []  # cria lista vazia para receber itens processados
    res_2 = 0  # criacao da variavel res_2 para receber os valores convertidos
    i = 0  # variavel funciona como range 2 dentro do for_range
    for a in range(a - 1, -1, -1):  # ordem decrescente
        dec_transito = int(x[i]) * (2 ** a)
        res_1.append(dec_transito)
        i = i + 1

    i = 0  # redefinicao da variavel
    a = len(x)  # redefinicao da variavel

    for a in range(a - 1, -1, -1):
        res_2 = res_2 + int(res_1[i])
        i = i + 1
    res_2 = int(res_2)
    return res_2


def dec_hex(x):
    a = len(x)
    r = int(x)
    i = 1  # atribuicao de valor para a variavel de controle do loop while
    resp = []
    list_dec = []

    # dicionário de base para conversao
    hexa  = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5",
             6: "6", 7: "7", 8: "8", 9: "9", 10: "A", 11: "B",
             12: "C", 13: "D", 14: "E", 15: "F"}

    lista_a = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15) # lista para conversao

    while i != 0:
        list_dec.append((r % 16))  # lista criada com o resto da divisao
        r = r // 16  # variavel recebe os valores inteiros apos a divisao por 16 (base hexadecimal)
        i = int(r)  # quando a divisao tende a zero inteiro, o loop encerra
    b = len(list_dec)
    i = 0
    f = 0

    for f in range(b - 1, -1, -1):
        for i in range(15, -1, -1):
            if lista_a[i] == list_dec[f]:
                resp.append(hexa[i])

    c = len(resp)
    resp_c = []
    concatenar = resp[0]
    for c in range(1, c):
        concatenar = concatenar + resp[c]

    return concatenar


def hex_dec(x):  # funcao de conversao numero hexadecimal para decimal
    a = len(x)  # variavel recebe o valor do tamanho da string
    res = []  # lista vazia para receber o processo de conversao

    # dicionários
    hexa = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5",
            6: "6", 7: "7", 8: "8", 9: "9", 10: "A", 11: "B",
            12: "C", 13: "D", 14: "E", 15: "F"}

    hexa2 = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
             '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11,
             'C': 12, 'D': 13, 'E': 14, 'F': 15}

    for f in range(0, a):
        for i in range(0, 16):
            if hexa[i] == x[f]:
                res.append(x[f])
    b = len(x)
    res2 = 0
    i = 0
    for b in range(b - 1, -1, -1):
        res2 = res2 + hexa2[res[i]] * (16 ** (b))
        i = i + 1

    return res2
    # pass


def dec_bin(x):  # fucao para converter decimal para binario

    r = int(x)  # recebe a string digitada como inteiro
    a = len(x)  # recebe o valor de itens digitados pelo usuario
    res_1 = []  # lista vazia para receber os restos da divisao por 2
    i = 1  # variavel de controle de loop

    while i != 0:
        res_1.append((r % 2))  # lista recebe os valores do resto da divisao
        r = r // 2  # variavel acumula de forma decrescente o valor inteiro da divisao
        i = int(r)  # controle de saida do loop, quando a divisao tende a zero inteiro

    res_2 = list(reversed(res_1))  # lista res_2 recebe a ordem invertida da lista res_1

    concatenar = str(res_2[0])  # variavel recebe primeiro item da lista res_2

    b = len(res_2)  # variavel recebe o tamanho de itens da lista para o range

    for a in range(1, b):
        concatenar = concatenar + str(res_2[a])  # juncao dos itens da lista res_2 cono string

    resposta = int(concatenar)  # transformacao da variavel string para numero inteiro

    return resposta


def bin_hex(x):  # funcao conversao de binario para hexadecimal

    a = bin_dec(x)
    a = str(a)
    res_01 = dec_hex(a)
    return res_01


def hex_bin(x):
    a = hex_dec(x)
    a = str(a)
    res_01 = dec_bin(a)
    return res_01


escolha = 0
# criando o menu
while escolha != '99':

    print('Conversor de Bases\n' +
          '1 - Binario para Decimal\n' +
          '2 - Decimal para Binário\n' +
          '3 - Hexadecimal para Decimal\n' +
          '4 - Decimal para Hexadecimal\n' +
          '5 - Binario para Hexadecimal\n' +
          '6 - Hexadecimal para Binário\n' +
          '99 - Sair do Programa\n')

    escolha = str(input('Digite a opção desejada:\n' +
                        '>>> '))

    if escolha == '1':
        numero = str(input('Digite o número para conversão:' +
                           '>>> '))
        numero_formatado = numero.upper()
        resposta = bin_dec(numero_formatado)
        print(resposta)

    elif escolha == '2':
        numero = str(input('Digite o número para conversão:' +
                           '>>> '))
        numero_formatado = numero.upper()
        resposta = dec_bin(numero_formatado)
        print(resposta)

    elif escolha == '3':
        numero = str(input('Digite o número para conversão:' +
                           '>>> '))
        numero_formatado = numero.upper()
        resposta = hex_dec(numero_formatado)
        print(resposta)

    elif escolha == '4':
        numero = str(input('Digite o número para conversão:' +
                           '>>> '))
        numero_formatado = numero.upper()
        resposta = dec_hex(numero_formatado)
        print(resposta)

    elif escolha == '5':
        numero = str(input('Digite o número para conversão:' +
                           '>>> '))
        numero_formatado = numero.upper()
        resposta = bin_hex(numero_formatado)
        print(resposta)

    elif escolha == '6':
        numero = str(input('Digite o número para conversão:' +
                           '>>> '))
        numero_formatado = numero.upper()
        resposta = hex_bin(numero_formatado)
        print(resposta)
