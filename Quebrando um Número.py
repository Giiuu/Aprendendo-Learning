from math import floor, ceil
num = float(input('Digite um número quebrado: '))
print('A versão arredondada de {} é: {} para cima e {} para baixo'.format(num, ceil(num), floor(num)))