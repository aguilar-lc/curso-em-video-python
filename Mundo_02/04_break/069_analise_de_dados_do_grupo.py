
#Exercicio_069 - Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
#o programa deverá perguntar se o usuário quer ou não continuar.
#No final, mostre:
#a) A quantidade de pessoas que tem mais de 18 anos
#b) Quantos homens foram cadastrados
#c) Quantas mulheres tem menos de 20 anos.


maior = masculino = feminino = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip() .upper()[0]
    if idade > 18:
        maior += 1
    if sexo == 'M':
        masculino += 1  
    elif sexo == 'F' and idade < 20:
        feminino += 1
    r = ' '
    while r not in 'SN':
        r = str(input('Quer continuar? ')).strip() .upper()[0]
    if r == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {maior}')
print(f'Ao todo temos {masculino} homens cadastrados')
print(f'E temos {feminino} mulheres com menos de 20 anos')