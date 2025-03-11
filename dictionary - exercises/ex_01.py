#Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
informations = {}
informations['nome'] = str(input('Digite seu nome: '))
informations['média'] = float(input('Sua média: '))
print(f'Seu nome é {informations["nome"]}')
print(f'Sua média é {informations["média"]}')
if informations['média'] > 7:
    print('Aprovado')
else:
    print('Reprovado.')