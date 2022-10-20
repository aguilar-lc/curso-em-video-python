
#Exercicio_022 - Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas;
#O nome com todas as letras minúsculas;
#Quantas letras ao todo (sem considerar os espaços);
#Quantas letras tem o primeiro nome.


nome1 = input(str('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print(f'Seu nome em maiúsculas é {(nome1.upper())}.')
print(f'Seu nome em minúsculas é {(nome1.lower())}.')
print(f'Seu nome ao todo tem {(len(nome1.replace(" ","")))} letras.')
primeiro = nome1.split()
print(f'Seu primeiro nome é {(primeiro[0])} e ele tem {(len(primeiro[0]))} letras.')