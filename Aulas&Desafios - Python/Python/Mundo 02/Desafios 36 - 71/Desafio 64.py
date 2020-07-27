r = 0
cont = 0
soma = 0
while r != 999:
    cont += 1
    soma += r
    r = int(input('Digite um número [999 para parar]: ' ))
print('Você deu {} números'.format(cont - 1))
print('O resultado da soma entre os números é {}'.format(soma))
