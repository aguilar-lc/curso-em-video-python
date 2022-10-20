
#Exercicio_070 - Crie um programa que simule o funcionamento de um caixa eletrônico.
#No início, pergunte ao usuário qual será o valor sacado(número inteiro) e o programa vai informar
#quantas cédulas de cada valor serão entregues.
#Obs: Considere que o caixa possui R$50,00 R$20, R$10,00 e R$1,00


print('='*39)
print('-----BEM VINDO AO CAIXA ELETRÔNICO-----')
print('='*39)
valor = int(input('Que valor você quer sacar? R$ ')) 
total = valor 
cedula = 50  
totcedula = 0 
while True:
    if total >= cedula: 
        total = total - cedula 
        totcedula = totcedula + 1 
    else: 
        if totcedula > 0:
            print(f'Total de {totcedula} cédulas de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totcedula = 0
        if total == 0:
            break
print('='*39)
print('Volte sempre!')