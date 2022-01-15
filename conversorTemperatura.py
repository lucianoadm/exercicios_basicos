# Escreva um programa que converta uma temperatura
# digitada em °C em °F. A fórmula para essa conversão é:
#  f = (9 * C / 5) + 32
temperatura_c = float(input('Digite a temperatura atual: '))
f = (9 * temperatura_c / 5) + 32
print(f'Temeperatura atual em Fº: {f}')
