from colorama import Fore
import os

restaurantes = ['Pizza', 'Cebola', 'Tomate']

def nome_programa():
    print(Fore.BLUE + '\n𝕊𝕒𝕓𝕠𝕣 𝔼𝕩𝕡𝕣𝕖𝕤𝕤\n')


def menu():
    print(Fore.WHITE +'1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Ativar Restaurante')
    print('4. Sair\n')

def cadastrar_novo_restaurante():
    os.system('cls')
    print('Cadastro de novos restaurantes\n')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    restaurantes.append(nome_do_restaurante)
    print(f'O restaurante: {nome_do_restaurante} foi cadastrado com sucesso!')
    input('Digite uma tecla para voltar para o menu principal: ')
    main()


def listar_restaurantes():
    os.system('cls')
    print('Listando restaurantes\n')
    for restaurante in restaurantes:
        print(f'- {restaurante}')


def escolha():
    try:
        opcao_escolhida = int(input(Fore.BLACK + 'Escolha uma opção: '))
    except ValueError:
        print(Fore.RED + 'Por favor, digite somente NUMEROS INTEIROS!')


    print(Fore.WHITE + f'Você escolheu a opção {opcao_escolhida}')


    if opcao_escolhida == 1:
        print(Fore.CYAN + '\nCadastrar Restaurante', Fore.WHITE + '')
        cadastrar_novo_restaurante() 
    elif opcao_escolhida == 2:
        print(Fore.CYAN + '\nListar Restaurante', Fore.WHITE + '')
        listar_restaurantes()
    elif opcao_escolhida == 3:
        print(Fore.CYAN + '\nAtivar Restaurante', Fore.WHITE + '')
    elif opcao_escolhida == 4:
        fechar_programa()


def fechar_programa():
    os.system('cls') # Para limpar a tela e fechar o app no Windows
    print(Fore.RED + '\nFechando o programa...', Fore.WHITE + '\n')


def main():
    nome_programa()
    menu()
    escolha()


if __name__ == '__main__':
    main()


print(Fore.WHITE + '')