
#Exercicio_097 - Faça um programa que tenha uma função chamada escreva(), que receba um texto como parâmetro
#e mostre uma mensagem com tamanho adaptável.

def escreva(texto):
    tam = len(texto) + 4
    print('^'* tam)
    print(f'  {texto}')
    print('^'* tam)
escreva('Lilian Candido')
escreva('Aprendendo Python')
