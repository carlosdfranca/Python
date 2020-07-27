s = 0
for c in range(0, 6):
	ano = int(input('Em queano você nasceu? '))
	idade = 2020 - ano
	if idade < 18:
		s = s + 1
print('{} nego ainda n é de maior.'.format(s))