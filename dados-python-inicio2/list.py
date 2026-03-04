def soma(lista):
    #Crie um código para imprimir a soma dos elementos de cada uma das listas contidas na seguinte lista:
    return [sum(n) for n in lista]


    lista_de_listas = [[4,6,5,9], [1,0,7,2], [3,4,1,8]]
    soma_elementos = soma(lista_de_listas)
    print(soma_elementos)

def terceiro_elemento(lista):
    # Crie um código para gerar uma lista que armazena o terceiro elemento de cada tupla contida na seguinte lista de tuplas:
    return  ["Peso ok" if n[-1] <= 80 else "Acima do peso" for n in lista]


    lista_de_tuplas = [('Pedro', 1.74, 81), ('Júlia', 1.65, 67), ('Otávio', 1.81, 83)]
    elemento3 = terceiro_elemento(lista_de_tuplas)
    print([i[0] for i in lista_de_tuplas], "\n", elemento3)

def nome_organizacao(lista):
    #A partir da lista, crie um código para gerar uma lista de tuplas em que cada tupla tenha o primeiro elemento como a posição do nome na lista original e o segundo elemento sendo o próprio nome

    # O enumerate entrega o índice (i) e o valor (v) de cada item
    return [(i+1, v) for i, v in enumerate(lista)]

    lista = ['Pedro', 'Júlia', 'Otávio', 'Eduardo']
    nome = nome_organizacao(lista)
    print(nome)

def valor_ap(lista):
    #Crie uma lista usando o list comprehension que armazena somente o valor numérico de cada tupla caso o primeiro elemento seja 'Apartamento', a partir da seguinte lista de tuplas
    return [n[1] for n in lista if n[0] == 'Apartamento']

    aluguel = [('Apartamento', 1700), ('Apartamento', 1400), ('Casa', 2150), ('Apartamento', 1900), ('Casa', 1100)]

    preco_aluguel = valor_ap(aluguel)
    print(preco_aluguel)


def data(mes, valor):
    # Crie um dicionário usando o dict compression com os meses e as despesas de cada mes
    return {mes: v for mes, v in zip(mes, valor)}

    meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
    despesa = [860, 490, 1010, 780, 900, 630, 590, 770, 620, 560, 840, 360]
    dicionario = data(meses, despesa)
    print(dicionario)


def jogos(lista1, lista2):
    #Se os pontos forem maiores ou iguais a 1000, o status é "Elite".
    #Se forem menores, o status é "Bronze"
    return {n: f"{p} - Elite" if p >= 1000 else f"{p} - Bronze" for n, p in zip(lista1, lista2)}

    jogadores = ['CyberPunk', 'NoobMaster69', 'GamerGirl', 'Troll_Face', 'Pro_Killer']
    pontos = [1200, 850, 1500, 400, 1100]
    hall_da_fama = jogos(jogadores, pontos)
    print(hall_da_fama)

def ex7(lista):
    # Filtra: Ano tem que ser 2022 E a venda (n[1]) tem que ser > 6000
    return [n for n in lista if n[0] == '2022' and n[1] > 6000]

    vendas = [('2023', 4093), ('2021', 4320), ('2021', 5959), ('2022', 8883), ('2023', 9859), ('2022', 5141), ('2022', 7688), ('2022', 9544), ('2023', 4794), ('2021', 7178), ('2022', 3030), ('2021', 7471), ('2022', 4226), ('2022', 8190), ('2021', 9680), ('2022', 5616)]
    op = ex7(vendas)
    print(op) 