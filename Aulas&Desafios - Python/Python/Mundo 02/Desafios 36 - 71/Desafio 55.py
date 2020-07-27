mp = 0 
for c in range(0, 5):
	name = str(input('Digite o seu nome: '))
	p = float(input('Quanto você pesa? '))
	if p > mp:
		mp = p
		mn = name
print('O mais gordo entre vcs é o {} com {}kg'.format(mn, mp))