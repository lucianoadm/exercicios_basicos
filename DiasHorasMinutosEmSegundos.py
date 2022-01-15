# escreva um programa que leia a quantidade de dias, horas,
# minutos e segundos do usuário. Calcule o total em segundos

dias = int(input('Dias: '))
horas = int(input('Horas: '))
minutos = int(input('Minutos: '))
segundos = int(input('segundos: '))

# 1 minuto = 60 segundos
# 1 hora = 3600 segundos
# 1 dia = 24 * 3600 segundos

diasseg = dias * 24 * 3600
horasseg = horas * 3600
minutosseg = minutos * 60
totalseg = diasseg + horasseg + minutosseg +  segundos
print(f'Total segundos.....: {totalseg}')

