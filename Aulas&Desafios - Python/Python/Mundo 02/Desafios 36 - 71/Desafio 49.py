print('TABUADA DO 1 AO 10')
n = int(input('Digite o número que deseja ver a tabiada: '))
for c in range(1, 11):
	print ('{} x {:2} = {}'.format(n, c, n*c))