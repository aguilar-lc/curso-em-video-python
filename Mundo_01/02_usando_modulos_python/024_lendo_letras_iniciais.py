
#Exercicio_024 - Crie um programa que leia o nome de uma cidade e diga se ele começa ou não com o nome "SANTO".


cidade = str(input('Em que cidade voce nasceu? ')).strip()
print(f'O nome da cidade se inicia pela palavra Santo? {(cidade[:5].upper() == "SANTO")}')