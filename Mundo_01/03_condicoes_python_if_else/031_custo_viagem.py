
#Exercicio_031 - Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Cálcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km
# e R$ 0,45 para viagens mais longas.


distancia = float(input('Qual a distândia da sua viagem? '))
preco1 = distancia * 0.50
preco2 = distancia * 0.45
if distancia <= 200:
    print(f'O valor a ser pago pela viagem é R${preco1:.2f}.')
else:
     print(f'O valor a ser pago pela viagem é R${preco2:.2f}.')