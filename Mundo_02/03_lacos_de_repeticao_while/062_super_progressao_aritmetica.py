
#Exercicio_062 - Melhore o exercício 61, perguntando para o usuário se ele quer mostrar mais alguns termos
#O programa encerra quando ele disser que quer mostrar zero termos.


primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro_termo
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(termo, end=' -> ')
        termo = termo + razao
        cont = cont + 1
    print('Pausa')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {total} termos')