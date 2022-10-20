
#Exercicio_093 - Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler
#o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida
#No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.


futebol = dict()
lista = list()
total = 0
nome = str(input('Nome do Jogador: '))
partida = int(input(f'Quantas partidas {nome} jogou? '))
for i in range(1,partida+1):
    gol = int(input(f'Quantos gols na {i} partida? '))
    lista.append(gol)
    total = total + gol
print('-='*25)
futebol['nome'] = nome
futebol['gols'] = lista
futebol['total'] = total
print(futebol)
print('-='*25)
for k,v in futebol.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*25)
print(f'O jogador {nome} jogou {partida} partidas.')
for i, v in enumerate(lista):
    print(f'=> Na partida {i}, fez {v} gols.')
print(f'Foi um total de {total} gols.')