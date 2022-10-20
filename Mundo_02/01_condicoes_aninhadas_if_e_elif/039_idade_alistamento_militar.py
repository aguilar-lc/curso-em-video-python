
#Exercicio_039 - Faça um programa que leia o ano de nascimento de um jovem e afirme, de acordo com sua idade:
#Se ele ainda vai se alistar no serviço militar
#Se é a hora de se alistar
#Se já passou do tempo do alistamento.
#Seu programa também terá que mostrar o tempo que falta ou o tempo que passou do prazo.


from datetime import date
data_hoje = date.today()

ano_atual = data_hoje.year
ano_nascimento = int(input('Ano de nascimento: '))
idade = ano_atual - ano_nascimento
print(f'Quem nasceu em {ano_nascimento} tem {idade} anos em {ano_atual}.')

if idade < 18:
    print(f'Ainda faltam {18 - idade} ano(s) para o alistamento.')
    print(f'Seu alistamento será em {ano_nascimento + 18}.')
elif idade == 18:
    print('Está na hora de se alistar no serviço militar!')
elif idade >18:
    print(f'Você deveria ter se alistado há {idade - 18} ano(s)')
    print(f'Seu alistamento deveria ter sido feito em {ano_nascimento + 18}.')