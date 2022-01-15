# Escreva um programa que calcule o tempo de uma viagem de carro.
# Pergunte a distância a percorrer e a velocidade média esperada para a viagem.


distancia = float(input('Digite a distância: '))
vm = float(input('Digite a velocidade média: '))
tempo = distancia / vm  # calculando o tempo total da viagem
horas = (tempo * 3600) // 3600  # convertendo o tempo total em horas inteiras
restohoras = str(round(tempo, 2))  # coletando o resto das horas
minutos = int(restohoras[2::])  #  transformando o resto das horas em minutos
if minutos > 60:
    horas += 1
    minutos = minutos - 60
print(f'tempo de viagem: {horas} horas e {minutos} minutos.')

