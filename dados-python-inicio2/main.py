import matplotlib.pyplot as plt   
from random import choice, randrange, sample
import numpy as np
# Exercicios inicias

def treino1():
    estudantes = ["João", "Maria", "José"]
    notas = [8.5, 9, 6.5]
    plt.bar(x = estudantes, height = notas)
    plt.show()

def treino2():
    estudantes = ["João", "Maria", "José", "Ana"]

    estudante = choice(estudantes)
    print(estudante)

    lista = []
    for i in range(10):
        lista.append(randrange(0, 20, 2))
    
    smp = sample(lista, 3)  
    print(smp)  



