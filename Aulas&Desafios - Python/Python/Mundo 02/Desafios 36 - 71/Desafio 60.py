from math import factorial
n = int(input('Digite um número pra eu calcular seu fatorial: '))
f = factorial(n)
print ('Calculando {}! = '.format(n), end='')
for c in range(n, 0, -1):
    if c > 1:
        print('{} x'.format(c), end=' ')
    else:
        print(c, end=' ')
print('= {}'.format(f))
