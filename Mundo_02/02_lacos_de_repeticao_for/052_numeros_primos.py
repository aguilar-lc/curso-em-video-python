
#Exercicio_052 - Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.


n = int(input(' Digite um número: '))
divisivel = 0
for i in range(1,n + 1):
    if n % i == 0:
        print(end=' ')
        divisivel = divisivel + 1
    else:
        print(end=' ')
    print('{}'.format(i), end=' ')
print('\n O número {} foi dividido {} vezes.'. format(n,divisivel))
if divisivel == 2:
    print(' E por isso ele é primo!')
else:
    print(' E por isso ele não é primo!')