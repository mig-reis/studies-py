print("Escola de dados alura")
# Arquivo exclusivo para exercícios do curso
# Foco em lógica e aprendizado, não em interface bonita


def ex2():
    nome = input("Digite o seu nome: ")
    sobrenome = input("Digite seu sobrenome: ")
    # Uso de f-string para exibir os dados
    print(f"Nome: {nome}")
    print(f"Sobrenome: {sobrenome}")


def ex3():
    nome = input("Digite o seu nome: ")
    # Percorre cada caractere da string
    for L in nome:
        print(L)


def ex4():
    try:
        # Converte o dia para inteiro
        dia = int(input("Digite o dia do seu aniversário: "))
        # Valida se o dia está entre 1 e 31
        if dia <= 31 and dia > 0:
            pass
        else:
            print("Data invalida!")
            return False 

        # Lê o mês como texto e converte para minúsculo
        mes = input("Digite o nome do mês do seu aniversario: ").lower()
        # Verifica se contém apenas letras
        if mes.isalpha():
            pass
        else:
            print("Por favor, digite o NOME do mês!")
            return False

        # Converte o ano para inteiro
        ano = int(input("Digite o ano do seu nascimento: "))
        # Validação simples de faixa de ano
        if ano >= 1926 and ano < 2027:
            pass
        else:
            print("Data INVALIDA!")
            return False

        # Exibe a data formatada
        print(f"{dia} de {mes} de {ano}.")
    except ValueError:
        # Captura erro caso o usuário digite texto ao invés de número
        print("Por favor, digite um NUMERO!")


def ex5():
    try:
        ano = int(input("Digite qual ano você esta: "))
        print(f"Ano atual: [{ano}]")
    except ValueError:
        print("Por favor, somente NUMEROS!")


# Pede dois números e mostra o maior
def ex6():
    print("O usuario deve digitar dois numeros, e retornaremos o MAIOR.")
    try:
        number1 = int(input("Digite o primeiro numero: "))
        number2 = int(input("Digite o segundo numero: "))

        # Comparação direta entre os números
        if number1 > number2:
            print(f"O numero: {number1} é o MAIOR.")
        elif number2 > number1:
            print(f"O numero: {number2} é o MAIOR.")
        else:
            print("Os numeros são iguais.")
    except ValueError:
        print("Por favor, somente NUMEROS INTEIROS!")


# Analisa crescimento ou decrescimento percentual
def ex7():
    print("O usuario deve digitar o percentual de crescimento de produção de uma empresa.")
    try:
        percentual1 = int(input("Digite o porcentual de crescimento de 2024: "))
        percentual2 = int(input("Digite o percentual de crescimento de 2025: "))

        # Se houve crescimento
        if percentual2 > percentual1:
            div = percentual2 / percentual1 - 1
            porcentagem = int(div * 100)
            print(f"PARABENS! Houve um crescimento POSITIVO de {porcentagem}%!")

        # Se houve queda
        elif percentual1 > percentual2:
            div = percentual1 / percentual2 - 1
            porcentagem = int(div * 100)
            print(f"POXA! Houve um decrescimento NEGATIVO de {porcentagem}%!")

        # Crescimento igual
        else:
            print("A empresa cresceu na mesma proporção ambos os anos!")
    except ValueError:
        print("Digite somente números, sem %.")


# Verifica se a letra é vogal ou consoante
def ex8():
    letra = input("Digite uma letra: ").strip().upper()

    # Verifica se foi digitado apenas um caractere
    if len(letra) != 1:
        print("Digite apenas UMA letra.")
        return

    # Verifica se é uma letra do alfabeto
    if not letra.isalpha():
        print("Digite apenas letras do alfabeto.")
        return

    # Verifica se é vogal
    if letra in "AEIOU":
        print(f"{letra} é uma VOGAL.")
    else:
        print(f"{letra} é uma CONSOANTE.")


# Mostra o maior valor do carro em 3 anos
def ex9():
    print("Informe o valor médio do carro por 3 anos.")
    carro = input("Informe o modelo do carro: ")
    try:
        ano1 = float(input("Valor em 2020: "))
        ano2 = float(input("Valor em 2021: "))
        ano3 = float(input("Valor em 2022: "))

        # Comparações para achar o maior valor
        if ano1 > ano2 and ano1 > ano3:
            print(f"Em 2020 o {carro} teve maior valor: R$ {ano1}")
        elif ano2 > ano1 and ano2 > ano3:
            print(f"Em 2021 o {carro} teve maior valor: R$ {ano2}")
        elif ano3 > ano1 and ano3 > ano2:
            print(f"Em 2022 o {carro} teve maior valor: R$ {ano3}")
    except ValueError:
        print("Por favor, digite somente NUMEROS!")


# Encontra o produto mais barato
def ex10():
    produtos = {
        "Garrafa": 14.99,
        "Teclado": 49.99,
        "Caderno": 11.99,
        "Lapís": 1.99
    }

    print(produtos)

    barato = None
    nome = None

    # Inicializa com o primeiro item do dicionário
    for preco in produtos:
        barato = produtos[preco]
        nome = preco
        break

    # Compara os valores para achar o menor
    for preco in produtos:
        if barato > produtos[preco]:
            barato = produtos[preco]
            nome = preco

    print(f"{nome} é o produto mais barato, custando: {barato} R$.")


# Exibe três números em ordem decrescente
def ex11():
    try:
        number1 = int(input("Digite o primeiro numero: "))
        number2 = int(input("Digite o segundo numero: "))
        number3 = int(input("Digite o terceito numero: "))

        maior = None
        meio = None
        menor = None

        # Lógica manual de comparação
        if number1 > number2 and number1 > number3:
            maior = number1
            if number2 > number3:
                meio = number2
                menor = number3
            else:
                meio = number3
                menor = number2

        elif number2 > number3 and number2 > number1:
            maior = number2
            if number1 > number3:
                meio = number1
                menor = number3
            else:
                meio = number3
                menor = number1

        else:
            maior = number3
            if number2 > number1:
                meio = number2
                menor = number1
            else:
                meio = number1
                menor = number2

        print(maior, meio, menor)
    except ValueError:
        print("Por favor, somente NUMEROS!")


# Mensagem de acordo com o turno
def ex12():
    try:
        pergunta = int(input("Qual turno você estuda? 1-Manhã 2-Tarde 3-Noite: "))
        if pergunta == 1:
            print("Bom dia!")
        elif pergunta == 2:
            print("Boa tarde!")
        elif pergunta == 3:
            print("Boa noite!")
        else:
            print("Alternativa INVALIDA.")
    except ValueError:
        print("Responda somente com o numero que representa a sua resposta (ex: 1 para manhã).")


# Verifica se o número é par ou ímpar
def ex13():
    try:
        numero = int(input("Digite um numero inteiro: "))
        if numero % 2 == 0:
            print("Seu numero é PAR!")
        else:
            print("Seu numero é IMPAR!")
    except ValueError:
        print("Digite somente NUMEROS INTEIROS!")


# Verifica se o número é inteiro ou decimal
def ex14():
    numero = input("Digite um numero: ")
    try:
        if numero.isdigit():
            print(f"{int(numero)} é um NUMERO INTEIRO.")
        else:
            print(f"{float(numero)} é um NUMERO DECIMAL.")
    except ValueError:
        print("Digite apenas NUMEROS!")


# Operações matemáticas + classificação do resultado
def ex15():
    try:
        numb1 = int(input("Digite o primeiro numero: "))
        numb2 = int(input("Digite o segundo numero: "))
        escolha = input("Operação (+, -, x ou /): ")

        if escolha == "+":
            resultado = numb1 + numb2
        elif escolha == "-":
            resultado = numb1 - numb2
        elif escolha == "x":
            resultado = numb1 * numb2
        elif escolha == "/":
            resultado = numb1 / numb2
        else:
            print("Operação invalida.")
            return

        # Par ou ímpar
        par_impar = "par" if resultado % 2 == 0 else "impar"

        # Positivo ou negativo
        positivo_negativo = "positivo" if resultado >= 0 else "negativo"

        # Inteiro ou decimal
        inteiro_decimal = "inteiro" if resultado == int(resultado) else "decimal"

        print(f"O resultado da conta é: {resultado}")
        print(f"O numero é: {par_impar}, {positivo_negativo} e {inteiro_decimal}")
    except ValueError:
        print("Digite apenas NUMEROS!")

def ex16():
    print("O usuario deve informar três números que representam os lados de um triângulo.")
    try:
        lado1 = int(input("Digite o primeiro lado: "))
        lado2 = int(input("Digite o segundo lado: "))
        lado3 = int(input("Digite o terceiro lado: "))

        maior = None
        menor1 = None
        menor2 = None

        if lado1 > lado2 and lado1 > lado3:
            maior = lado1
            menor1 = lado2
            menor2 = lado3
        elif lado2 > lado1 and lado2 > lado3:
            maior = lado2
            menor1 = lado1
            menor2 = lado3
        elif lado3 > lado2 and lado3 > lado1:
            maior = lado3
            menor1 = lado1
            menor2 = lado2

        print(menor1, menor2, maior)
        soma = menor1 + menor2
        print(soma)
        triangulo = None

        if soma > maior:
            triangulo = "Sim"
        else:
            triangulo = "Não"

        print(f"Essas medidas podem formar um trinagulo: {triangulo}.")
        tipo = None
        
        if triangulo == "Sim":
            if lado1 == lado2 and lado1 == lado3 and lado2 == lado3:    
                tipo = "Equilatero"
            elif lado1 == lado2 and lado1 == lado3 or lado2 == lado3:
                tipo = "Isósceles "       
            else:
                tipo = "Escaleno"
        
        print(f"O triangulo é: {tipo}. ")
    
    except ValueError:
        print("Por favor, digite apenas NUMEROS!")
    

def ex17():
    print("-" * 30)
    print("Bem-vindo ao nosso posto!")
    print("-" * 30)

    try:
        combustivel = input("Qual combustível você deseja por? (E)tanol ou (D)iesel: ").lower().strip()

        if combustivel not in ("e", "d"):
            print("Responda apenas com E ou D.")
            return

        litros = float(input("Quantos litros deseja abastecer? "))

        # Preços por litro
        preco_etanol = 1.70
        preco_diesel = 2.00

        # Definição de preço e desconto
        if combustivel == "e":
            preco = preco_etanol
            desconto = 0.02 if litros <= 15 else 0.04
        else:
            preco = preco_diesel
            desconto = 0.03 if litros <= 15 else 0.05

        valor_bruto = preco * litros
        valor_desconto = valor_bruto * desconto
        valor_final = valor_bruto - valor_desconto

        print(
            f"Total a pagar: R$ {valor_final:.2f} "
            f"(desconto de {desconto*100:.0f}%)"
        )

    except ValueError:
        print("Por favor, digite apenas números válidos.")


    def ex18(): 
        try:
            nome_empresa = input("Por favor, digite o nome da empresa: ")

            print(f"Bem vindo {nome_empresa}!")

            valor_2022 = float(input("Informe o valor de vendas no ano de 2022: "))
            valor_2023 = float(input("Informe o valor de vendas no ano de 2023: "))

            if valor_2022 == 0:
                print("Não é possível calcular variação com valor inicial igual a 0.")
                return

            # Calular variação percentual
            div1 = valor_2023 - valor_2022
            div2 = div1 / valor_2022
            calculo = div2 * 100
            
            if calculo > 20:
                print(f"Parabens pelo aumento de {int(calculo)}%! Vocês irão ser parabenlizados com uma bonificação.")
            elif calculo > 2 and calculo <= 20:
                print(f"Parabens pelo aumento de {int(calculo)}%! Vocês irão ser parabenlizados com uma pequena bonificação.")
            elif -10 <= calculo <= 2:
                print(f"Poxa, tiveram uma variação de {int(calculo)}%! Vocês irão ter um planejamento de políticas de incentivo às vendas.")
            else:
                print(f"O resultado de vocês foi bem negativo, e por isso, tera corte de gastos!")
        except ValueError:
            print("Por favor, informe o valor com numeros (ex: 65.232).")


# Novos exercicios
# Para tratar uma quantidade de 15 dados de avaliações de pessoas usuárias de
#  um serviço da empresa, precisamos verificar se as notas são válidas. Então, 
# escreva um programa que vai receber a nota de 0 a 5 de todos os dados e 
# verificar se é um valor válido. Caso seja inserido uma nota acima de 5 
# ou abaixo de 0, repita até que a pessoa usuária insira um valor válido.

from pprint import pprint

def ex20():
    notas = {}
    usuario = 1
    soma = 0

    while usuario <= 15:
        try:
            nota = int(input(f"Olá usuario {usuario}, digite sua nota: "))

            if 0 <= nota <= 5:
                notas[f"Usuario {usuario}"] = nota
                soma += nota
                usuario += 1
            else:
                print("Digite uma nota entre 0 e 5.")

        except ValueError:
            print("Por favor, digite um número inteiro válido.")

    media = soma / len(notas)

    contador = 0
    for chave in sorted(notas, key=lambda x: int(x.split()[1])):
        print(f"{chave}: {notas[chave]}", end=" | ")
        contador += 1
        if contador % 4 == 0:
            print()

    print(f"\nA média total das notas foi: {media:.2f}")

ex20()
