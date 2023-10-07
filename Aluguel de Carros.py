km = float(input('Quantos KM o carro andou?'))
dias = int(input('Quantos dias o carro ficou alugado?'))
valor = (60 * dias) + (0.15 * km)
print('O valor do aluguel do carro foi R${:.2f}'.format(valor))