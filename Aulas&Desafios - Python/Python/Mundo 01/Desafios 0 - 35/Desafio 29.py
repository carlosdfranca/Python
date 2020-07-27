v = int(input('Qual foi a velocidade do carro?(Km) '))
if v > 80:
    print('Você estava acima do limite de velocidade de 80Km.')
    multa = (v - 80) * 7
    print('Você vai ter que pagar R${:.2f}'.format(multa))
else:
    print('Vôce estava no limite de velocidade')
print('Tenha um bom dia.')