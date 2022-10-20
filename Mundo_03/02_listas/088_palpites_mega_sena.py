
#Exercicio_088 - Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
#O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
#cadastrando tudo em uma lista composta.


import random
print('-' * 30)
print(f"{'     JOGO NA MEGA SENA'     }")
print('-' * 30)
num = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'=-=-= SORTEANDO {num} JOGOS =-=-=')
for c in range(1,num+1):
    lista = random.sample(range(1,25),15)
    print(f'Jogo {c}: {sorted(lista)}')
print(f'=-=-= < BOA SORTE! > =-=-=')