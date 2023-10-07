rs = float(input('Digite quantos reais você tem e iremos transformar em dólar: R$'))
dol = rs / 5.17
print('Com R${:.2f} você pode comprar US${:.2f}.'.format(rs, dol))