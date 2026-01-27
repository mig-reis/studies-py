from colorama import Fore  # importa cores para o terminal


def exercicio(nome):
    print(Fore.WHITE + "-" * 12)  # imprime linha separadora
    print(Fore.BLUE + f"Exercicio {nome}")  # mostra o número do exercício
    print(Fore.WHITE + "-" * 12)  # imprime linha separadora


def exercicio_1():
    print(Fore.BLACK + "Vamos comparar os numeros, e resultar o maior e o menor.")
    print(Fore.WHITE + "")
    try:
        number1 = int(input("Digite 1 numero: "))  # recebe o primeiro número
        number2 = int(input("Digite outro numero: "))  # recebe o segundo número

        if number1 > number2:  # verifica se o primeiro é maior
            print(f"{number1} é maior que {number2}.")
        elif number1 == number2:  # verifica se são iguais
            print("Os numeros são iguais.")
        else:  # caso o segundo seja maior
            print(f"{number2} é maior que {number1}.")
    except ValueError:  # trata erro caso não seja número
        print(Fore.RED + "Por favor, apenas numeros.")


def exercicio_2():
    print(Fore.BLACK + "Vamos ver se o numero digitado é NEGATIVO ou POSITIVO.")
    print(Fore.WHITE + "")
    try:
        numero = int(input("Digite um numero: "))  # recebe o número do usuário
        if numero > 0:  # verifica se é positivo
            print(f"{numero} é um numero POSITIVO.")
        elif numero < 0:  # verifica se é negativo
            print(f"{numero} é um numero NEGATIVO.")
        else:  # se for zero
            print("Seu numero é ZERO.")
    except ValueError:
        print(Fore.RED + "Por favor, digite apenas numeros!")


def exercicio_3():
    print(Fore.BLACK + "Digite 3 notas e vamos mostrar a média.")
    print(Fore.WHITE + "")
    try:
        notas = []  # lista para armazenar as notas
        soma = 0  # variável para somar as notas

        for n in range(3):  # loop para pedir 3 notas
            nota = int(input("Digite a nota: "))  # recebe a nota
            notas.append(nota)  # adiciona a nota na lista
            soma += nota  # soma a nota ao total

        media = soma / len(notas)  # calcula a média das notas
        print(notas)  # mostra a lista de notas
        print(f"A média das suas notas foi: {media}")

        if media >= 7:  # verifica aprovação
            print("Parabens! Você foi APROVADO.")
        else:  # caso reprovado
            print("Infelizmente você foi REPROVADO!")
    except ValueError:
        print(Fore.RED + "Por favor, digite apenas numeros.")


def exercicio_4():
    print(Fore.BLACK + "Vamos mostrar todos os numeros PARES de 0 a 50.")
    print(Fore.WHITE + "")
    for n in range(0, 51, 2):  # loop que pula de 2 em 2 (somente pares)
        print(n)


def exercicio_5():
    print(Fore.BLACK + "Tabuada de 1 a 10.")
    print(Fore.WHITE + "")
    try:
        numero = int(input("Digite um numero: "))  # recebe o número base
        for n in range(1, 11):  # loop de 1 até 10
            print(f"{numero} X {n} = {numero * n}")  # calcula a tabuada
    except ValueError:
        print(Fore.RED + "Por favor, apenas NUMEROS!")


def exercicio_6():
    print(Fore.BLACK + "Digite numeros para somar (0 para parar).")
    print(Fore.WHITE + "")
    try:
        soma = 0  # guarda a soma total
        contador = 0  # conta quantos números foram digitados
        numero = int(input("Digite um numero: "))  # recebe o primeiro número

        while numero > 0:  # loop enquanto o número for maior que zero
            soma += numero  # soma o número atual
            contador += 1  # incrementa o contador
            numero = int(input("Digite um numero: "))  # pede novo número

        print(f"Você digitou {contador} numeros.")
        print(f"A soma dos numeros é: {soma}")
    except ValueError:
        print(Fore.RED + "Por favor, apenas NUMEROS!")


def exercicio_7():
    print(Fore.BLACK + "Digite 5 numeros e vamos mostrar o MAIOR e o MENOR.")
    print(Fore.WHITE + "")
    try:
        lista = []  # lista para armazenar os números
        for n in range(5):  # loop para pedir 5 números
            numero = int(input("Digite um número: "))  # recebe o número
            lista.append(numero)  # adiciona na lista

        maior = lista[0]  # assume o primeiro como maior
        menor = lista[0]  # assume o primeiro como menor

        for n in lista:  # percorre a lista
            if n > maior:  # verifica se é maior
                maior = n
            elif n < menor:  # verifica se é menor
                menor = n

        print(lista)
        print(f"O maior número é: {maior}")
        print(f"O menor número é: {menor}")
    except ValueError:
        print(Fore.RED + "Por favor, apenas NUMEROS!")


def exercicio_8():
    print(Fore.BLACK + "Digite 5 nomes.")
    print(Fore.WHITE + "")
    nomes = []  # lista para armazenar os nomes

    for i in range(5):  # loop para pedir 5 nomes
        nome = input(f"Digite o {i+1}º nome: ").lower()  # recebe e converte para minúsculo
        nomes.append(nome)  # adiciona o nome na lista

    print("Nomes com mais de 4 letras:")
    for nome in nomes:  # percorre a lista de nomes
        if len(nome) > 4:  # verifica o tamanho do nome
            print(nome)


def exercicio_9():
    print(Fore.BLACK + "Digite numeros (-1 para parar).")
    print(Fore.WHITE + "")
    lista = []  # lista para armazenar os números
    soma = 0  # variável para somar

    numero = int(input("Digite um numero: "))  # recebe o primeiro número
    while numero != -1:  # loop até digitar -1
        lista.append(numero)  # adiciona número na lista
        soma += numero  # soma o número
        numero = int(input("Digite um numero: "))  # pede outro número

    media = soma / len(lista)  # calcula a média
    print(lista)
    print(f"A soma é: {soma}")
    print(f"A média é: {media}")


def exercicio_10():
    print(Fore.BLACK + "Digite seu nome e sua nota.")
    print(Fore.WHITE + "")
    dados = {
        "nome": input("Digite seu nome: "),  # armazena o nome
        "nota": int(input("Digite sua nota: "))  # armazena a nota
    }

    if dados["nota"] >= 7:  # verifica se passou
        print(f"Parabens {dados['nome']}! Você foi APROVADO.")
    else:  # caso reprovado
        print(f"{dados['nome']}, você foi REPROVADO.")


def chamando_funcoes():
    exercicio(1); exercicio_1()  # chama exercício 1
    exercicio(2); exercicio_2()  # chama exercício 2
    exercicio(3); exercicio_3()  # chama exercício 3
    exercicio(4); exercicio_4()  # chama exercício 4
    exercicio(5); exercicio_5()  # chama exercício 5
    exercicio(6); exercicio_6()  # chama exercício 6
    exercicio(7); exercicio_7()  # chama exercício 7
    exercicio(8); exercicio_8()  # chama exercício 8
    exercicio(9); exercicio_9()  # chama exercício 9
    exercicio(10); exercicio_10()  # chama exercício 10


chamando_funcoes()  # inicia o programa
# 🧠 Exercícios de Lógica em Python

Este repositório contém uma coleção de exercícios desenvolvidos para praticar **lógica de programação em Python**.

Os exercícios foram criados com foco em:
- Fixar conceitos fundamentais
- Melhorar o raciocínio lógico
- Praticar boas práticas iniciais de programação

---

## 📌 Conteúdos praticados

- Estruturas condicionais (`if / elif / else`)
- Laços de repetição (`for` e `while`)
- Listas
- Dicionários
- Funções (`def`)
- Tratamento de erros (`try / except`)
- Contadores e acumuladores
- Entrada e saída de dados

---

## 📂 Organização

Cada exercício está separado em uma função numerada (`exercicio_1`, `exercicio_2`, etc.),  
e uma função principal (`chamando_funcoes`) é responsável por executar todos.

---

## 🚧 Status do projeto

🟢 Concluido 
Esses exercicios foram fundamentais para meu desenvolvimento, e ter os mesmos registrados é de extrema importancia.

---

## 🎯 Objetivo

Criar um repositório de estudos para:
- Acompanhar minha evolução em Python
- Reforçar lógica de programação
- Servir como material de revisão futura

---

## 🛠️ Tecnologias utilizadas

- Python 3.x
- Biblioteca `colorama` (para estilização do terminal)

---

## 📌 Observação

Este projeto faz parte do meu processo de aprendizado.
Sugestões e melhorias são sempre bem-vindas 🙂
