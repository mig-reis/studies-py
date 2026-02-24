import matplotlib.pyplot as plt   
from random import choice, randrange, sample
import numpy as np
import math
# Exercicios inicias


# Conhecendo plt
def treino1():
    estudantes = ["João", "Maria", "José"]
    notas = [8.5, 9, 6.5]
    plt.bar(x = estudantes, height = notas)
    plt.show()


# Conhecendo Random e funções dele
def treino2():
    estudantes = ["João", "Maria", "José", "Ana"]

    estudante = choice(estudantes)
    print(estudante)

    lista = []
    for i in range(10):
        lista.append(randrange(0, 20, 2))
    
    smp = sample(lista, 3)  
    print(smp)  


# Treinando funções
def treino3():
    lista = [8, 12, 54, 23, 43, 1, 90, 87, 105, 77]
    print(f"Dada a lista: {lista}")
    numero = choice(lista)
    print(f"O numero sorteado foi: {numero}")


# Crie um programa que sorteia, aleatoriamente, um número inteiro positivo menor que 100.
def treino4():
    print("Gerando numero positivo aleatorio de 1 a 100...")
    numero = randrange(100)
    print(f"Numero gerado! O numero é {numero}.")


# Crie um programa que solicite à pessoa usuária digitar 
# dois números inteiros e calcular a potência do 1º número elevado ao 2º.
def treino5():
    print("Por favor, digite dois numero a seguir para calcularmos a potência.")
    numero1 = int(input("Digite o primero numero: "))
    numero2 = int(input("Digite o segundo numero: "))
    result = (numero1 ** numero2)
    print(result)


# Um programa deve ser escrito para sortear uma pessoa seguidora 
# de uma rede social para ganhar um prêmio. A lista de participantes 
# é numerada e devemos escolher aleatoriamente um número de acordo 
# com a quantidade de participantes. Peça à pessoa usuária para fornecer 
# o número de participantes do sorteio e devolva para ela o número sorteado.
def treino6():
    print("VAMOS REALIZAR UM SORTEIO!")

    try:
        quantidade = int(input("Digite a quantidade de participantes: "))
        lista = list(range(1, quantidade + 1))
        print(lista)

        sorteado = choice(lista)
        print(f"Número sorteado: {sorteado}")

    except ValueError:
        print("Digite apenas números!")


# Você recebeu uma demanda para gerar números de token para acessar o 
# aplicativo de uma empresa. O token precisa ser par e variar de 1000 até 
# 9998. Escreva um código que solicita à pessoa usuária o seu nome e exibe 
# uma mensagem junto a esse token gerado aleatoriamente.
def treino7():
    nome = input("Digite o seu nome: ")

    if not nome.isalpha():
        print("Por favor, digite um NOME!")
        return 

    token = randrange(1000, 9998, 2)

    print(f"Bem vindo(a) {nome}! Seu token para acesso é: {token}.")


# Para diversificar e atrair novos(as) clientes, uma lanchonete 
# criou um item misterioso em seu cardápio chamado "salada de 
# frutas surpresa". Neste item, são escolhidas aleatoriamente 3 
# frutas de uma lista de 12 para compor a salada de frutas da pessoa 
# cliente. Crie o código que faça essa seleção aleatória de acordo com a lista abaixo:
def treino8():
    print("Vamos sortear as 3 frutas para compor sua salada de frutas!")

    frutas = ["maçã", "banana", "uva", "pêra", 
          "manga", "coco", "melancia", "mamão",
          "laranja", "abacaxi", "kiwi", "ameixa"]

    print(f"As opções são: {frutas}")

    result = sample(frutas, 3)
    print(f"As frutas sorteadas foram: {', '.join(result)}")


# Você recebeu um desafio de calcular a raiz quadrada de uma lista de números,
#  identificando quais resultaram em um número inteiro. A lista é a seguinte:
def treino8():
    numeros = [2, 8, 15, 23, 91, 112, 256]

    for numero in numeros:
        raiz = math.sqrt(numero)

        if raiz == int(raiz):
            print(f"A raiz quadrada de {numero} é inteira: {int(raiz)}")


# Faça um programa para uma loja que vende grama para jardins. Essa loja 
# trabalha com jardins circulares e o preço do metro quadrado da grama 
# é de R$ 25,00. Peça à pessoa usuária o raio da área circular e devolva 
# o valor em reais do quanto precisará pagar.
def treino9():
    try:

        raio = float(input("Digite o raio da aréa que você deseja adquirir a grama: "))

        area = math.pi * raio ** 2
        valor_final = area * 25

        print(f"O jardim de {area:.2f}m² custará R$ {valor_final:.2f}")

    except ValueError:
        print("Por favor, digite um NUMERO.")
    

# Uma empresa constrói piscinas circulares.
# O custo do revestimento é R$ 120 por m².
# Peça o raio da piscina e mostre: área da piscina e custo total

def treino10():
    try:
        raio = float(input("Digite o raio total da area da piscina: "))

        area = math.pi * raio ** 2
        result = area * 120

        print(f"A piscina de {area:.2f}m² custara R$ {result:.2f}.")
    except ValueError:
        print("Por favor, digite apenas numeros!")
        return


# Uma empresa de paisagismo precisa calcular o custo para preparar um terreno circular.
# O terreno será coberto com grama ao custo de R$ 30,00 por metro quadrado e também
# será cercado, sendo que o custo da cerca é de R$ 80,00 por metro de comprimento.
# Faça um programa que solicite o raio do terreno circular, calcule a área do terreno,
# o comprimento da cerca (circunferência) e determine o custo da grama, o custo da cerca
# e o custo total do projeto. Os valores devem ser exibidos com duas casas decimais.
def treino11():
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



# Escreva um código que lê a lista abaixo e faça: A leitura do tamanho da lista
# A leitura do maior e menor valor e a soma dos valores da lista
def treino12():
    lista = [16, 14, 63, 65, 17, 99, 70, 11, 20, 48, 79, 32, 17, 89, 12, 25, 66]

    tam = len(lista)
    soma = sum(lista)
    maior = max(lista)
    menor = min(lista)

    print(f"A lista possui {tam} números em que o maior número é {maior} e o menor número é {menor}. A soma dos valores presentes nela é igual a {soma}")


#Escreva uma função que gere a tabuada de um número inteiro de 1 a 10, de acordo com a escolha da pessoa usuária. Como exemplo, para o número 7, a tabuada deve ser mostrada no seguinte formato:
def treino13():
    try:
        escolha = int(input("Digite um numero de 1 a 10: "))

        while escolha < 1 or escolha > 10:
            print("Por favor, digite um numero de 1 a 10.")
            escolha = int(input("Digite um numero de 1 a 10: "))

        for n in range(1, 10 + 1):
            print(f"{escolha} X {n} = {(escolha * n)} ")
            

    except ValueError:
        print("Por favor, digite somente numeros inteiros.")


# Crie a função que leia a lista abaixo e retorne uma nova lista com os múltiplos de 3:
# Utilize o return na função e salve a nova lista na variável mult_3.
def treino14():
    lista = [97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]
    mult_3 = [x for x in lista if x % 3 == 0]

    print(mult_3)


# Crie uma lista dos quadrados dos números da seguinte lista . Lembre-se de utilizar as funções lambda e map() para calcular o quadrado de cada elemento da lista.
def treino15():
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    lista_atualizada = list(map(lambda x: x**2, lista))
    print(lista_atualizada)

treino15()
