# Escreva um programa que pergunte a quantidade de km
# percorridos por um carro alugado pelo usuário, assim
# como a quantidade de dias pelos quais o carro foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$ 60
# por dia e R$ 0,15 por km rodado.

percorrido = float(input('Digite a quantidade de Km percorrido: '))
qtd_dias = int(input('Digite a quantidade de dias de aluguel: '))
custoaluguel = 60
custo_km = 0.15
total_aluguel = custoaluguel * qtd_dias
total_km = percorrido * custo_km

print(f'Custo com Km..............: {total_km}')
print(f'Custo aluguel do carro....: {total_aluguel}')
print(f'Total gasto...............: {total_aluguel + total_km}')
