#Python Exercise 076: Create a program that has a single tuple with product names and their respective prices, in sequence. At the end, show a price list, organizing the data in tabular form.

products = ('Lápis',1.75, 'Borracha', 2.00, 'Caderno', 15.0, 'Estojo', 25.00, 'Transferidor', 4.20)
print('Listagem de Preços')
for position in range(0, len(products)):
    if position % 2 == 0:
        print(f'{products[position]:.<30}', end ='')
    else:
        print(f'R${products[position]:>8}')