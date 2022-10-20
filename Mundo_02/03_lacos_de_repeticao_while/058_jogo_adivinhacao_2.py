
#Exercicio_058 - Melhore o jogo do desafio 28 onde o computador vai "pensar" em um número de 0 a 10.
#Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites
#foram necessários para vencer.


from random import randint
c = 1
computador = randint(0,10)
print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
jogador = int(input('Qual seu palpite? '))
while jogador != computador:
    if jogador < computador:
        print('Mais... Tente mais uma vez.')
    elif jogador > computador:
        print('Menos... Tente mais uma vez.')
    jogador = int(input('Qual seu palpite? '))
    c = c + 1
print(f'Acertou com {c} tentativa(s). Parabéns!.')