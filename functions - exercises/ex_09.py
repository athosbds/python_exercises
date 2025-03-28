#Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)

def readInt(message):

    while True:
        number = str(input(message))
        if number.isnumeric():
            return number
        else:
            print('Erro!')
   
n = readInt('Número: ')
print(f'Você acabou de digitar o número {n}')