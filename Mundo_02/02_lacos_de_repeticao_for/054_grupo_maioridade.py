
#Exercicio_054 - Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas
#pessoas ainda não atingiram a maioridade e quantos já são maiores.(considere 21 anos a maioridade)


from datetime import date
anoatual = date.today().year
menor = 0
maior = 0
for i in range(1,8):
    nascimento = int(input(f'Em que ano a {i}ª pessoa nasceu? '))
    idade = anoatual - nascimento
    if idade <= 21:
        menor = menor + 1
    else:
        maior = maior + 1
print(f'Ao todo tivemos {maior} pessoas maiores de idade e {menor} pessoas menores de idade.')