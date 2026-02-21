import matplotlib.pyplot as plt   
from random import choice, randrange, sample
import numpy as np
from math import pow
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


def treino4():
    print("Gerando numero positivo aleatorio de 1 a 100...")
    numero = randrange(100)
    print(f"Numero gerado! O numero é {numero}.")


def treino5():
    print("Por favor, digite dois numero a seguir para calcularmos a potência.")
    numero1 = int(input("Digite o primero numero: "))
    numero2 = int(input("Digite o segundo numero: "))
    result = (numero1 ** numero2)
    print(result)

#Um programa deve ser escrito para sortear uma pessoa seguidora de uma 
# rede social para ganhar um prêmio. A lista de participantes é numerada e 
# devemos escolher aleatoriamente um número de acordo com a quantidade de participantes. 
# Peça à pessoa usuária para fornecer o número de participantes do sorteio e devolva 
# para ela o número sorteado.
def treino6():
    print("VAMOS REALIZAR UM SORTEIO!")

    try:
        quantidade = int(input("Digite a quantidade de participantes: "))
        lista = list(range(1, quantidade + 1))

        sorteado = choice(lista)
        print(f"Número sorteado: {sorteado}")

    except ValueError:
        print("Digite apenas números!")

treino6()
