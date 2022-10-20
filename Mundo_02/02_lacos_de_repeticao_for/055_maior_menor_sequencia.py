
#Exercicio_055 - Faça um programa que leia o peso de 5 pessoas e mostre no final qual o foi o peso maior e menor.


maior = 0
menor = 0
for pessoa in range(1,6):
    peso = float(input(f'Qual o peso da {pessoa}ª pessoa? '))
    if pessoa == 1: #Quando se trata do peso a primeira pessoa, ele vai ser ao mesmo tempo o menor e maior
        maior = peso
        menor = peso
    else:
        if peso > maior: #se o peso for o maior numero que eu tenho
            maior = peso
        if peso < menor: #se o peso for o menor numero que qu tenho
            menor = peso
print(f'O maior peso lido foi de {maior}Kg')
print(f'O menor peso lido foi de {menor}Kg')   