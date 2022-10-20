
#Exercicio_016 - Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela 
#a sua porção inteira.

from math import trunc
real = float(input('Digite um número: '))
print(f'O número real {real} tem a parte inteira é {trunc(real)}.')