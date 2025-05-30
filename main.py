from colorama import Fore, init

init(autoreset=True)  # Reseta a cor automaticamente após cada print

def mostrar_menu():
    print(Fore.CYAN + '-' * 50)
    print(Fore.YELLOW + 'MENU PRINCIPAL'.center(40))
    print(Fore.CYAN + '-' * 50)
    print(Fore.GREEN + '1' + Fore.BLUE + ' - Ver pessoas cadastradas')
    print(Fore.GREEN + '2' + Fore.BLUE + ' - Cadastrar nova pessoa')
    print(Fore.GREEN + '3' + Fore.BLUE + ' - Sair do sistema')
    print(Fore.CYAN + '-' * 50)

def ver_pessoas():
    try:
        with open('pessoas.txt', 'r', encoding='utf-8') as arquivo:
            pessoas = arquivo.readlines()
            if pessoas:
                print(Fore.CYAN + '\n' + '-' * 50)
                print(Fore.YELLOW + 'PESSOAS CADASTRADAS'.center(40))
                print(Fore.CYAN + '-' * 50)
                print(Fore.BLUE + f'{"Nome":<28}{"Idade":>10}')
                print(Fore.CYAN + '-' * 50)
                for pessoa in pessoas:
                    partes = pessoa.strip().split(',')
                    if len(partes) == 2:
                        nome, idade = partes
                        idade = idade.replace(' anos', '')
                        print(Fore.WHITE + f'{nome:<28}{idade:>10} anos')
                    else:
                        print(Fore.RED + 'Linha inválida no arquivo:', pessoa.strip())
                
            else:
                print(Fore.RED + 'Nenhuma pessoa cadastrada ainda.')
    except FileNotFoundError:
        print(Fore.RED + 'Arquivo de cadastro não encontrado. Nenhuma pessoa cadastrada.')

def cadastrar_pessoa():
    nome = input(Fore.WHITE + 'Nome: ').strip()
    idade = input(Fore.WHITE + 'Idade: ').strip()
    try:
        with open('pessoas.txt', 'a', encoding='utf-8') as arquivo:
            arquivo.write(f'{nome}, {idade} anos\n')
        print(Fore.GREEN + f'{nome} foi cadastrado com sucesso!')
    except Exception as e:
        print(Fore.RED + f'Ocorreu um erro ao cadastrar a pessoa: {e}')

def main():
    while True:
        mostrar_menu()
        try:
            opcao = int(input(Fore.YELLOW + 'Sua opção: '))
        except ValueError:
            print(Fore.RED + 'Por favor, digite um número válido.')
            continue

        if opcao == 1:
            ver_pessoas()
        elif opcao == 2:
            cadastrar_pessoa()
        elif opcao == 3:
            print(Fore.MAGENTA + 'Saindo do sistema... Até logo!')
            break
        else:
            print(Fore.RED + 'Opção inválida. Tente novamente.')

if __name__ == '__main__':
    main()
