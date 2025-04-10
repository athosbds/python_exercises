def menu():
    while True:
        print(f'{"\nMENU PRINCIPAL":>40}')
        print("""
            1 - Ver pessoas Cadastradas
            2 - Cadastrar Nova Pessoa
            3 - Sair do Programa
            4 - Limpar Cadastro""")
        
        try:
            choice = int(input('\nSua Escolha: '))
            if choice == 1:
                print(f'{"OPÇÃO 1":>40}')
                try:
                    with open('people.txt', 'r') as arq:
                        content = arq.read()
                    if content.strip() == '':
                        print('Nenhuma Pessoa Cadastrada ainda.')
                    else:
                        print(content)
                except FileNotFoundError:
                    print('Não Encontrado')
            elif choice == 2:
                name = input('Nome da Pessoa: ')
                print(f'{"OPÇÃO 2":>40}')
                with open('people.txt', 'a') as arq:
                    arq.write(name + '\n')
                print(f'{name} cadastrado(a) com sucesso!')
            elif choice == 3:
                print('SAINDO DO PROGRAMA...')
                break
            elif choice == 4:
                print(f'{"OPÇÃO 4":>40}')
                with open('people.txt', 'w') as arq:
                    arq.write('')
                print('LIMPO COM SUCESSO.')
            else:
                print('Opção Inválida.')
        except ValueError:
            print('ERRO! OPÇÃO INVÁLIDA.')
