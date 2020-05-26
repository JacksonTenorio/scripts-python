from math import hypot
b = float(input('Comprimento do cateto oposto: '))
c = float(input('Comprimento do cateto adjecente: '))
a = hypot(b, c)
print('A hitotenusa vai medir: {:.2f}'.format(a))
