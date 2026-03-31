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



def main():
    menu()
    #exercicio_1()
    #exercicio_2()
    #exercicio_3()
    #exercicio_4()


if __name__ == '__main__':
    main()