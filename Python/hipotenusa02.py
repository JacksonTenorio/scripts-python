import math
b = float(input('Comprimento do cateto oposto: '))
c = float(input('Comprimento do cateto adjecente: '))
a = math.hypot(b, c)
print('A hipotenusa via medir: {:.2f}'.format(a))
