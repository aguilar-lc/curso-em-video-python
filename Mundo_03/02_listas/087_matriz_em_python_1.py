
#Exercicio_087 - Aprimore o desafio anterior, mostrando no final:
#a) A soma de todos os valores pares digitados.
#b) A soma dos valores da terceira coluna
#c) O maior valor da segunda linha


matrix = [0,0,0], [0,0,0], [0,0,0]
spar = mai = scol = 0
for l in range(0,3):
    for c in range(0,3):
        matrix[l][c] = int(input(f'Digite um valor para [{l},{c}]: '))
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matrix[l][c]:^5}]', end='')
        if matrix[l][c] % 2 == 0:
            spar = spar + matrix[l][c]
    print()
print(f'A soma dos valores pares é {spar}.')
for l in range(0,3):
    scol = scol + matrix[l][2]
print(f'A soma dos valores da terceira coluna é {scol}.')
for c in range(0,3):
    if c == 0:
        mai = matrix [1][c]
    elif matrix[1][c] > mai:
        mai = matrix[1][c]
print(f'O maior valor da segunda linha é {mai}.')