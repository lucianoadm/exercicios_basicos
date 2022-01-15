# Escreva um programa para calcular a redução do tempo
# de vida de um fumante. Pergunte a quantidade de cigarros
# fumados por dia e quantos anos ele já fumou. Considere que
# ,um fumante perde 10 minutos de vida a cada cigarro,
# e calcule quantos dias de vida um fumante perderá.
# Exiba o total em dias.
cigarros_dia = int(input('Digite a quantidade média de cigarro por dia: '))
tempo_fumando = int(input('Digite o tempo de fumante: '))
total_fumado = cigarros_dia * 365 * tempo_fumando
tempo_perdido_seg = total_fumado * 600
tempo_perdido_hora = tempo_perdido_seg / 3600
tempo_perdido_dia = tempo_perdido_hora / 24
print(f'Total de cigarros fumados:  {total_fumado}')
print(f'Tempo perdido em dias: {round(tempo_perdido_dia,2)} dias.')
print(f'Tempo total de vida perdido: {round(tempo_perdido_hora,2)} horas.')
