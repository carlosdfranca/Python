n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
print('A sua média é {:.1f}'.format(m))
if m >= 6.0:
    print('Sua nota foi boa! PARABÉNS!!')
else:
    print('Você precisa melhorar. Estude mais!')
