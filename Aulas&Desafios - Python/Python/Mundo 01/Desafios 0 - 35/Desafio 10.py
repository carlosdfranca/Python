print('=========Desafio 10=========')
print('Conversão de Real para Dolar')
r = int(input('Quantos reais você tem agora na carteira? '))
d = r / 5.35 
print('Com R${} você pode comprar ${:.2f} dólares.'.format(r,d))