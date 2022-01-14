# Faça um programa que calcule o aumento de um salário.
# Ele deve solicitar o valor do salário e a porcentagem
# do aumento. Exiba o valor do aumento e do novo salário.

salario = float(input('Digite o salário base: '))
aumento = float(input('Digite o percentual de aumento: '))
diferenca = salario * (aumento/100)
print(f'Novo salário: R${round(diferenca + salario,2)}')
print(f'Aumento de: R${round(diferenca,2)}')
