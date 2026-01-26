def exercicio(nome):
    print("-"*12)
    print(f"Exercicio {nome}")
    print("-"*12)

exercicio(1)

def exercicio_1():
    try:
        number1 = int(input("Digite 1 numero: "))
        number2 = int(input("Digite outro numero: "))
        if number1 > number2:
            print(f"{number1} é maior que {number2}.")
        elif number1 == number2:
            print("Os numeros são iguais.")
        else:
            print(f"{number2} é maior que {number1}.")
    except ValueError:
        print("Por favor, apenas numeros.")

exercicio(2)

def exercicio_2():
    try:
        numero = int(input("Digite um numero: "))
        if numero > 0:
            print(f"{numero} é um numero POSITIVO.")
        elif numero < 0:
            print(f"{numero} é um numero NEGATIVO.")
        else:
            print("Seu numero é ZERO.")
    except ValueError:
        print("Por favor, digite apenas numeros!")

exercicio(3)

def exercicio_3():
    try:
        notas = []
        soma = 0
        for n in range(3):
            nota = int(input("Digite a nota: "))
            notas.append(nota)
            soma += nota
        media = soma / len(notas)
        print(notas)
        print(f"A média das suas notas foi: {media}.")
        if media >= 7:
            print("Parabens! Você foi APROVADO.")
        elif media < 7:
            print("Infelizmente você foi REPROVADO!")
    except ValueError:
        print("Por favor, digite apenas numeros.")

exercicio(4)

def exercicio_4():
    for n in range(0, 51, 2):
        print(n)
        
exercicio(5)

def exercicio_5():
    numero = int(input("Digite um numero: "))
    for n in range(1, 11):
        resultado = numero * n
        print(f"{numero} X {n} = {resultado}")

exercicio(6)

def exercicio_6():
    try:
        numero = int(input("Digite um numero (0 para parar): "))
        soma = 0
        contador = 0
        while numero > 0:
            contador += 1
            soma += numero
            numero = int(input("Digite um numero: "))
        print(f"Você digitou {contador} numeros.")
        print(f"A soma dos numeros digitados é: {soma}")
    except ValueError:
        print("Por favor, digite apenas NUMEROS.")


exercicio(7)

def exercicio_7():
    lista = []
    maior = 0
    menor = 0
    for n in range(5):
        numeros = int(input("Digite o numero: "))
        lista.append(numeros)
        if numeros > len(lista):
            maior = numeros
        elif numeros < len(lista):
            menor = numeros
    print(lista)
    print(f"O maior numero é: {maior}")
    print(f"O menor numero é : {menor}")
exercicio_7()
