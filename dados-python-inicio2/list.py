import pandas as pd

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

def diabates(lista):
    #Uma clínica analisa dados de pacientes e armazena o valor numérico da glicose em um banco de dados e gostaria de rotular os dados da seguinte maneira:
    # Glicose igual ou inferior a 70: 'Hipoglicemia'

    # Glicose entre 70 a 99: 'Normal'
    # Glicose entre 100 e 125: 'Alterada'
    # Glicose superior a 125: 'Diabetes'

    #A clínica disponibilizou parte dos valores e sua tarefa é criar uma lista de tuplas usando list comprehension contendo o rótulo e o valor da glicemia em cada tupla

    return [(
        f"Rotulo: {i}", 
        f"{valor} - Hipoglicemica" if valor <= 70
        else f"{valor} - Normal" if valor <= 99
        else f"{valor} - Alterada" if valor <= 125
        else f"{valor} - Diabetes"
    ) 
    for i, valor in enumerate(lista)]

    glicemia = [129, 82, 60, 97, 101, 65, 62, 167, 87, 53, 58, 92, 66, 120, 109, 62, 86, 96, 103, 88, 155, 52, 89, 73]
    status = diabates(glicemia)
    df = pd.DataFrame(status, columns=["rotulo", "classificação"])
    print(df)

def loja(list1, list2, list3):
    #Um e-commerce possui as informações de id de venda, quantidade vendida e preço do produto divididos nas seguintes listas 

    # # O e-commerce precisa estruturar esses dados em uma tabela contendo o valor total da venda, que é obtida multiplicando a quantidade pelo preço unitário. Além disso, a tabela precisa conter um cabeçalho indicando as colunas: 'id', 'quantidade', 'preco' e 'total'. 
    
    # # Crie uma lista de tuplas em que cada tupla tenha id, quantidade, preço e valor total, na qual a primeira tupla é o cabeçalho da tabela

    return [('id', 'quantidade', 'preco', 'total')] + [
        (i, q, p, q*p) for i, q, p in zip(list1, list2, list3)
    ]


    ids = [0,1,2,3,4,5,6,7,8,9]
    quantidade = [15,12,1,15,2,11,2,12,2,4]
    preco = [93.0,102.0,18.0,41.0,122.0,14.0,71.0,48.0,14.0,144.0]

    df = pd.DataFrame({
        "id": ids,
        "quantidade": quantidade,
        "preco": preco
    })

    df["total"] = df["quantidade"] * df["preco"]

    print(df)


def relatorio(list1, list2, list3):
    # EXERCÍCIO EXTRA - RELATÓRIO DE LOJA

    # A loja quer descobrir qual produto gerou mais faturamento.

    # Usando as mesmas listas:

    # produtos
    # quantidades
    # precos

    # Crie uma função que retorne:

    # 1️⃣ O produto com maior faturamento
    # 2️⃣ O valor desse faturamento
    # 3️⃣ O faturamento total da loja

    # Exemplo esperado:

    # Produto com maior faturamento: Notebook
    # Faturamento: 17500
    # Faturamento total da loja: XXXXX
    return [
        ('produto', 'quantidade', 'preco', 'faturamento', 'status') + (
        (produto, qtd, preco, qtd * preco, "Baixa venda" if qtd * preco < 1000 else "Média Venda" if qtd * preco < 5000 else "Alta venda")
    )
    for produto, qtd, preco in zip(list1, list2, list3)
    ]

    produtos = ["Notebook", "Mouse", "Teclado", "Monitor", "Headset"]
    quantidades = [5, 10, 7, 3, 8]
    precos = [3500.0, 80.0, 150.0, 900.0, 200.0]

    #df = pd.DataFrame({
        #"produto" : produtos,
        #"quantidade": quantidades,
        #"Preços": precos
        #})

        #df["Faturamento"] = df["quantidade"] * df["Preços"]
        #df["Status"] = df["Faturamento"].apply(lambda x: "Baixa venda" if x < 1000 else ("Média Venda" if x < 5000 else "Alta venda"))

        #print(df)


def filiais(estados):

    # Uma empresa possui filiais espalhadas nos Estados da região Sudeste do Brasil. Em uma das tabelas de cadastro das filiais há uma coluna contendo a informação de qual é o Estado a que pertence:

    # A empresa sempre está abrindo novas filiais, de modo que a tabela está constantemente recebendo novos registros e o gestor gostaria de possuir a informação atualizada da quantidade de filiais em cada Estado.

    #A partir da coluna com a informação dos Estados, crie um dicionário usando dict comprehension com a chave sendo o nome de um Estado e o valor sendo a contagem de vezes em que o Estado aparece na lista.

    return {estado: estados.count(estado) for estado in set(estados)}

    estados = ['SP', 'ES', 'MG', 'MG', 'SP', 'MG', 'ES', 'ES', 'ES', 'SP', 'SP', 'MG', 'ES', 'SP', 'RJ', 'MG', 'RJ', 'SP', 'MG', 'SP', 'ES', 'SP', 'MG']

    contadorsp, contadorrj, contadores, contadormg = filiais(estados)

    ok = filiais(estados)
    print(ok)


def contar_categorias(lista):
    #Uma empresa de e-commerce quer analisar quais categorias de produtos aparecem mais nos pedidos.
    return {item: lista.count(item) for item in set(lista)}

    categorias = [
        'eletronicos', 'roupas', 'eletronicos', 'livros',
        'livros', 'roupas', 'eletronicos', 'moveis',
        'livros', 'eletronicos', 'moveis', 'roupas'
    ]

    ok = contar_categorias(categorias)
    mais_vendido = max(ok, key=ok.get)

    print(ok)
    print(f'O mais vendido foi: {mais_vendido}')


def contar_produtos(lista):
    #Crie uma função contar_produtos
    #Use dict comprehension, Crie um dicionário
    return {produto: lista.count(produto) for produto in set(lista)}

    produtos = [
    'notebook', 'mouse', 'teclado', 'mouse',
    'monitor', 'mouse', 'notebook', 'teclado',
    'mouse', 'monitor', 'notebook'
    ]

    produto, quantidade = max(contar_produtos(produtos).items(), key=lambda x: x[1])

    print(contar_produtos(produtos))
    print(f"O produto mais vendido foi: {produto} com {quantidade} vendas.")

def analise_notas(lista):
    return {
        "media": sum(lista) / len(lista),
        "maior": max(lista),
        "menor": min(lista)
    }

    notas = [7, 8, 5, 9, 7, 8, 6, 10, 5, 7]
    resultado = analise_notas(notas)

    print(resultado)

    def contar_palavras(frase):
        palavras = frase.split()
        return {p: palavras.count(p) for p in set(palavras)}
        
    frase = "produto bom qualidade boa produto chegou rapido produto bom"
    ok = contar_palavras(frase)
    print(ok)


def faturamento(vendas):

    resultado = {}

    for produto, valor in vendas:
        if produto in resultado:
            resultado[produto] += valor
        else:
            resultado[produto] = valor

    return resultado

    vendas = [
    ('Notebook', 3500),
    ('Mouse', 80),
    ('Teclado', 200),
    ('Mouse', 80),
    ('Notebook', 3500),
    ('Mouse', 80)
    ]

    print(faturamento(vendas))

def faturamento_total(lista):
    soma = 0
    for v in vendas[2]:
        soma += v
    return soma


    vendas = [
        {"produto": "Notebook", "categoria": "Eletronicos", "valor": 3500},
        {"produto": "Mouse", "categoria": "Eletronicos", "valor": 80},
        {"produto": "Cadeira", "categoria": "Moveis", "valor": 900},
        {"produto": "Teclado", "categoria": "Eletronicos", "valor": 200},
        {"produto": "Mesa", "categoria": "Moveis", "valor": 1200},
        {"produto": "Mouse", "categoria": "Eletronicos", "valor": 80},
        {"produto": "Notebook", "categoria": "Eletronicos", "valor": 3500}
    ]

    ok = sum(item["valor"] for item in vendas)
    print(ok)

def saudacao(nome):
    print(f'Olá, {nome} seja bem vindo ao meu programa!')


def dobro(numb):
    return numb * 2


def p_or_i(numb):
    return 'par' if numb % 2 == 0 else 'impar'


def numeros():
    for n in range(1, 11):
        print(f'numero: {n}')


def maior_menor():
    try:
        numb1 = int(input("Digite o primeiro numero: "))
        numb2 = int(input("Digite o segundo numero: "))

        result = numb1 if numb1 > numb2 else numb2
        print(f'{result} é maior.')
    except ValueError:
        print("Por favor, digite somente numeros inteiros!")


nome = input("Digite o seu nome: ")
saudacao(nome)


try:
    numero = int(input(f'{nome}, digite um numero: '))
    print(f'Numero: {numero}')

    resp = dobro(numero)
    print(f'Dobro: {resp}')

    resultado = p_or_i(numero)
    print(f'O numero é: {resultado}')

    def idade(numb):
        return 'maior' if numb >= 18 else 'menor'

    anos = int(input("Digite quantos anos você tem: "))

    result = idade(anos)
    print(f'Você é {result} de idade.')
except ValueError:
    print('Por favor, digite numeros inteiros!')


maior_menor()
numeros()

