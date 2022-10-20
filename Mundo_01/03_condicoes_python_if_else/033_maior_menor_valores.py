
#Exercicio_033 - Faça um programa que leia trê números e mostre qual é o maior e qual é o menor.


num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))
num3 = int(input('Terceiro número: '))
lista = [num1, num2, num3]
print(f'O menor valor digitado foi {min(lista)}.')
print(f'O maior valor digitado foi {max(lista)}.')