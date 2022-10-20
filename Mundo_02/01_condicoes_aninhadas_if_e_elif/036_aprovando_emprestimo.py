
#Exercicio_036 - Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
#O programa #vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#Cálcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário
# ou então o empréstimo será negado.


casa = float(input('Valor da casa R$ '))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financeiamento? '))
porcentagem = (salario * (30/100))
prestacao = float(casa / (anos * 12))
if prestacao <= porcentagem:
    print(f'Considerando o comprometimento máximo de 30% do salário, a prestação deve ter o valor até R${porcentagem:.2f}')
    print(f'Com os dados informados a prestação será de R${prestacao:.2f}. O empréstimo foi APROVADO.')
else:
    print(f'Considerando o comprometimento máximo de 30% do salário, a prestação deve ter o valor até R${porcentagem:.2f}')
    print(f'Com os dados informados a prestação será de R${prestacao:.2f}. O empréstimo foi NEGADO.')