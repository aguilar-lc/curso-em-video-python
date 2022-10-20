
#Exercicio_045 - Crie um programa que faça o computador jogar Jokepô com você.


from random import choice
from time import sleep
lista = ['PEDRA','PAPEL','TESOURA']
computador = choice(lista)
print('-=-'* 15)
print("""Suas Opções:
[1] = PEDRA
[2] = PAPEL
[3] = TESOURA""")
jogador = int(input('Qual sua escolha? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=-'* 15)
if jogador == 1 and computador == 'PEDRA':
    print('Eu escolhi pedra e você também, empatamos! Vamos tentar de novo!')
elif jogador == 1 and computador == 'PAPEL':
    print('Eu escolhi papel e você pedra, ganhei!')
elif jogador == 1 and computador == 'TESOURA':
    print('Eu escolhi tesoura e você pedra, você ganhou!')

elif jogador == 2 and computador == 'PEDRA':
    print('Eu escolhi pedra e você papel, Você ganhou!')
elif jogador == 2 and computador == 'PAPEL':
    print('Eu escolhi papel e você também, empatamos! Vamos tentar de novo!')
elif jogador == 2 and computador == 'TESOURA':
    print('Eu escolhi tesoura e você papel, ganhei!')

elif jogador == 3 and computador == 'PEDRA':
    print('Eu escolhi pedra e você tesoura, ganhei!')
elif jogador == 3 and computador == 'PAPEL':
    print('Eu escolhi papel e você tesoura, você ganhou!')  
elif jogador == 3 and computador == 'TESOURA':
    print('Eu escolhi tesoura e você também, empatamos! Vamos tentar de novo!')

else:
    print('Opçao inválida, tente outra vez.')