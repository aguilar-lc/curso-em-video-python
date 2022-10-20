
#Exercicio_026 - Faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra "A"
#Em que posição ela aparece a primeira vez 
#Em que posição ela aparece a última vez


frase = input(str('Digite uma frase: ')).upper().strip()
print(f'Quantas vezes aparece a letra "A" na frase?: {(frase.count("A"))}')
print(f'Em que posição a letra "A" aparece a primeira vez?: {(frase.find("A"))}')
print(f'Em que posição a letra "A" parece a última vez?: {(frase.rfind("A"))}')