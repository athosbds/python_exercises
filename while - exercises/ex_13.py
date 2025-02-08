#Python Exercise 69: Create a program that reads the age and gender of several people. For each registered person, the program must ask whether or not the user wishes to continue. At the end, show:
# A) how many people are over 18 years old./ B) how many men were registered./C) how many women are under 20 years old.
print('Cadastre uma pessoa')
age = count = male_gender = female_age = 0
while True:
    age = int(input('Idade: '))
    gender = ' '
    while gender not in 'FM':
        gender = str(input('Sexo: [M/F] ')).strip().upper()

    if age >= 18:
        count += 1
    if gender == 'M':
        male_gender += 1
    if gender == 'F' and age < 20:
        female_age += 1
    continuous = ' '
    while continuous not in 'SN':
        continuous = str(input('Quer Continuar? [S/N]: ')).strip().upper()
    if continuous == 'N':
        break
print('Total de pessoas com mais de 18 anos: {}  \n Total de {} homem cadastrado \n E temos {} mulher(es) com menos de 20 anos. '.format(count, male_gender, female_age))






