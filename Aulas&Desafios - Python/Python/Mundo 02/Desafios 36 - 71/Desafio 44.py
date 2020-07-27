print('Bom dia! Qal é o preço do produto que você deseja fazer a compra? ')
p = float(input('Preço do produto:(R$) '))
v = int(input('Em quantas vezes você deseja pagar? '))
if v == 1:
	dc = int(input('Dinheiro ou cartão?(para cartão: 1/ para dinheiro: 2) '))
	if dc == 1: 
		p = p + ((p / 100) * 5)
		print('Seu produto teve um desconto de 5%  e ficou R${} .'.format(p))
	else:
		print('Seu produto teve um desconto de 10%  e ficou R${} .'.format(p))
elif v == 2:
	print('Ok. você pode pagar em até 2x sem juros.')
elif v > 2:
	p =  p + ((p / 100) * 20)
	print('Pagando {}x no cartão vc recebe temque paagr 20%  de juros. O produto ficou RS${}.'.format(v , p))