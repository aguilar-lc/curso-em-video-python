
#Exercicio_027 - Faça um programa que leia o nome completo de uma pessoa,
#mostrando em seguida o primeiro e o último nome separadamente.


n = input(str('Digite seu nome completo: ')).strip()
print('Pazer em te conhecer!')
n1 = n.split()
print(f'Seu primeiro nome é: {(n1[0])}.')
print(f'Seu último nome é: {n1[-1]}.')