
#Exercicio_048 - Faça um programa que cálcule a soma entre todos os números 
#ímpares que são multiplos de 3 e que se encontram no intervalo de 1 até 500.


soma = 0
cont = 0
for i in range(1,501,2):
    if i % 3 == 0:
        soma = soma + i
        cont = cont + 1
print(f'A soma de todos os {cont} valores solicitados é {soma}.')