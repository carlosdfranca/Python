print('SEPARAÇÃO DE CATEGORIAS PARA NATAÇÃO')
ano = int(input('Em que ano você nasceu? '))
idade = 2020 - ano
if idade <= 9:
	print('Categoria: MIRIM')
elif idade <= 14:
	print('Categoria: INFANTIL')
elif idade <= 19:
	print('Categoria: JUNIOR')
elif idade <= 21:
	print('Categoria: SÊNIOR')
else:
	print('Categoria: MASTER')