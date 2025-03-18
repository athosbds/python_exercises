#Exercício Python 097: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.    
def write(message):
    size = len(message) + 4
    print('-' * size)
    print(message)
    print('-' * size)
write('Eu amo Python!')
write('Eu Odeio Java.')