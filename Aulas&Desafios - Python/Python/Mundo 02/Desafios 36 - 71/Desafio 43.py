print('CALCULO DO IMC')
peso = float(input('Quanto você pesa? '))
altura = float(input('Qual é a sua altura? '))
IMC = peso / altura ** 2
print('Seu IMC é {}.'.format(IMC))
if  IMC  < 18.5:
	print('Você está abaixo do peso. ')
elif IMC >= 15.5 and IMC < 25: 
	print('Você está no seu peso ideal. ')
elif IMC >= 25 and IMC < 30:
	print('Você está na faixa do sobrepeso. ')
elif IMC >= 30 and IMC < 40:
	print('Você está na faixa da obesidade ')
elif IMC >= 40:
	print('Você está na faixa da obesidade mórbida. ')