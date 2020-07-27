print('=========Desafio 12=========')
print('Desconto de 5%')
p = float(input('Qual é o preço do produto?(R$) '))
d = p/100*5
pd = p-d
print('Olha, como estamos em liquidação, você ganhou um desconto de 5%!')
print('O produto que você comprou por R${} ganhou o desconto de R${} e agora está valendo R${}'.format(p,d,pd))