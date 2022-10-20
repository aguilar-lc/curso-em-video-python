#Exercicio_013 - Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário,
#com aumento de 15%.


salario1 = float(input('Qual é o salário do funcionário?: R$'))
salario2 = salario1 + (salario1 * 15 / 100)
print(f'Um funcionário que ganhava R${salario1:.2f}, com aumento de 15% passa a receber R${salario2:.2f}.')