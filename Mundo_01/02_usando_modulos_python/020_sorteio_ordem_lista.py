
#Exercicio_020 - O mesmo professor do desafio anterior quer sortear a ordem da apresentação e trabalho dos alunos.
#Faça um programa que leia o nome os quatro alunos e mostre a ordem sorteada.


import random
primeiro = input('Primeiro aluno: ')
segundo = input('Segundo aluno: ')
terceiro = input('Terceiro aluno: ')
quarto = input('Quarto aluno: ')
list = [primeiro, segundo, terceiro, quarto]
random.shuffle(list)
print('Ordem de apresentação:')
print(list)