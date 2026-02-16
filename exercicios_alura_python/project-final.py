from colorama import Fore


def inicio():   # Layout inicial
    print(Fore.BLUE + "-" * 15)
    print("PROJETO FINAL")
    print("-" * 15)
    print(Fore.WHITE + "")


def exercicio(numero):  
    print(Fore.BLACK + f"EXERCICIO {numero}")
    print(Fore.WHITE + "")


def exercicio_1():
    print("Dado os seguintes gastos de uma empresa de papel: ")

    gastos = [2172.54, 3701.35, 3518.09, 3456.61, 
              3249.38, 2840.82, 3891.45, 3075.26,
              2317.64, 3219.08]

    print(Fore.RED + f"{gastos}", Fore.WHITE + "")
    print("Vamos calcular a média desses gastos.")

    media = sum(gastos) / len(gastos)   # Usando funções built-in para calcular a média.

    print("A média dos gastos é:", Fore.GREEN + f"{media}.", Fore.WHITE + "")


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
    

exercicio_2()

