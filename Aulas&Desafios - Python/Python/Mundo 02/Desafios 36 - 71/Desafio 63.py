print('-=' * 20)
print('SEQUÊNCIA DE FIBONACCI')
print('-=' * 20)
n =  int(input('Quantos números da sequência de Fibonacce você quuer ver? '))
n1 = 0
n2 = 1
print('{} - {}'.format(n1, n2), end=' - ')
for c in range (0, n-2):
    n3 = n1 + n2
    print('{}'.format(n3), end=' - ')
    n1 = n2
    n2 = n3
print('Fim')
