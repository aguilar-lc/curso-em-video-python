
#Exercicio_060 - Faça um programa que leia um número qualquer e mostre seu fatorial.


numero = int(input('Digite um número para cálcular o seu fatorial: '))
contador = numero
fatorial = 1
while contador > 0:
    print(f'{contador}', end='')
    print(' x ' if contador > 1 else '= ', end='')
    fatorial = fatorial * contador
    contador = contador - 1
print(f'{fatorial}')