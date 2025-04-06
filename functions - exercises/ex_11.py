#Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.
def interatictive_help():
    while True:
        print('\033[42m Sistema de Ajuda PyHELP\033[m')
        helped = str(input('Função ou Biblioteca: '))
        if helped != 'fim':
            print(f'\033[44m Acessando o manual do comando ´{helped}´\033[m')
            help(helped)
        else
            print('\033[41Até logo\033[m')
            break
interatictive_help()

