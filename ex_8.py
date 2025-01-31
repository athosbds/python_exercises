#Python Exercise 059: Create a program that reads two values ​​and displays a menu on the screen: [ 1 ] add [ 2 ] multiply [ 3 ] largest [ 4 ] new numbers [ 5 ] exit the program
# Your program must perform the requested operation in each case.

value_one = int(input('Primeiro Valor: '))
value_two = int(input('Segundo Valor: '))
choose = 0
while choose != 5:
    print("""
      [1] Soma
      [2] Multiplicar
      [3] Maior
      [4] Novos Números
      [5] Sair do Programa""")

    choose =int(input('Sua Escolha: '))
    if choose == 1:
        print('Soma dos números {} e {} é = {}'.format(value_one, value_two, value_one + value_two))
    elif choose == 2:
        print('A multiplicação do número {} vezes {} é igual a {}'.format(value_one, value_two, value_one*value_two))
    elif choose == 3:
        if value_one > value_two:
            print('O maior valor é o {}'.format(value_one))
        else:
            print('O maior valor é o {}'.format(value_two))
    elif choose == 4 :
        print('Informe os números novamente')
        value_one = int(input('Primeiro Valor: '))
        value_two = int(input('Segundo Valor: '))
    elif choose == 5:
        print('Finalizado.')
else:
    print('Opção Inválida! Tente Novamente.')
print('Fim do Programa! Volte sempre.')
