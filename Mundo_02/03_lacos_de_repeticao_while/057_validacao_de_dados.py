
#Exercicio_057 - Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
#Caso esteja errado peça a digitação novamente até ter o valor correto.


sexo = (str(input('Digite seu sexo [F/M]: '))).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe o sexo: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso.')