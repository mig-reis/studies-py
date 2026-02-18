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


#6) Escreva um programa que peça uma data informando o dia, 
# mês e ano e determine se ela é válida para uma análise.
def exercicio_7():
    try:
        print(Fore.BLUE + "Por favor, insira uma data a seguir 👇 ", Fore.WHITE + "")

        dia = int(input("Digite o dia: "))

        if dia < 1 or dia > 31:
            print(Fore.RED + "Por favor, digite um dia valido!", Fore.WHITE + "")
            return False

        mes = int(input("Digite o mês (ex: janeiro = 1): "))

        if mes not in range(1, 13):
            print(Fore.RED + "Por favor, digite em um formato valido. Ex: junho = 6.", Fore.WHITE + "")
            return False
        else:
            if mes < 10:
                mes = f"0{mes}"

        ano = int(input("Digite o ano: "))
        if ano > 2027 or ano < 1927:
            print(Fore.RED + "Por favor, digite um ano valido.", Fore.WHITE + "")
            return False
        else:
            print(Fore.GREEN + "Data valida!", Fore.WHITE + "")
            print(Fore.BLACK + f"{dia}|{mes}|{ano}", Fore.WHITE + "")

    except ValueError:
        print(Fore.RED + "Por favor, digite um NUMERO!", Fore.WHITE + "")
        return


#O exercício fornece uma lista com a quantidade de bactérias por dia e pede 
# para criar um programa que calcule o percentual de crescimento diário, 
# comparando o valor de cada dia com o do dia anterior
def exercicio_8():
    print("Dada a lista de aumento do numero de bacterias por dia:")

    bacterias_por_dia = [1.2, 2.1, 3.3, 5.0, 7.8, 11.3, 16.6, 25.1, 37.8, 56.9]

    print(Fore.BLACK + f"{bacterias_por_dia}", Fore.WHITE + "")

    for i in range(1, len(bacterias_por_dia)):
        amostra_passada = bacterias_por_dia[i-1]
        amostra_atual = bacterias_por_dia[i]

        calculo = 100 * (amostra_atual - amostra_passada) / amostra_passada

        print(f"Do dia {i} para o dia {i+1}, aumentou:", Fore.GREEN + f"{calculo:.2f}%", Fore.WHITE + "")

    # crescimento do dia 1 ao 10
    calculo_total = 100 * (bacterias_por_dia[-1] - bacterias_por_dia[0]) / bacterias_por_dia[0]
    print(f"Do dia 1 em relação ao dia 10, aumentou:", Fore.BLUE + f"{calculo_total:.1f}%", Fore.WHITE + "")


#8) Para uma seleção de produtos alimentícios, precisamos separar o 
# conjunto de IDs dados por números inteiros sabendo que os produtos 
# com ID par são doces e os com ID ímpar são amargos.
#  Monte um código que colete 10 IDs. Depois, calcule e mostre a quantidade de produtos doces e amargos.
def exercicio_9():
    print(Fore.BLUE + "Insira o ID de 10 produtos alimenticios (ex:7728) : ", Fore.WHITE + "")

    ids = []
    contador = 1

    while len(ids) < 10:
        id = input(Fore.BLACK + f"Digite o id {contador}: ")

        if not id.isdigit():
            print(Fore.RED + "Por favor, DIGITE SOMENTE NUMEROS!", Fore.WHITE + "")
            continue

        if len(id) != 4:
            print(Fore.RED + "Por favor, digite um formato de id valido! Contendo 4 numeros.", Fore.WHITE + "")
            continue

        ids.append(id)
        contador += 1

    doce = []
    amargo = []

    for id in ids:
        if int(id) % 2 == 0:
            doce.append(id)
        else:
            amargo.append(id)

    print(
        Fore.CYAN + "\nLista de ids:", Fore.WHITE + f"\n{ids}",
        Fore.GREEN + "\nProdutos doce:", Fore.WHITE + f"{doce}",
        Fore.GREEN + "\nProdutos amargos:", Fore.WHITE + f"{amargo}"
    )


#um programa que informa a nota de um(a) aluno(a) de acordo com suas respostas. 
# Ele deve pedir a resposta desse(a) aluno(a) para cada questão e é preciso verificar 
# se a resposta foi igual ao gabarito. Cada questão vale um ponto e existem as alternativas A, B, C ou D.
def exercicio_10():

    gabarito = {
        1: "D", 2: "A", 3: "C",
        4: "B", 5: "A", 6: "D",
        7: "C", 8: "C", 9: "A",
        10: "B"
    }

    acertos = 0
    erros = 0

    for questao in gabarito:

        nota = input(f"Digite a ALTERNATIVA da questão {questao}: ").upper()

        while nota not in ["A", "B", "C", "D"]:
            print("Por favor, digite uma alternativa valida! (A, B, C ou D)")
            nota = input(f"Digite a ALTERNATIVA da questão {questao}: ").upper()

        if nota == gabarito[questao]:
            acertos += 1
        else:
            erros += 1

    if acertos >= 6:
        print(Fore.GREEN + "Parabens! Você foi aprovado!", Fore.WHITE + f"\nAcertos: {acertos}", f"\nErros: {erros}")
    else:
        print(Fore.RED + f"Poxa, você errou {erros} perguntas e infelizmente foi REPROVADO!", Fore.WHITE + "")


#Criar um programa que registre a temperatura média de cada mês do ano em uma lista,
#  calcule a média anual e exiba apenas as temperaturas que ficaram acima dessa média,
#  indicando também os meses correspondentes por extenso.
def exercicio_11():


