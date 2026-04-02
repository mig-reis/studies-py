from colorama import Fore
import os

restaurantes = [
                {'nome': 'Pizzaria', 'categoria': 'Italiano', 'ativo': True}, 
                {'nome': 'Sushi', 'categoria': 'Japonesa', 'ativo': False}
                ]

def nome_programa():
    print(Fore.BLUE + '\n𝕊𝕒𝕓𝕠𝕣 𝔼𝕩𝕡𝕣𝕖𝕤𝕤\n')


def menu():
    print(Fore.WHITE +'1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Ativar Restaurante')
    print('4. Sair\n')


def voltar_menu():
    input('\nDigite uma tecla para voltar ao menu principal: ')
    main()


def subtitulo_escolha(escolha):
    os.system('cls')
    print(f'\n{escolha}')


def cadastrar_novo_restaurante():
    os.system('cls')
    subtitulo_escolha('Cadastrar Restaurante\n')

    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria_restaurante = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')

    dados_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria_restaurante, 'ativo': False}
    restaurantes.append(dados_restaurante)

    print(f'O restaurante: {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_menu()


def listar_restaurantes():
    os.system('cls')
    subtitulo_escolha('Listando Restaurantes...\n')

    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        status_ativo = restaurante['ativo']

        print(f'- {nome_restaurante} | {categoria_restaurante} | {status_ativo}')

    voltar_menu()


def alterar_status_restaurante():
    subtitulo_escolha('Alternando status do restaurante...')

    nome_restaurante = input('Digite o nome do restaurante que deseja ativar: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']

            msg = f'O restaurante {nome_restaurante} foi ativado com sucesso!' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso!'

            print(msg)

    if not restaurante_encontrado:
        print('O restaurante não foi encontrado...')

    voltar_menu()


def escolha():
    try:
        opcao_escolhida = int(input(Fore.BLACK + 'Escolha uma opção: '))
    except ValueError:
        print(Fore.RED + 'Por favor, digite somente NUMEROS INTEIROS!')


    print(Fore.WHITE + f'Você escolheu a opção {opcao_escolhida}')


    if opcao_escolhida == 1:
        cadastrar_novo_restaurante() 
    elif opcao_escolhida == 2:
        listar_restaurantes()
    elif opcao_escolhida == 3:
        alterar_status_restaurante()
    elif opcao_escolhida == 4:
        fechar_programa()


def fechar_programa():
    os.system('cls') # Para limpar a tela e fechar o app no Windows
    subtitulo_escolha('Fechando programa...')


def main():
    nome_programa()
    menu()
    escolha()


if __name__ == '__main__':
    main()


print(Fore.WHITE + '')