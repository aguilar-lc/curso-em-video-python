
#Exercicio_018 - Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno,
#cosseno e tangente desse ângulo.


import math
angulo = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print(f'O valor de seno é {seno:.2f}, o valor de cosseno é {cosseno:.2f} e o valor da tangente é {tangente:.2f}.')