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
    result = pow(numero1, numero2)
    print(result)

treino5()
