from colorama import Fore, Style

def exercicio(numero):
    print(Fore.CYAN + "--------------")
    print(Fore.CYAN + f" Exercicio {numero}")
    print(Fore.CYAN + "--------------")
    print(Fore.WHITE + "")

def par_or_impar():
    print(Fore.BLACK + "Digite um numero a seguir, e informaremos se ele é PAR ou IMPAR\n")
    try:
        numero = int(input(Fore.WHITE + "Digite o numero: "))
        if numero % 2 == 0:
            print(Fore.BLUE + f"\nO numero {numero} é par.")
            print(Fore.WHITE + "")
        else:
            print(Fore.BLUE + f"\nO numero {numero} é impar.")
            print(Fore.WHITE + "")
    except ValueError:
        print(Fore.RED + "Por favor, digite somente NUMEROS INTEIROS!")
        print(Fore.WHITE + "")
        return par_or_impar()


def maior_or_menor():
    print(Fore.BLACK + "Digite dois numeros a seguir, e mostramos qual é MAIOR.")
    try:
        numb1 = int(input(Fore.WHITE + "\nDigite o primeiro numero: "))
        numb2 = int(input("Digite o segundo numero: "))
        if numb1 > numb2:
            print(Fore.BLUE + f"\nO numero {numb1} é maior.")
            print(Fore.WHITE + "")
        elif numb2 > numb1:
            print(Fore.BLUE + f"\nO numero {numb2} é maior.")
            print(Fore.WHITE + "")
        else:
            print(Fore.BLUE + "\nOs numeros são iguais.")
            print(Fore.WHITE + "")
    except ValueError:
        print(Fore.RED + "Por favor digite somente numeros inteiros.")
        print(Fore.WHITE + "")
        return maior_or_menor()

def contador():
    print(Fore.BLACK + "Digite um numero que iremos contar ate ele.")
    try:
        numero = int(input(Fore.WHITE + "Digite o numero: "))
        for n in range(1, numero + 1):
            print(Fore.BLUE + f"{n}")
        print(Style.RESET_ALL) 
    except ValueError:
        print(Fore.RED + "Por favor, digite somente numeros inteiros!")
        print(Style.RESET_ALL)
        return contador()
     

#Chamando as funções
contador()