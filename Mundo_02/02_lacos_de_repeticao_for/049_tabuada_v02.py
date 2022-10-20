
#Exercicio_049 - Refaça o desafio 09, mostrando a tabuada de um número que o usuário escolher,
# só que agora utilizando o laço FOR.


num = int(input('Digite um número para ver sua tabuada: '))
print('-=' * 6)
for i in range(0,11):
    print(f'{num} x  {i} = {num*1}')
print('-=' * 6)