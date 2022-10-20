
#Exercicio_090 - Faça um programa que leia o nome e média de um aluno, guardando também a situação
#em um dicionário no final, mostre o conteúdo da estrutura na tela.


nome = str(input('Nome: '))
media = float(input(f'Média de {nome}: '))
dic = {'nome' : nome, 'média': media}
print(f'- Nome é igual a {dic["nome"]}')
print(f'- Média é igual a {dic["média"]}')
if media >= 7:
    print('- Situação é igual a Aprovado')
elif media < 7:
    print('- Situação é igual a Recuperação')