# Escreva um programa que pergunte a velocidade do carro de
# um usuário. Caso ultrapasse 80 km/h, exiba uma mensagem
# dizendo que o usuário foi multado. Nesse caso, exiba o
# valor da multa, cobrando R$ 5 por km acima de 80 km/h.

velocidade = float(input('Digite a velocidade registrada: '))
if velocidade > 80:
    print(f'Velocidade ultrapassada em: {velocidade-80}')
    print(f'Valor da multa: R${(velocidade-80)*5}')