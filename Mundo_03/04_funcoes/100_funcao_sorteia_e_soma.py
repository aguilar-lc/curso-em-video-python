
# Exercicio_100 - Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteio()
#e somaPart(). A primeira função  vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai
#mostrar a soma entre todos os valores PARES sorteados pela função anterior.


import random
from datetime import time
from time import sleep

numeros = []
soma = 0

def sorteio():
    print('Sorteando 5 valores da lista:', end=' ')
    for i in range(0,5):
        sorteio = random.randint(1,10)
        print(sorteio,end=' ')
        sleep(0.5)
        numeros.append(sorteio)
    print('PRONTO!')
sorteio()

def somaPart(soma):
    print(f'Somando os valores pares de {numeros}, temos:', end=' ')
    for i in numeros:
        if i % 2 == 0:
            soma = soma + i
    print(soma)
somaPart(soma)