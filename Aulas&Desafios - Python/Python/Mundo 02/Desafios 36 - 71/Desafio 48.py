s = 0
for c in range(0, 501, 3):
	if c % 3 == 0:
		print (c, end='..')
		s = s + c
print ('A soma de tdos os multiplos de 3 é {}'.format(s)) 