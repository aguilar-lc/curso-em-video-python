
#Exercicio_019 - Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que o ajude lendo o nome deles e escrevendo o nome do escolhido.


import random
primeiro = input('Primeiro aluno: ')
segundo = input('Segundo aluno: ')
terceiro = input('Terceiro aluno: ')
quarto = input('Quarto aluno: ')
list = [primeiro, segundo, terceiro, quarto]
escolhido = random.choice(list)
print(f'O aluno escolhido foi {escolhido}.')