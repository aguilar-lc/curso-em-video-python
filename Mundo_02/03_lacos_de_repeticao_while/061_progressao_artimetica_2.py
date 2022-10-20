
#Exercicio_061 - Refaça o exercício 51, lendo o primeiro termo e a razão de uma PA,
#mostrando os 10 primeiros termos da progressão usando a estrutura while.


primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro_termo
cont = 1
while cont <= 10:
    print(termo, end=' -> ')
    termo = termo + razao
    cont = cont + 1
print('Pausa')