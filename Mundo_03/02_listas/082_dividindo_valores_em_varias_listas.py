
#Exercicio_082 - Crie um programa que vai ler vários números e colocar em uma lista.
#Depois disso, crie duas listas extras que vão contar apenas os valores pares e os ímpares digitados,
#respectivamente. No final, mostre o conteúdo das três listas geradas


lista = []
par = []
impar = []
while True:
    n = int(input('Digite um número: '))
    r = str(input('Quer continuar? [S/N] ')).upper() . strip()
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    lista.append(n)
    while r not in 'SsNn':
        r = str(input('Quer continuar? [S/N]: '))
    if r in 'Nn':
        break
print(f'A lista completa é {lista}')
print(f'A lista de pares é {par}')
print(f'A lista de ímpares é {impar}')