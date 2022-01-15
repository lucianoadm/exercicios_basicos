# Escreva um programa que leia três números
# e que imprima o maior entre eles

a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))
if (a > b) and (a > c):
    print('maior valor:', a, ' letra a')
elif (b > a) and (b > c):
    print('maior valor:', b, ' letra b')
else:
    print('maior valor:', c, ' letra c')
