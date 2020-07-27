from math import sin, cos, tan, radians
n = float(input('Digite o valor de um ângulo: '))
ang = radians(n)
print('sen = {:.2f}, cos = {:.2f} tan = {:.2f}'.format(sin(ang), cos(ang), tan(ang)))