from colorama import Fore
import random

def inicio():   # Layout inicial
    print(Fore.BLUE + "-" * 15)
    print("PROJETO FINAL")
    print("-" * 15)
    print(Fore.WHITE + "")


def exercicio(numero):  
    print(Fore.BLACK + f"EXERCICIO {numero}")
    print(Fore.WHITE + "")


#Calculando média de gastos de uma empresa
def exercicio_1():
    print("Dado os seguintes gastos de uma empresa de papel: ")

    gastos = [2172.54, 3701.35, 3518.09, 3456.61, 
              3249.38, 2840.82, 3891.45, 3075.26,
              2317.64, 3219.08]

    print(Fore.RED + f"{gastos}", Fore.WHITE + "")
    print("Vamos calcular a média desses gastos.")

    media = sum(gastos) / len(gastos)   # Usando funções built-in para calcular a média.

    print("A média dos gastos é:", Fore.GREEN + f"{media}.", Fore.WHITE + "")


#Com os mesmos dados da questão anterior, defina quantas compras foram realizadas acima de 3000 reais e calcule a porcentagem quanto ao total de compras.
def exercicio_2():
    print("Ainda com os mesmos dados")

    gastos = [2172.54, 3701.35, 3518.09, 3456.61, 
              3249.38, 2840.82, 3891.45, 3075.26,
              2317.64, 3219.08]

    print(Fore.RED + f"{gastos}", Fore.WHITE + "")
    print(Fore.BLACK + "Vamos mostrar quantas vendas foram realizadas acima de 3.000 e a porcentagem em relação ao total de compras.", Fore.WHITE + "")

    contador = 0

    for valor in gastos:
        if valor > 3000:
            contador += 1
    
    print("Foram realizadas", Fore.GREEN + f"{contador}", Fore.WHITE + "compras acima de 3 mil.")
    
    porcentagem = (contador / len(gastos)) * 100

    print("A porcentagem que representa no total de compras é de:", Fore.GREEN + f"{porcentagem:.0f}%", Fore.WHITE + "")
    

#Receber uma letra e informar se é vogal ou consoante.
def exercicio_3():
        letra = input("Digite uma letra: ").upper()

        if len(letra) != 1 or letra not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            print(Fore.RED + "Por favor, digite uma letra.", Fore.WHITE + "")
            
        else:

            if letra not in "AEIOU":
                print(Fore.GREEN + f"{letra} é uma CONSOANTE.", Fore.WHITE + "")
            else:
                print(Fore.GREEN + f"{letra} é uma VOGAL.", Fore.WHITE + "")


#Faça um código que colete em uma lista 5 números inteiros quaisquer e imprima a lista.
def exercicio_4():
    print(Fore.BLUE + "Gerando numeros...", Fore.WHITE + "")

    lista = [random.randint(1, 9) for _ in range(5)]

    print(Fore.GREEN + "Numeros gerados", Fore.WHITE + "")
    print(lista)


#Colete novamente 5 inteiros e imprima a lista em ordem inversa à enviada.
def exercicio_5():
    print("Gerando a lista...")
    print(Fore.BLUE + "Lista gerada!", Fore.WHITE + "")

    lista = [random.randint(1, 9) for i in range(5)]

    print(lista)

    print(Fore.BLUE + "Agora, em ordem inversa.", Fore.WHITE + "")
    print(lista[::-1])


#Faça um programa que, ao inserir um número qualquer, cria uma 
# lista contendo todos os números primos entre 1 e o número digitado.
def exercicio_6():
    try:
        numero = int(input("Digite um numero entre 1 e 100: "))

        if numero > 100:
            print(Fore.RED + "O numero digitado é MAIOR que 100!", Fore.WHITE + "")
            return False

        lista = []
        contador = 0

        numeros_primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 
                          29, 31, 37, 41, 43, 47, 53, 59, 
                          61, 67, 71, 73, 79, 83, 89, 97.]
        
        for n in numeros_primos:
            if n > numero:
                break 
            lista.append(n)
            contador += 1

        print(Fore.BLUE + f"Numeros primos até {numero}: {contador}", Fore.WHITE + "")
        print(lista)

                
    except ValueError:
        print("Por favor, digite apenas numeros inteiros.")


exercicio_6()

