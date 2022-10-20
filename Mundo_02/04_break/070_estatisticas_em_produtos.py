
#Exercicio_070 - Crie um programa que leia o nome e o preço de vários produtos.
#O programa deverá perguntar se o usuário vai continuar. No final, mostre:
#a) Qual é o total gasto na compra
#b) Quantos produtos custam mais de R$ 1000,00
#c) Qual é o nome do produto mais barato.


soma = maisdemil = menor = cont = 0
barato = ' '
while True:
    produto = str(input('Nome do produto: ')).strip()
    preco = float(input('Preço: R$'))
    cont += 1
    if preco > 1000:
        maisdemil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    r = ' '
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N] ')).upper() .strip()
    soma = soma + preco
    if r == 'N':
        break
print(f'O total da compra foi R${soma:.2f}')
print(f'Temos {maisdemil} produtos custando mais de R$1000,00')
print(f'O produto mais barato foi {produto} que custa R${menor:.2f}')