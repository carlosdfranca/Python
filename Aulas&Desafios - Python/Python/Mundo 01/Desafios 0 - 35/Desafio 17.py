from math import hypot
catO = float(input('Digite o comprimento do catesto oposto:'))
catA = float(input('Digite o comprimento do catesto adjacente:'))
print('A comprimento hipotenusa do triangulo com os parametros que você descreveu é: {}'.format(hypot(catO,catA)))