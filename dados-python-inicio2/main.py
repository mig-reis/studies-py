import matplotlib.pyplot as plt   
from random import choice, randrange, sample
import numpy as np
import math
# Exercicios inicias


def treino1():
    # Conhecendo plt
    estudantes = ["João", "Maria", "José"]
    notas = [8.5, 9, 6.5]
    plt.bar(x = estudantes, height = notas)
    plt.show()


def treino2():
    # Conhecendo Random e funções dele
    estudantes = ["João", "Maria", "José", "Ana"]

    estudante = choice(estudantes)
    print(estudante)

    lista = []
    for i in range(10):
        lista.append(randrange(0, 20, 2))
    
    smp = sample(lista, 3)  
    print(smp)  


def treino3():
    # Treinando funções
    lista = [8, 12, 54, 23, 43, 1, 90, 87, 105, 77]
    print(f"Dada a lista: {lista}")
    numero = choice(lista)
    print(f"O numero sorteado foi: {numero}")


def treino4():
    # Crie um programa que sorteia, aleatoriamente, um número inteiro positivo menor que 100.
    print("Gerando numero positivo aleatorio de 1 a 100...")
    numero = randrange(100)
    print(f"Numero gerado! O numero é {numero}.")


def treino5():
    # Crie um programa que solicite à pessoa usuária digitar 
    # dois números inteiros e calcular a potência do 1º número elevado ao 2º    
    print("Por favor, digite dois numero a seguir para calcularmos a potência.")
    numero1 = int(input("Digite o primero numero: "))
    numero2 = int(input("Digite o segundo numero: "))
    result = (numero1 ** numero2)
    print(result)


def treino6():
    # Um programa deve ser escrito para sortear uma pessoa seguidora 
    # de uma rede social para ganhar um prêmio. A lista de participantes 
    # é numerada e devemos escolher aleatoriamente um número de acordo 
    # com a quantidade de participantes. Peça à pessoa usuária para fornecer 
    # o número de participantes do sorteio e devolva para ela o número sorteado.

    print("VAMOS REALIZAR UM SORTEIO!")

    try:
        quantidade = int(input("Digite a quantidade de participantes: "))
        lista = list(range(1, quantidade + 1))
        print(lista)

        sorteado = choice(lista)
        print(f"Número sorteado: {sorteado}")

    except ValueError:
        print("Digite apenas números!")


def treino7():
    # Você recebeu uma demanda para gerar números de token para acessar o 
    # aplicativo de uma empresa. O token precisa ser par e variar de 1000 até 
    # 9998. Escreva um código que solicita à pessoa usuária o seu nome e exibe 
    # uma mensagem junto a esse token gerado aleatoriamente.

    nome = input("Digite o seu nome: ")

    if not nome.isalpha():
        print("Por favor, digite um NOME!")
        return 

    token = randrange(1000, 9998, 2)

    print(f"Bem vindo(a) {nome}! Seu token para acesso é: {token}.")


def treino8():
    # Para diversificar e atrair novos(as) clientes, uma lanchonete 
    # criou um item misterioso em seu cardápio chamado "salada de 
    # frutas surpresa". Neste item, são escolhidas aleatoriamente 3 
    # frutas de uma lista de 12 para compor a salada de frutas da pessoa 
    # cliente. Crie o código que faça essa seleção aleatória de acordo com a lista abaixo:
    print("Vamos sortear as 3 frutas para compor sua salada de frutas!")

    frutas = ["maçã", "banana", "uva", "pêra", 
          "manga", "coco", "melancia", "mamão",
          "laranja", "abacaxi", "kiwi", "ameixa"]

    print(f"As opções são: {frutas}")

    result = sample(frutas, 3)
    print(f"As frutas sorteadas foram: {', '.join(result)}")


def treino8():
    # Você recebeu um desafio de calcular a raiz quadrada de uma lista de números,
    #  identificando quais resultaram em um número inteiro. A lista é a seguinte:
    numeros = [2, 8, 15, 23, 91, 112, 256]

    for numero in numeros:
        raiz = math.sqrt(numero)

        if raiz == int(raiz):
            print(f"A raiz quadrada de {numero} é inteira: {int(raiz)}")


def treino9():
    # Faça um programa para uma loja que vende grama para jardins. Essa loja 
    # trabalha com jardins circulares e o preço do metro quadrado da grama 
    # é de R$ 25,00. Peça à pessoa usuária o raio da área circular e devolva 
    # o valor em reais do quanto precisará pagar.
    try:

        raio = float(input("Digite o raio da aréa que você deseja adquirir a grama: "))

        area = math.pi * raio ** 2
        valor_final = area * 25

        print(f"O jardim de {area:.2f}m² custará R$ {valor_final:.2f}")

    except ValueError:
        print("Por favor, digite um NUMERO.")
    

def treino10():
    # Uma empresa constrói piscinas circulares.
    # O custo do revestimento é R$ 120 por m².
    # Peça o raio da piscina e mostre: área da piscina e custo total

    try:
        raio = float(input("Digite o raio total da area da piscina: "))

        area = math.pi * raio ** 2
        result = area * 120

        print(f"A piscina de {area:.2f}m² custara R$ {result:.2f}.")
    except ValueError:
        print("Por favor, digite apenas numeros!")
        return


def treino11():
    # Uma empresa de paisagismo precisa calcular o custo para preparar um terreno circular.
    # O terreno será coberto com grama ao custo de R$ 30,00 por metro quadrado e também
    # será cercado, sendo que o custo da cerca é de R$ 80,00 por metro de comprimento.
    # Faça um programa que solicite o raio do terreno circular, calcule a área do terreno,
    # o comprimento da cerca (circunferência) e determine o custo da grama, o custo da cerca
    # e o custo total do projeto. Os valores devem ser exibidos com duas casas decimais.
    try:
        raio = float(input("Informe o raio do terreno: "))

        area = math.pi * raio ** 2
        comprimento = 2 * math.pi * raio

        custo_grama = area * 30
        custo_cerca = comprimento * 80
        custo_total = custo_grama + custo_cerca

        print(f"\nCusto da grama: R$ {custo_grama:.2f}")
        print(f"Custo da cerca: R$ {custo_cerca:.2f}")
        print(f"Custo total: R$ {custo_total:.2f}")

    except ValueError:
        print("Por favor, digite apenas números!")


def treino12():
    # Escreva um código que lê a lista abaixo e faça: A leitura do tamanho da lista
    # A leitura do maior e menor valor e a soma dos valores da lista

    lista = [16, 14, 63, 65, 17, 99, 70, 11, 20, 48, 79, 32, 17, 89, 12, 25, 66]

    tam = len(lista)
    soma = sum(lista)
    maior = max(lista)
    menor = min(lista)

    print(f"A lista possui {tam} números em que o maior número é {maior} e o menor número é {menor}. A soma dos valores presentes nela é igual a {soma}")


def treino13():
    #Escreva uma função que gere a tabuada de um número inteiro de 1 a 10, de acordo com a escolha da pessoa usuária. Como exemplo, para o número 7, a tabuada deve ser mostrada no seguinte formato:

    try:
        escolha = int(input("Digite um numero de 1 a 10: "))

        while escolha < 1 or escolha > 10:
            print("Por favor, digite um numero de 1 a 10.")
            escolha = int(input("Digite um numero de 1 a 10: "))

        for n in range(1, 10 + 1):
            print(f"{escolha} X {n} = {(escolha * n)} ")
            

    except ValueError:
        print("Por favor, digite somente numeros inteiros.")


def treino14():
    # Crie a função que leia a lista abaixo e retorne uma nova lista com os múltiplos de 3:
    # Utilize o return na função e salve a nova lista na variável mult_3.
    lista = [97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]
    mult_3 = [x for x in lista if x % 3 == 0]

    print(mult_3)


def treino15():
    # Crie uma lista dos quadrados dos números da seguinte lista . Lembre-se de utilizar as funções lambda e map() para calcular o quadrado de cada elemento da lista.
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    lista_atualizada = list(map(lambda x: x**2, lista))
    print(lista_atualizada)


def treino16():
    
    # Você foi contratado(a) como cientista de dados de uma associação de skate. Para analisar as notas recebidas de skatistas em algumas competições ao longo do ano, você precisa criar um código que calcula a pontuação dos(as) atletas. Para isso, o seu código deve receber 5 notas digitadas pelas pessoas juradas.
    #Para calcular a pontuação de um(a) skatista, você precisa eliminar a maior  e a menor pontuação dentre as 5 notas e tirar a média das 3 notas que sobraram. Retorne a média para apresentar o texto:
    #"Nota da manobra: [media]"

    try:
        NotaJurados = []
        contador = 0

        while contador < 5:
            nota = int(input("Digite a nota: "))
            if 1 <= nota <= 10:
                NotaJurados.append(nota)
                contador += 1
            else:
                print("Digite uma nota de 1 a 10")
        
        NotaJurados.remove(max(NotaJurados))
        NotaJurados.remove(min(NotaJurados))
        media = (sum(NotaJurados) / len(NotaJurados))

        print(f"Nota da manobra: {media:.1f}")

    except ValueError:
        print("Por favor, digite uma nota VALIDA!")



def analisar_notas(notas):

    #"O(a) estudante obteve uma média de [media], com a sua maior nota de [maior] pontos e a menor nota de [menor] pontos e foi [situacao]"

    media = sum(notas) / len(notas)
    maior = max(notas)
    menor = min(notas)
    situacao = "Aprovado" if media >= 7 else "Reprovado"
    return media, maior, menor, situacao
    notas = []
    contador = 1

    while contador <= 4:
        nota = int(input(f"Digite a nota {contador}: "))
        if 1 <= nota <= 10:
            notas.append(nota)
            contador += 1
        else:
            print("Por favor, digite uma nota de 1 a 10.")

    media, maior, menor, situacao = analisar_notas(notas)

    print(
        f"O(a) estudante obteve uma média de {media:.2f}, "
        f"com a sua maior nota de {maior} pontos e a menor nota de {menor} pontos "
        f"e foi {situacao}."
    )


def media_ponderada(notas, pesos):
     # Apenas treinando funções, parametros e etc
    media = sum(n * p for n, p in zip(notas, pesos)) / sum(pesos)
    return media

    notas = [7.0, 9.0]
    pesos = [2, 3]

    resultado = media_ponderada(notas, pesos)
    print(f"Média Ponderada: {resultado:.2f}")


def treino15():

    # Você recebeu uma demanda para tratar 2 listas com os nomes e sobrenomes de cada estudante concatenando-as para apresentar seus nomes completos na forma Nome Sobrenome O texto exibido ao fim deve ser parecido com:"Nome completo: Ana Silva"

    nomes = ["joão", "MaRia", "JOSÉ"]
    sobrenomes = ["SILVA", "souza", "Tavares"]
    NomeCompleto = []

    # Usamos o range(len(nomes)) para pegar a posição (0, 1, 2)
    for i in range(len(nomes)):
        # Formatamos nome e sobrenome e juntamos com um espaço
        nome_formatado = nomes[i].capitalize()
        sobrenome_formatado = sobrenomes[i].capitalize()
        
        # Criamos a frase e adicionamos na lista
        frase = f"Nome completo: {nome_formatado} {sobrenome_formatado}"
        NomeCompleto.append(frase)

    # Imprimimos um por um para ficar organizado
    for nome in NomeCompleto:
        print(nome)


def calcula_pontos(gols_marcados, gols_sofridos):

    #Crie uma função calcula_pontos(marcados, sofridos) que processe duas listas de gols e retorne a pontuação total (Vitória: 3, Empate: 1, Derrota: 0) e o aproveitamento percentual do time."A pontuação do time foi de [pontos] e seu aproveitamento foi de [aprov]%"

    pontos = 0
    num_jogos = len(gols_marcados)
    
    for m, s in zip(gols_marcados, gols_sofridos):
        if m > s:
            pontos += 3
        elif m == s:
            pontos += 1
            
    aproveitamento = (pontos / (num_jogos * 3)) * 100
    return pontos, aproveitamento
    
    # Guardando tudo nas funções, para quando programa for executado, não puxar tudo
    gols_marcados = [2, 1, 3, 1, 0]
    gols_sofridos = [1, 2, 2, 1, 3]
    pontos, aproveitamento = calcula_pontos(gols_marcados, gols_sofridos)
    print(f"A pontuação do time foi de {pontos} e seu aproveitamento foi de {aproveitamento:.1f}%")


def situacao(lista1, lista2):

    # Função que recebe: notas_prova notas_trabalho Para cada aluno: média = (prova + trabalho)/ Se média ≥ 7 → aprovado Retorne: quantidade de aprovados percentual de aprovação

    aluno = []
    media = []
    for n, s in zip(lista1, lista2):
        media.append((n + s) / 2)
    for n in media:
        if n >= 7:
            aluno.append("Aprovado")
        else:
            aluno.append("Reprovado")
    return media, aluno

    notas_prova = [7, 8, 5]
    notas_trabalho = [5, 10, 8] 
    media, aluno = situacao(notas_prova, notas_trabalho)
    print(f"{aluno}\n{media}")


def treino16():

    # O desafio consiste em desenvolver um sistema que calcule o custo total de uma viagem partindo de Recife para Salvador, Fortaleza, Natal ou Aracaju, estruturado em três funções específicas para hotel, gasolina e lazer. O cálculo deve considerar uma diária fixa de 150 reais, o consumo de um veículo que faz 14 km/l com combustível a 5 reais e custos variáveis de alimentação e passeios conforme o destino escolhido. Para concluir o exercício, é necessário simular especificamente uma viagem de três dias para Salvador, aplicando as distâncias fornecidas e garantindo que o gasto com combustível contabilize tanto o trajeto de ida quanto o de volta.

    print("="*5, "Vamos viajar", "="*5)
    print("Você está em Recife!")

    escolha = input("Você deseja viajar para qual cidade: Salvador, Fortaleza, Natal ou Aracaju? ").lower().strip()

    cidades = ["salvador", "fortaleza", "natal", "aracaju"]

    if escolha not in cidades:
        print("Por favor, escolha uma cidade válida!")
        exit()

    try:
        dias = int(input("Quantos dias você vai ficar lá: "))
    except ValueError:
        print("Por favor, digite a quantidade de dias em NÚMEROS!")
        exit()


    # 🔹 Dicionários com dados organizados
    distancias = {
        "salvador": 850,
        "fortaleza": 800,
        "natal": 300,
        "aracaju": 550
    }

    custos_passeio = {
        "salvador": 200,
        "fortaleza": 400,
        "natal": 250,
        "aracaju": 300
    }


    def gasto_hotel(dias):
        return 150 * dias


    def gasto_gasolina(cidade):
        distancia_total = distancias[cidade] * 2  # ida e volta
        litros = distancia_total / 14
        return litros * 5


    def gasto_passeio(cidade, dias):
        return custos_passeio[cidade] * dias


    print(f"\nVocê vai para: {escolha.capitalize()}")
    print("Segue abaixo os gastos:\n")

    valor_hotel = gasto_hotel(dias)
    valor_gasolina = gasto_gasolina(escolha)
    valor_passeio = gasto_passeio(escolha, dias)

    total = valor_hotel + valor_gasolina + valor_passeio

    print(f"Hotel: R${valor_hotel:.2f}")
    print(f"Gasolina (ida e volta): R${valor_gasolina:.2f}")
    print(f"Passeio e alimentação: R${valor_passeio:.2f}")
    print(f"\nTOTAL DA VIAGEM: R${total:.2f}")


def treino17():
    #Você iniciou um estágio em uma empresa que trabalha com processamento de linguagem natural (NLP). Sua líder requisitou que você criasse um trecho de código que recebe uma frase digitada pela pessoa usuária e filtre apenas as palavras com tamanho maior ou igual a 5, exibindo-as em uma lista. Essa demanda é voltada para a análise do padrão de comportamento de pessoas na escrita de palavras acima dessa quantidade de caracteres.

    frase = input("Digite a frase: ")
    maiores = [p for p in frase.split() if len(p) >= 5]

    print(maiores)



