#Exercício Python 114: Crie um código em Python que teste se o site pudim está acessível pelo computador usado
import requests
link = "https://www.pudim.com.br/"
try:
    answer = requests.get(link)
    print(f'Consegui acessar: {link}')
except:
    print(f'Não consegui acessar: {link}')