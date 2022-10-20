
# Exercicio_081 - Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
#A) Quantos números foram digitados
#B) A lista de valores, ordenada de forma decrescente
#C) Se o valor 5 foi digitado e está ou não na lista

num = []
while True:
    num.append(int(input('Digite um valor: ')))
    r = str(input('Quer continuar? [S/N] ')).upper() 
    while r not in 'SsNn':
        r = str(input('Quer continuar? [S/N] ')).upper()
    if r in 'Nn':
        break
print('-=' * 30)
print(f'Você digitou {len(num)} elementos.')
num.sort(reverse = True)
print(f'Os valores em ordem decrescente são {num}')
if 5 in num:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')