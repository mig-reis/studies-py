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