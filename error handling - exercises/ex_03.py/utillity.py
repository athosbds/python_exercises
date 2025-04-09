def menu():
    while True:
        print(f'{"\nMENU PRINCIPAL":>40}')
        print("""
            1 - Ver pessoas Cadastradas
            2 - Cadastrar Nova Pessoa
            3 - Sair do Programa""")
        
        try:
            choice = int(input('\nSua Escolha: '))
            if choice == 1:
                print(f'{"OPÇÃO 1":>40}')
            elif choice == 2:
                print(f'{"OPÇÃO":>40}')
            elif choice == 3:
                print('Saindo do programa...')
            else:
                print('Opção Inválida.')
        except ValueError:
            print('ERRO! OPÇÃO INVÁLIDA.')
