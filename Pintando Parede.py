altura = float(input('Digite a altura da parede:'))
largura = float(input('Digite a largura da parede:'))
area = altura * largura / 2
tinta = area / 2
print('A área da parede é de {}m².'.format(area))
print('A quantidade de litros de tinta necessária será: {}'.format(tinta))