
#Exercicio_010 - Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e 
# mostra quantos Dólares ela pode comprar. #considere US$00 = R$4,91


real = float(input('Quanto dinheiro você tem na carteira? R$ '))
dolar = real/4.91
print(f'Com R${real:.2f} você pode compar US${dolar:.2f}')