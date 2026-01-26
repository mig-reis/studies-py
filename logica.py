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
    try:
        lista = []
        for n in range(5):
            numero = int(input("Digite um número: "))
            lista.append(numero)
        maior = lista[0]
        menor = lista[0]
        for n in lista:
            if n > maior:
                maior = n
            elif n < menor:
                menor = n
        print(lista)
        print(f"O maior número é: {maior}")
        print(f"O menor número é: {menor}")
    except ValueError:
        print("Por favor, apenas NUMEROS!")

exercicio(8)

def exercicio_8():
    try:
        nomes = []
        for i in range(5):
            nome = input(f"Digite o {i+1}º nome: ")
            nomes.append(nome)
        print("Nomes com mais de 4 letras:")
        for nome in nomes:
            if len(nome) > 4:
                print(nome)
    except ValueError:
        print("Por favor, apenas NUMEROS!")

exercicio(9)

def exercicio_9():
    try:
        lista = []
        numero = int(input("Digite um numero: (-1 para parar)"))
        soma = 0
        media = 0
        while numero > -1:
            lista.append(numero)
            soma += numero
            media += soma / len(lista)
            numero = int(input("Ditie um numero: (-1 para parar)"))
        print(lista)
        print(f"A média dos numeros foi: {media}")
        print(f"A soma dos numeros foi: {soma}")
    except ValueError:
        print("Por favor, apenas numeros!")

exercicio(10)

def exercicio_10():
    try:
        media = {
            "nome": input("Digite seu nome: "),
            "notas": int(input("Qual sua nota? "))
        }
        
        if media["notas"] >= 7:
            print(f"Parabens {media["nome"]}! Você foi APROVADO!") 
    except ValueError:
        print("Por favor, apenas NUMEROS!")
exercicio(11)

def exercicio_11():
        compras = {
            "Cerveja": 2.99,
            "Carne": 49.99,
            "Chinelo": 29.99
        }
        
        print(compras)

        maior = 0
        produto = ""

        for chave in compras:
            valor_atual = compras[chave]
            if valor_atual > maior:
                maior = valor_atual
                produto = chave
        
        print(f"O produto {produto} é o mais caro, custando {maior}R$.")
           
exercicio(12)

def exercicio_12():
    dicionario = {
        "João": 12,
        "Miguel": 18,
        "Leticia": 15,
        "Marli": 64
    }

    print(dicionario)

    maior_de_idade = 0
    nome = ""

    for n in dicionario:
        idade_atual = dicionario[n]
        if idade_atual >= 18:
            nome = n
            print(f"{nome} é maior de idade!")

exercicio(13)

def exercicio_13():
    try:
        numeros = []
        maior = 0
        for n in range(2):
            numero = int(input("Digite um numero: "))
            numeros.append(numero)
        for i in numeros:
            numero_atual = numeros[1]
            if numero_atual > maior:
                maior = numero_atual
        print(numeros)
        print(f"O maior numero é: {maior}")
    except ValueError:
        print("Por favor, somente NUMEROS!  ")

exercicio(14)