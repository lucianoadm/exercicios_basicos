# Faça um programa que solicite o preço de uma mercadoria e o percentual
# de desconto. Exiba o valor do desconto e o preço a pagar.
preco = float(input('Digite o valor do produto: '))
desconto = float(input('Digite o valor do desconto: '))
descontor = preco * (0.01 * desconto)
print(f'Valor do desconto....: {descontor}')
print(f'Preço com desconto...: {preco-descontor}')
