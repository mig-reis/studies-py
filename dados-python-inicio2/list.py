def soma(lista):
    #Crie um código para imprimir a soma dos elementos de cada uma das listas contidas na seguinte lista:
    return [sum(n) for n in lista]


lista_de_listas = [[4,6,5,9], [1,0,7,2], [3,4,1,8]]
soma_elementos = soma(lista_de_listas)
print(soma_elementos)
    
