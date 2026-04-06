import os


def menu():
    print('-' * 17)
    print('Exercicios Alura')
    print('-' * 17)


def fechar_programa():
    os.system('cls') # Para limpar a tela e fechar o app no Windows
    print('Programa finalizado.')


def exercicio_1():
    # 1 - Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.

    print('\nEscolha um numero e iremos informar se o numero é par ou impar.')

    try:
        numero = int(input("Digite o numero: "))
    except ValueError:
        print("Por favor, digite somente numeros inteiros!")

    if numero % 2 == 0:
        print(f'{numero} é par.')
    else:
        print(f'{numero} é impar.')


def exercicio_2():
    # 2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:

    #Criança: 0 a 12 anos; Adolescente: 13 a 18 anos; Adulto: acima de 18 anos.

    try:
        idade = int(input('Digite sua idade: '))
    except ValueError:
        print('Por favor, digite somente numeros inteiros!')
    
    if idade > 0 and idade <= 12:
        print('Você é criança.')
    elif idade >= 13 and idade < 18:
        print('Você é adolescente.')
    elif idade >= 18 and idade < 100:
        print('Você é adulto.')
    else:
        print('Digite uma idade valida!')


def exercicio_3():
    #3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.
    print('Informe seu nome de usuario e senha.')

    nome = input('\nDigite seu nome: ').upper()
    
    try:
        senha = int(input('Digite sua senha (Somente Numeros): '))
    except ValueError:
        print('Por favor, digite somente numeros inteiros!')
    
    if nome.isalpha():
        print('\nRegistro feito!')
    else:
        print('\nDados invalidos!')


def exercicio_4():
    #4 - Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura if elif else para determinar em qual quadrante do plano cartesiano o ponto se encontra de acordo com as seguintes condições:

    #Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
    #Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
    #Terceiro Quadrante: os valores de x e y devem ser menores que zero;
    #Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
    #Caso contrário: o ponto está localizado no eixo ou origem.

    print('\nVamos localizar você no plano cartesiano!')

    try:
        coordenada_x = int(input('Digite o ponto X: '))
        coordenada_y = int(input('Digite o ponto Y: '))
    except ValueError:
        print('Por favor, digite somente numero inteiros!')
    
    if coordenada_x > 0 and coordenada_y > 0:
        print('Você esta no primeiro quadrante!')
    elif coordenada_x < 0 and coordenada_y > 0:
        print('Você esta no segundo quadrante!')
    elif coordenada_x < 0 and coordenada_y < 0:
        print('Você esta no terceiro quadrante!')
    elif coordenada_x > 0 and coordenada_y < 0:
        print('Você esta no quarto quadrante!')
    else:
        print('Você esta no eixo ou na origem!')


def exercicio_5():
    #Crie uma lista para cada informação a seguir: Lista de números de 1 a 10; Lista com quatro nomes; Lista com o ano que você nasceu e o ano atual.
    numeros = []
    quatro_nomes = []
    ano = {}

    contador = 0

    while contador < 10:
        contador += 1
        numeros.append(contador)

    for n in range(1, 5):
        nome = input(f'Digite o {n}° nome: ').upper()
        quatro_nomes.append(nome)
    
    try:
        nascimento = int(input('\nDigite o ano que você nasceu: '))
        ano_atual = int(input('Digite o ano atual: '))

        ano = f'Ano de nascimento: {nascimento}', f'Ano atual: {ano_atual}'
    except ValueError:
        print('Por favor, digite somente numeros! (Ex: 2020)')


    print('\nNumeros de 1 a 10:')
    print(numeros)

    print('\nLista com 4 nomes: ')
    print(quatro_nomes)

    print(f'\n{ano}')


def exercicio_6():
    #Crie uma lista e utilize um loop for para percorrer todos os elementos da lista. 
    
    lista = [10, 20, 30, 40, 50]

    for n in lista:
        print(n)


def exercicio_7(): 
    #Utilize um loop for para calcular a soma dos números ímpares de 1 a 10. 

    inpares = []

    for n in range(0, 10):
        if n % 2 == 0:
            pass
        else:
            inpares.append(n)

        resultado = sum(inpares)

    print(resultado)


def exercicio_8(): 
    #Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.

    for n in range(10, 0, -1):
        print(n)


def exercicio_9(): 
    #Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse     número, indo de 1 a 10. 

    try:
        numero = int(input('Digite um numero: '))
    except ValueError:
        print('Por favor, digite somente numeros inteiros!')
    
    for n in range(1, 11):
        resultado = n * numero
        print(f'{numero} x {n} = {resultado}')


def exercicio_10(): 
    #Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções. 

    lista_numeros = []

    try:
        for n in range(1, 11):
            numero = int(input(f'Digite o {n}° numero: '))
            lista_numeros.append(numero)
    except ValueError:
        print('Por favor, digite somente NUMEROS INTEIROS!')


    print(f'A lista ficou assim: {lista_numeros}')

    soma = sum(lista_numeros)
    print(f'A soma dos numeros é: {soma}')


def exercicio_11():
    #Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.

    lista = []

    try:
        for n in range(1, 5):
            numero = int(input(f'Digite a {n}° nota: '))
            lista.append(numero)
    except ValueError:
        print('Por favor, digite somente numeros inteiros!')

    print(f'As notas são: {lista}')

    try:
        media = sum(lista) / len(lista)
        print(f"Média: {media}")
    except ZeroDivisionError:
        print("Erro: Não é possível calcular a média de uma lista vazia.")

def exercicio_12():
    #1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.
    infos = {'nome': 'nome', 'idade': 'idade', 'cidade': 'cidade'}

    print('\nSeja Bem vindo!')
    print('\nVamos iniciar seu cadastro')


    nome = input('\nDigite o seu nome: ')
    cidade = input('Digite sua cidade: ')

    try:
        idade = int(input('Digite sua idade: '))
    except ValueError:
        print('Digite somente numeros iteiros!')

    infos['nome'] = nome
    infos['idade'] = idade
    infos['cidade'] = cidade

    print('')
    print(f'{'    Nome'.ljust(15)} | {'   Cidade'.ljust(15)} | {' Idade'}')

    print(f'     {nome.ljust(10)} |   {cidade.ljust(13)} |      {idade}')

    #Utilizando o dicionário criado no item 1: Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa); Adicione um campo de profissão para essa pessoa; Remova um item do dicionário.

    print('\nAgora selecione a opção que deseja:')
    print('1. Atualizar Cadastro')
    print('2. Sair')

    try:
        escolha = int(input('Digite aqui (1 para atualizar 2 para sair): '))
    except ValueError:
        print('Por favor, digite somente numeros!')

    if escolha == 1:
        print('Vamos atualizar seu cadastro, por favor responda as perguntas:')

        try:
            idade = int(input('Confirme sua idade: '))
        except ValueError:
            print('Por favor, digite somente numeros!')

        profissão = input('Digite sua profissão: ')

        infos['idade'] = idade
        infos['profissão'] = profissão

        print('')
        print(f'{'    Nome'.ljust(15)} |   {'  Cidade'.ljust(13)} |   {' Profissão'}')

        print(f'     {nome.ljust(10)} |   {cidade.ljust(13)} |      {profissão}')
    elif escolha == 2:
        fechar_programa()


def exercicio_13():
    #Crie um dicionário que relacione os números de 1 a 5 aos seus respectivos quadrados.

    numeros = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

    print('Vamos mostrar os numeros de 1 a 5 e seus respectivos quadrados:')

    for n in numeros:
        print(f'{n} ao quadrado: {numeros[n]}')


def exercicio_14():
    #Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.

    dic = {'Nome': 'Miguel', 'Idade': 17, 'Namorada': 'Leticia' }

    print(dic)

    nome = input('Digite o nome da namorada do Miguel: ')

    if nome == dic['Namorada']:
        print('Nome correto!')
    else:
        print('Essa chave não exsite no dicionario!')


def exercicio_15():
    #Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.


def main():
    menu()
    #exercicio_1()
    #exercicio_2()
    #exercicio_3()
    #exercicio_4()
    #exercicio_5()
    #exercicio_7()
    #exercicio_8()
    #exercicio_9()
    #exercicio_10()
    #exercicio_11()
    #exercicio_12()
    #exercicio_13()
    #exercicio_14()



if __name__ == '__main__':
    main()