#Python Exercise 70: Create a program that reads the name and price of several products. The program should ask whether the user will continue or not.
continuous = ''
price = purchase = count = 0
lower = None
lower_product = ''
while True:
    product = str(input('Nome do Produto: '))
    price = float(input('Preço do Produto: R$ '))
    purchase += price

    if price > 100:
        count += 1
    if lower is None or price < lower:
        lower = price
        lower_product = product
    continuos = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if continuos == 'N':
        break

print(f'O total da compra foi R${purchase} \n Temos {count} produto(s) valendo mais de R$ 1000.00 \n O produto mais barato foi o {lower_product} com R$ {lower}')    