import matplotlib.pyplot
temperturas = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
gramasKNO3 = [13.3, 20.9, 31.6, 45.8, 63.9, 85.5, 110, 138, 169, 202, 246]
matplotlib.pyplot.plot(temperturas, gramasKNO3)
matplotlib.pyplot.title('Solubilidade do KNO3 em Água')
matplotlib.pyplot.xlabel('TEMPERATURA')
matplotlib.pyplot.ylabel('GRAMAS DE KNO3/100g DE ÁGUA')
matplotlib.pyplot.show()