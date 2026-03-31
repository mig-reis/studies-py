def menu():
    print('-' * 17)
    print('Exercicios Alura')
    print('-' * 17)


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
    
def exercicio_7(): 
    #Utilize um loop for para calcular a soma dos números ímpares de 1 a 10. 
    
def exercicio_8(): 
    #Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.
    
def exercicio_9(): 
    #Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse     número, indo de 1 a 10. 
    
def exercicio_10(): 
    #Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções. 

def exercicio_11():
    #Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.


def main():
    menu()
    #exercicio_1()
    #exercicio_2()
    #exercicio_3()
    #exercicio_4()
    #exercicio_5()

if __name__ == '__main__':
    main()