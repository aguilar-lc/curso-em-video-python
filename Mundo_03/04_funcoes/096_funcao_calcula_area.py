
#Exercicio_096 - Faça um programa que tenha uma função chamada área(), que receba as dimensões de
#um terreno retangular (largura e comprimento) e mostre a área do terreno.

def area(larg,comp):
    a = larg * comp
    print(f'A área do terreno {larg}x{comp} é de {a}m²')
print('Controle de Terrenos')
print('-'*20)
largura = float(input('LARGURA(m): '))
comprimento = float(input('COMPRIMENTO(m): '))
area(largura, comprimento)