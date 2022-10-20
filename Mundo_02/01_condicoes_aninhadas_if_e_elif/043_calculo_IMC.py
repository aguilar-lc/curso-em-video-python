
#Exercicio_043 - Desenvolva uma lógica que leia o peso e altura de uma pessoa,
#calcula seu IMC e mostre seu status de acordo com a tabela abaixo:
#Abaixo de 18.5: Abaixo do peso
#Entre 18.5 e 25: Peso ideal
#25 até 30: Sobrepeso
#30 até 40: Obesidade mórbida


peso = float(input('Digite o peso: (Kg) '))
altura = float(input('Digite a altura: '))
imc = peso / (altura**2)
if imc < 18.5:
    print(f'Seu IMC é {imc:.2f}, você está abaixo do peso.')
elif imc > 18.5 and imc <= 25:
    print(f'Seu IMC é {imc:.2f}, você está no peso ideal.')
elif imc > 25 and imc <= 30:
    print(f'Seu IMC é {imc:.2f}, você está com sobrepeso.')
elif imc > 30 and imc <= 40:
    print(f'Seu IMC é {imc:.2f}, você está com obesidade mórbida.')