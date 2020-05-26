b = float(input('Comprimento do cateto oposto:'))
c = float(input('Comprimento do cateto adjecente:'))
a = (b ** 2 + c ** 2) ** (1/2)
print('A hipotenusa vai medir: {:.2f}'.format(a))  