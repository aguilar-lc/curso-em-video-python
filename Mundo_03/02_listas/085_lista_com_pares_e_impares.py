
#Exercicio_085 - Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os
#em uma lista única #que mantenha separados os valores pares e ímpares.
#No final, mostre os valores pares e ímpares em ordem crescente.

lista = []
par = []
impar = []
for c in range(1,8):
    num = int(input(f'Digite o {c}º Valor: '))
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
lista.append(par)
lista.append(impar)
print('-='*25)
print(f'Os valores pares digitados foram {sorted(lista[0])}')
print(f'Os valores ímpares digitados foram {sorted(lista[1])}')