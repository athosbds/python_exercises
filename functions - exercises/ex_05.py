#Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
from random import randint

def sorted(*value):
    memory = []
    value = [randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10)]
    memory.append(value)
    print(f'Sorteando 5 valores da lista: {value}')
    add_up(value)

def add_up(space):
    total = 0
    for number in space:
        if number % 2 == 0:
            total += number
    print(f'Somando os valores pares d temos {total}')

sorted()
