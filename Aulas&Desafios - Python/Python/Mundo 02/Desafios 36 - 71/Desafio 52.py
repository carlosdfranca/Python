n = int(input('Digite um número: '))
tot = 0
for c in range(1 , n+1):
	if n % c == 0:
		tot = tot + 1
print('FIM')
print('O número {} é divisivel por {} números.'.format(n, tot))
if tot == 2:
	print('O número é primo.')
else:
	print('O número não é primo')