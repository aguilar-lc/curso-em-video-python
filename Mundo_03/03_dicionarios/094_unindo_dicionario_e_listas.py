
#Exercicio_094 - Crie um programa que leia nome, sexo e idade de várias pessoas,
#guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
#a)Quantas pessoas foram cadastradas
#b)A média de idade do grupo
#c)Uma lista com todos as mulheres
#d)Uma lista com todas as pessoas com idade acima da média.


pessoa = dict()
lista = list()
soma = 0
while True:
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo [F/M]: ')).upper()
    if pessoa['sexo'] not in 'MmFf':
        print('Por favor, digite apenas M ou F')
        sexo = str(input('Sexo [F/M]: '))
    pessoa['idade'] = int(input('Idade: '))
    r = str(input('Quer continuar? [S/N]? ')).upper()
    lista.append(pessoa.copy())
    soma = soma + pessoa['idade']
    media = soma/len(lista)
    if r not in 'SsNn':
        print('ERRO! Responda apenas S ou N.')
        r = str(input('Quer continuar? [S/N]? ')).upper()
    if r == 'N':
        break
print('-='*20)
print(f'A) Ao todo temos {len(lista)} pessoas cadastradas.')
print(f'B) A média de idade do grupo é de {media:.2f} anos.')
print(f'C) As mulheres cadastradas foram', end=' ')
for p in lista:
    if p['sexo'] == 'F':
        print(p['nome'], end=' ')
print()
print('Lista das pessoas que estão acima da média:')
for p in lista:
    if p['idade'] >= media:
        print(f'nome = {p["nome"]}; sexo = {p["sexo"]}; idade = {p["idade"]};')