from random import randint
itens = ('Pedra','Papel','Tesoura')
pc = randint(0, 2)
user = int(input('Escolha?: \n [0]Pedra \n [1]Papel \n [2]Tesoura \n Qual é a sua jogada? '))
print(' JO \n JEN \n PO!!!')
print('-=-=-=-=-=-=-=-=-=-=-=--=-=')
print('O computador escolheu: {}'.format(itens[pc]))
print('O jogador escolheu: {}'.format(itens[user]))
print('-=-=-=-=-=-=-=-=-=-=-=--=-=')
if pc < user or pc == 3 and user == 1:
	print('JOGADOR VENCEU')
elif pc == user:
	print('EMPATE')
elif pc > user or user == 3 and pc == 1:
	print('COMPUTADOR VENCEU')
