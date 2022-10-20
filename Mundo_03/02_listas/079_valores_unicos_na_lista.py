
#Exercicio_079 - Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os
#em uma lista caso o número já exista la dentro, ele não será adicionado.
#No final, serão exibidos todos os valores únicos digitados em ordem crescente


valores = []
while True:
    num = int(input('Digite um valor: '))
    if num not in valores:
        valores.append(num)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...') 
    r = str(input('Quer continuar? [S/N ] ')).upper() .strip()
    while r not in 'SsNn':
        r = str(input('Quer continuar? [S/N ] ')).upper() .strip()
    if r in 'nN':
        break
print(f'Você digitou os valores {sorted(valores)}')