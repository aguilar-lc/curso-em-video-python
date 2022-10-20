
#Exercicio_044 - Elabore um programa que cálcule o valor a ser pago por um produto,
#considerando seu preço normal e condição de pagamento.
# À vista dinheiro/cheque: 10% de desconto
# À vista no cartão: 5% de desconto
# Em até 2x no cartão:: 20% de juros


preco = float(input('Digite o preço do produto: R$'))
print('''Escolha a a opção de pagamento:
[1] dinheiro_cheque
[2] cartao
[3] dividido''')
opcao = int(input('Digite sua opcao: '))

if opcao == 1:
    print(f'Pagando em dinheiro ou cheque você tem um desconto de 10% e pagará R${preco - (preco/100 * 10):.2f}.')
elif opcao == 2:
    print(f'Pagando no cartão você tem um desconto de 5% e pagará R${preco - (preco/100 * 5):.2f}.')
elif opcao == 3:
    print(f'Pagando em até 2x no cartão, o juros é de 20% e você pagará R${preco + (preco/100 * 20):.2f}.')