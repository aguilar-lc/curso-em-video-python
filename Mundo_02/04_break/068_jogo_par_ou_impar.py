
#Exercicio_068 - Faça um programa que jogue par ou ímpar com o computador.
#O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias
#consecutivas que ele conquistou no final do jogo.


from random import randint
print('=-='*10)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-='*10)
cont = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(1,10)
    soma = jogador + computador
    opcao = ' '
    while opcao not in 'PI':
        opcao = str(input('Par ou Ímpar? [P/I] ')).upper() .strip()
    print(f'Você jogou {jogador} e o computador {computador} -> Total de {soma} -> ', end='')
    print('DEU PAR.'if soma % 2 == 0 else 'DEU ÍMPAR.')
    if opcao == 'P':
        if soma % 2 == 0:
            print('Você GANHOU!')
        else:
            print('Você PERDEU!')
            break
    if opcao == 'I':
        if soma % 2 == 0:
            print('Você PERDEU!')
            break
        else:
            print('Você GANHOU!')
    print('Vamos jogar novamente...') 
    cont = cont +1    
print('=-='*10)
print(f'GAME OVER! Você venceu {cont} vezes.')