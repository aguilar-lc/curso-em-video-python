
#Exercicio_074 - Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
#Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla


from random import sample
num = sample(range(10),5)
print(f'Os valores sorteados foram:', end = ' ')
for i in num:
    print(f'{i} ', end ='')
print(f'\nO maior valor sorteado foi {max(num)}')
print(f'O menor valor sorteado foi {min(num)}')