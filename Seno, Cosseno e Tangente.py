from math import sin, cos, tan, radians
num = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(num))
cosseno = cos(radians(num))
tangente = tan(radians(num))
print('O ângulo de {} tem o SENO de {:.2f}, cosseno de {:.2f} e tangente de {:.2f}.'.format(num, seno, cosseno, tangente))