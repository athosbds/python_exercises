#Python Exercise 57: Write a program that reads a person's gender, but only accepts the values ​​'M' or 'F'. If you are wrong, ask for it to be entered again until you have the correct value.

genre = str(input('Informe seu Sexo [M/F]: ')).upper()

while genre not in 'F' and 'M':
    invalid = str(input('Inválido [M/F]: ')).upper
else:
    print('Registrado!')