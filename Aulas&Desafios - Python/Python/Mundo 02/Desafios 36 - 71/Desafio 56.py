s = 0
mv = 0
mn = 0
for c in range (1, 5):
	print('==== {}ª PESSOA ===='.format(c))
	nome = str(input(' Nome: '))
	idade = int(input(' Idade: '))
	sexo = int(input(' Sexo: \n [1] Maculino \n [2] Feminino		Resposta: '))
	s += idade
	if sexo == 1 and idade > mv:
		nmv = nome
	if sexo == 2 and idade < 20:
		mn += 1
m = s / 4 
print('A média de idade do grupo é {}.'.format(m))
print('O homem mais velho é o {}'.format(nmv))
print('Existem {} mulheres que tem menos de 20 anos.'.format(mn))