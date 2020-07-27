n1 = float(input('Nota do primeiro semestre: '))
n2 = float(input('Nota do segundo semestre: '))
m = (n1 + n2) / 2
print('Sua média é {:.1f}'.format(m))
if m < 5 and m :
	print('REPROVADO')
elif m >= 5 and m < 7:  
	print('RECUPERAÇÃO')
else:
	print('APROVADO')