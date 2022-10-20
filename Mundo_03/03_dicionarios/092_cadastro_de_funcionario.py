
#Exercicio_092 - Crie um programa que leia nome, ano de nascimento e carteira de trabalho e
#cadastre-os(com idade) em um dicionário. Se por acaso a CTPS for diferente de zero, o dicionário
#receberá também o ano de contratação e o salário.
#Cálcule e acrescente, além da idade com quantos anos a pessoa vai se aposentar.


from datetime import date
data_hoje = date.today()
ano_atual = data_hoje.year
anosaposenta = 35
dados = {'nome' : str(input('Nome: ')),
         'ano de nascimento' : int(input('Ano de Nascimento: ')),
         'CTPS' : int(input('Carteira de Trabalho (0 não tem): '))}
idade = ano_atual - dados['ano de nascimento']
if dados['CTPS'] != 0:
    ano_contratacao = int(input('Ano de Contratação: '))
    salario = float(input('Salário: '))
    dados ['contratação'] = ano_contratacao
    dados ['salario'] = salario
    dados ['aposentadoria'] = (ano_contratacao + anosaposenta)-dados['ano de nascimento']
    dados ['idade'] = idade
print('='*30)
del dados['ano de nascimento']
for k,v in dados.items():
    print(f'- {k} tem o valor {v}')