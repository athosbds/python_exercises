#Python Exercise 73: Create a tuple filled with the top 20 placed in the Brazilian Football Championship Table, in order of placement.
print('Campeonato Brasileiro')

brazilian = ('Botafogo', 'Palmeiras', 'Flamengo', 'Fortaleza', 'Internacional', 'São Paulo', 'Corinthians', 'Bahia', 'Cruzeiro', 'Vasco', 'Vitória', 'Atlético-MG', 'Fluminense', 'Grêmio', 'Juventude', 'Bragantino', 'Athletico-PR', 'Criciúma', 'Atlético-GO', 'Cuiabá')

print(f'\n Os cinco primeiros são: \n {brazilian[0:5]}')
print(f'\n Os últimos 4 colocados são: \n {brazilian[16:]}')
print(f'\n Times em Ordem Alfabética: \n {sorted(brazilian)} ')