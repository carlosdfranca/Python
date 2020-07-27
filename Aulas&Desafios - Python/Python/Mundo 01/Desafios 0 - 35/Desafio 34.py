s = int(input('Qual é o seu salário? '))

if s <= 1250:
	a = (s / 100 * 15) + s 
	print('Vê ganhou um aumento de R${:.2f}'.format(a))
else:
	a = (s / 100 * 10) + s 
	print('Vê ganhou um aumento de R${:.2f}'.format(a))
print('Espero que tenha gostado da notícia!')