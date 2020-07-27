km = int(input('Qual é a distância da viagem percorrida? '))
if km <= 200:
    p = km * 0.50
    print('O preço da viagem é de R${:.2f}'.format(p))
else:
    p = km * 0.45
    print('O preço da viagem é de R${:.2f}'.format(p))
print('Você pode pagar o que deve no caixa a sua esquerda. \n Tenha um bom dia!')