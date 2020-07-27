print('=============================')
print('		10 TERMOS DE UMA PA		')
print('=============================')
i = int(input('Primeiro termo: '))
p = int(input('Razão: '))
d = i + (10 - 1) * p
for c in range(i, d + p, p):
	print('{}'.format(c), end='>>>')
print('FIM')