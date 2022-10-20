
#Exercicio_041 - A confederação nacional de natação precisa de um programa que leia o ano de nascimento
#de um atleta e mostre sua categoria, de acordo com a idade:
# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JUNIOR
# Até 20 anos: SÊNIOR
# Acima: MASTER


from datetime import date
ano_atual = date.today().year
ano_nasc = int(input('Ano nascimento: '))
idade = ano_atual - ano_nasc

if idade <= 9:
    print(f'Você tem {idade} anos e sua Categoria é MIRIM.')
elif idade <= 14:
    print(f'Você tem {idade} anos e sua Categoria é INFANTIL.')
elif idade <= 19:
    print(f'Você tem {idade} anos e sua Categoria é JUNIOR.')
elif idade <=20:
    print(f'Você tem {idade} anos e sua Categoria é SÊNIOR.')
else:
    print(f'Você tem {idade} anos e sua Categoria é MASTER.')