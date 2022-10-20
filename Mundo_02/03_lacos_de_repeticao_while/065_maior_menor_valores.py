
#Exercicio_065 - Crie um programa que leia vários números inteiros pelo teclado.
#No final da execução mostre a média entre todos os valores e qual foi o maior e o menor valor lido.
#O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.


num = 0
r = 'S'
cont = soma = maior = menor = 0
while r == 'S':
    num = int(input('Digite um número: '))
    r = str(input('Deseja continuar? [S/N] ')).upper()
    cont = cont + 1
    soma = soma + num
    if cont == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
print(f'A média entre os valores é de {soma/cont:.2f}.')
print(f'O maior valor foi {maior} e o menor valor foi {menor}.')