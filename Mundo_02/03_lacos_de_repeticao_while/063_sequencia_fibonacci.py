
#Exercicio_063 - Escreva um programa que leia um numero n inteiro qualquer e mostre na tela os n
#primeiros elementos de uma sequência Fibonacci.



n1 = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print(f'{t1} -> {t2}', end='')
cont = 3
while cont <= n1:
    t3 = t1 + t2
    print(f' -> {t3}', end='')
    t1 = t2
    t2 = t3
    cont = cont + 1
print('-> Fim')