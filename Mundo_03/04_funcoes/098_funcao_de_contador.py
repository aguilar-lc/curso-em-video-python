
#Exercicio_098 - Faça um programa que tenha uma função chamada contador(), que receba três parâmetros:
#início, fim e passo e realiza a contagem.
#Seu programa tem que realizar três contagens através da função criada:
#a) De 1 até 10, de 1 em 1
#b) De 10 até 1, de 2 em 2
#c) Uma contagem personalizada


from time import sleep
def contador(num1,num2,num3):
    for i in range(num1,num2,num3):
        print(i,end=' ')
        sleep(0.6)
    print('FIM!')
    print('-='*20)
print('-='*20)
print('Contagem de 1 até 10 de 1 em 1:')
contador(1,11,1)
print('Contagem de 10 até 0 de 2 em 2:')
contador (10,1,-2)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
print('-='*20)
print(f'Contagem de {inicio} até {fim} de {passo} em {passo}:')
contador(inicio, fim, passo)