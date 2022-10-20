
#Exercicio_073 - Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro
#de Futebol, na ordem da colocação. Depois mostre:
#a) Apenas os 5 primeiros colocados.
#b) Os últimos 4 colocados da tabela
#c) Uma lista com os times em ordem alfabética
#d) Em que posição na tabela está o time da Chapecoense.


times = ('Atletico-MG', 'Palmeiras', 'Corinthians', 'Internacional',
        'Fluminense', 'Atlhetico-PR','Flamengo', 'Bragantino',
        'São Paulo','Santos', 'Botafogo', 'Avaí', 'Goiás',
        'Ceará','Cuiabá','Coritiba', 'América-MG', 'Atletico-GO',
        'Fortaleza','Chapecoense')
print('-='*19)
print(f'Lista de Times do Brasileirão: {times}')
print('-='*19)
print(f'Os 5 primeiros são: {times[:5]}')
print('-='*19)
print(f'Os 4 últimos são: {times[-4:]}')
print('-='*19)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-='*19)
print(f'O Chapecoense está na {times.index("Chapecoense")+1}ª posição')