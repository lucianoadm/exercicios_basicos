# Escreva um programa que leia três números e
# que imprima o maior e o menor

a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

print(f'O menor valor digitado foi: {menor}')
print(f'O maior valor digitado foi: {maior}')
