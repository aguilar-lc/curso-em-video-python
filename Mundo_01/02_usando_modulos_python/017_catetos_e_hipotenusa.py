
#Exercicio_017 - Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente 
# de um triângulo retângulo, cálcule e mostre o comprimento da hipotenusa.


from math import hypot
cateto_oposto = float(input('Digite o valor do cateto oposto: '))
cateto_adjacente = float(input('Digite o valor do cateto adjacente: '))
hipotenusa = hypot(cateto_oposto, cateto_adjacente)
print(f'O comprimento da hipotenusa é {hipotenusa:.2f}.')