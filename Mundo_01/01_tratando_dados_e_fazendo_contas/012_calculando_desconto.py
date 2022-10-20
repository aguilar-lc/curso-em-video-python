
#Exercicio_012 - Faça um algoritmo que leia o preço de um produto e mostre seu novo
#preço com 5% de desconto.


preco1 = float(input('Digite o preço do produto: R$'))
preco2 = preco1 - (preco1 * 5 / 100)
print(f'O produto custava R${preco1:.2f}, na promoção com desconto de 5% vai custar R${preco2:.2f}.')